# System Monitoring Application (Python, Docker, Kubernetes)

A simple system monitoring service built with **Python** that exposes **CPU, memory, and disk metrics** via REST APIs.  
The application is containerized using **Docker** and deployed on **Kubernetes** using a Deployment and Service.

This project demonstrates end-to-end skills in **backend development, containerization, and Kubernetes deployment**.

---

## Features

- REST APIs to fetch:
  - CPU usage
  - Memory usage
  - Disk usage
- Built using FastAPI
- Dockerized application
- Deployed on Kubernetes (Minikube)
- Accessible via Kubernetes Service (NodePort)

---

## Architecture Overview

The application is built as a simple monitoring service and deployed using container and orchestration tools.

- The FastAPI application exposes REST APIs to return system metrics such as CPU, memory, and disk usage.
- The psutil library is used to collect system-level metrics from the running environment.
- The application is packaged into a Docker image to ensure consistency across environments.
- A Kubernetes Deployment runs the container as a Pod inside the cluster.
- A Kubernetes Service (NodePort) exposes the application so it can be accessed from outside the cluster.

This setup demonstrates how a backend service can be containerized and deployed on Kubernetes.

---

## API Endpoints

| Endpoint | Description |
|--------|------------|
| `/` | Health check |
| `/metrics/system` | CPU and memory metrics |
| `/metrics/disk` | Disk usage metrics |

---

## Run Locally (Python)

### Prerequisites
- Python 3.11 or later
- pip

### Steps

Install dependencies:
```bash
pip install fastapi uvicorn psutil


###Run the application:

python main.py

###Access the API

http://localhost:8000/

http://localhost:8000/metrics/system

http://localhost:8000/metrics/disk

###Run with Docker

Prerequisites

Docker installed and running

###Build Docker Image
docker build -t system-monitor .

###Run Docker Container
docker run -p 8000:8000 system-monitor

Access the API

http://localhost:8000/

http://localhost:8000/metrics/system

http://localhost:8000/metrics/disk

Deploy on Kubernetes (Minikube)
Start Minikube Cluster
minikube start

Load Docker Image into Minikube
minikube image load system-monitor

Apply Kubernetes Manifests
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

Verify Resources
kubectl get pods
kubectl get svc

Access Application
minikube service system-monitor

Or get the URL:

minikube service system-monitor --url
