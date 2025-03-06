FROM python:3.10.14-slim

WORKDIR /app

COPY . /app/

RUN pip install --no-cache-dir --root-user-action=ignore -r requirements.txt

# Expor portas gRPC e HTTP
EXPOSE 6000 8000

CMD ["python", "scaler.py"]