import os
import requests
import logging
from concurrent import futures
import grpc
from fastapi import FastAPI
import uvicorn
from threading import Thread
from dotenv import load_dotenv
import scaler_pb2
import scaler_pb2_grpc

# Inicialização das variáveis de ambiente
load_dotenv()
ONPREMISE_SERVICES = os.getenv("ONPREMISE_ENDPOINTS", "http://onpremise:8080/health").split(",")

# Configuração de Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s]: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class ExternalScalerServicer(scaler_pb2_grpc.ExternalScalerServicer):
    def __init__(self):
        self.last_status = None

    def check_onpremise_status(self):
        for service in ONPREMISE_SERVICES:
            try:
                response = requests.get(service.strip(), timeout=5)
                if response.status_code != 200:
                    return 1  # On-premise DOWN
            except requests.RequestException as e:
                logging.error(f"Falha ao acessar {service}: {e}")
                return 1  # On-premise DOWN
        return 0  # Todos endpoints on-premise OK

    def log_status_change(self, current_status):
        if current_status != self.last_status:
            status_str = "DOWN" if current_status else "UP"
            logging.info(f"Status do ambiente on-premise mudou para: {status_str}")
            self.last_status = current_status

    def IsActive(self, request, context):
        status = self.check_onpremise_status()
        self.log_status_change(status)
        return scaler_pb2.IsActiveResponse(result=bool(status))

    def GetMetricSpec(self, request, context):
        metric_spec = scaler_pb2.MetricSpec(
            metricName="onpremise-app-health",
            targetSize=1
        )
        return scaler_pb2.GetMetricSpecResponse(metricSpecs=[metric_spec])

    def GetMetrics(self, request, context):
        metric_value = self.check_onpremise_status()
        self.log_status_change(metric_value)
        metric = scaler_pb2.MetricValue(
            metricName="onpremise-app-health",
            metricValue=metric_value
        )
        return scaler_pb2.GetMetricsResponse(metricValues=[metric])

# Health Check HTTP com FastAPI
app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

def start_http_server():
    uvicorn.run(app, host="0.0.0.0", port=8000)

def serve():
    # Inicializa servidor gRPC
    grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    scaler_pb2_grpc.add_ExternalScalerServicer_to_server(ExternalScalerServicer(), grpc_server)
    grpc_server.add_insecure_port('[::]:6000')

    # Start HTTP server em uma thread separada
    http_thread = Thread(target=start_http_server, daemon=True)
    http_thread.start()

    grpc_server.start()
    logging.info("🚀 External Scaler gRPC rodando na porta 6000")
    logging.info("🚦 Health Check HTTP rodando na porta 8000")
    grpc_server.wait_for_termination()

if __name__ == '__main__':
    logging.info("Inicializando External Scaler...")
    serve()
