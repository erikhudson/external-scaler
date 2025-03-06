# Documentação da Implementação de External Scaler Personalizado (gRPC) para KEDA

## Introdução

Este documento descreve a implementação e o funcionamento de um **External Scaler personalizado utilizando gRPC para o KEDA**, projetado para monitorar um ambiente on-premise e realizar o escalonamento automático de pods em um cluster AKS baseado na disponibilidade desse ambiente.

---

## Objetivo da Solução

A solução implementada realiza a seguinte função:

- Monitora continuamente serviços hospedados no ambiente on-premise.
- Utiliza um serviço gRPC que fornece métricas ao KEDA, permitindo que o Kubernetes escale automaticamente as réplicas de um Deployment (como uma aplicação Nginx) com base no status do ambiente on-premise.
- O Deployment configurado no Kubernetes terá:
  - **0 réplicas** quando o ambiente on-premise estiver **disponível**.
  - **Escalamento automático** (até 10 réplicas) quando o ambiente on-premise estiver **indisponível**.

---

## Estrutura do Projeto

```
HPA
├── Dockerfile
├── requirements.txt
├── scaler.proto
├── scaler.py
├── scaler_pb2.py
├── scaler_pb2_grpc.py
├── k8s-deploy/
│   ├── deployment-healthcheck-scaler.yaml
│   ├── nginx-deployment.yaml
│   ├── nginx-scaledobject.yaml
│   └── service-healthcheck-scaler.yaml
```

## Explicação dos Componentes

### External Scaler (gRPC)

A aplicação desenvolvida atua como um External Scaler para o KEDA, expondo uma API gRPC que fornece métricas personalizadas. O External Scaler verifica regularmente o status de endpoints do ambiente on-premise (definidos via variável de ambiente) e retorna uma métrica que indica:

- **0**: Ambiente on-premise está operacional
- **1**: Ambiente on-premise está fora ou com falhas

O scaler utiliza estas métricas para informar ao KEDA se é necessário ou não escalar a aplicação no Kubernetes.

## Estrutura da Aplicação

- **scaler.proto:** Define o contrato gRPC utilizado pelo KEDA.
- **scaler.py**: Código principal do servidor gRPC que verifica o status do on-premise.
- **Dockerfile**: Utilizado para gerar a imagem do servidor gRPC.

## Kubernetes e KEDA

- **ScaledObject (KEDA)**: Recurso do KEDA que especifica qual Deployment será escalado, a métrica usada (external scaler via gRPC) e os limites de réplicas (mínimo e máximo).
- **Service**: Expõe o servidor gRPC dentro do cluster Kubernetes para que o KEDA acesse o servidor de métricas.

## Funcionamento Passo a Passo

1. O External Scaler personalizado (gRPC) é inicializado e começa a monitorar os endpoints do ambiente on-premise.
2. O External Scaler responde às requisições do KEDA com a métrica personalizada:
   - Se qualquer endpoint monitorado estiver indisponível, retorna valor **1**.
   - Se todos endpoints estiverem disponíveis, retorna valor **0**.
3. Com base nessa métrica, o KEDA:
   - Mantém as réplicas do deployment em **0** se o ambiente on-premise estiver operacional.
   - Escala automaticamente o deployment para a quantidade máxima definida caso o on-premise fique indisponível.
   - Retorna para 0 automaticamente após o ambiente on-premise ser restaurado.

## Deploy no Kubernetes

- O External Scaler é implantado como um **Deployment Kubernetes** e exposto através de um **Service** (porta gRPC padrão 6000).
- O KEDA é instalado com suporte para External Scaler habilitado.
- O recurso ScaledObject utiliza a URL do Service do External Scaler para obter as métricas via gRPC.

## Exemplo de fluxo:

```plaintext
KEDA ---> (consulta via gRPC) ---> External Scaler personalizado ---> (HTTP Health Check) ---> Ambiente On-Premise
```

**Resultado:**

- Escalabilidade automática baseada na disponibilidade do ambiente on-premise, proporcionando alta disponibilidade e recuperação automática com mínimo custo operacional, pois mantém recursos desligados ou com baixa utilização quando não necessários.

---

Esta documentação cobre os principais conceitos, arquitetura e fluxo operacional da solução com KEDA e External Scaler personalizado (gRPC).

---

[**Documentação Oficial do KEDA External Scaler:**](https://keda.sh/docs/latest/concepts/external-scalers/)