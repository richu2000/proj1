# proj1
Built a lightweight, Python-based system monitoring tool capable of collecting real-time CPU usage, memory usage, process information, and network details using Linux system internals and psutil.

Later we can add:

K8s CronJob to periodically scrape & store metrics

Maybe Prometheus scraping & Grafana dashboards

But for now: basic monitoring app on K8s.

🧩 Phase 1: Turn Your Collectors into an HTTP API (FastAPI)

Right now you have:

collectors/system_info.py → get_system_metric() + get_disk_usage()

A main.py that just prints

We’ll change it to a FastAPI app.

1️⃣ Install FastAPI & Uvicorn (once)

In your venv / system:

pip install fastapi uvicorn

2️⃣ Create api/app.py

Inside your project (projectA/), create a folder api if not there:

mkdir -p api


Create file: api/app.py:

from fastapi import FastAPI
from collectors.system_info import get_system_metric, get_disk_usage

app = FastAPI(title="System Monitoring API")

@app.get("/metrics/system")
def read_system_metrics():
    return get_system_metric()

@app.get("/metrics/disk")
def read_disk_metrics():
    return get_disk_usage("/")

@app.get("/")
def read_root():
    return {"status": "ok", "message": "System Monitoring API is running"}

3️⃣ Update main.py to run the API (for local dev)
import uvicorn

if __name__ == "__main__":
    uvicorn.run("api.app:app", host="0.0.0.0", port=8000, reload=True)

4️⃣ Run it locally

From project root:

python main.py


Then open in browser:

http://localhost:8000/ → health

http://localhost:8000/metrics/system

http://localhost:8000/metrics/disk

If you see JSON → you now have a proper monitoring API 🎉

🐳 Phase 2: Dockerize the Monitoring App

Once the API works, we’ll create a Dockerfile like:

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["python", "main.py"]


And a simple requirements.txt:

fastapi
uvicorn
psutil


Then:

docker build -t system-monitor:latest .
docker run -p 8000:8000 system-monitor:latest

☸️ Phase 3: Kubernetes Deployment + Service

Later, we’ll add a k8s/ folder with:

deployment.yaml – runs your container

service.yaml – exposes it inside cluster or via NodePort/Ingress

Example (high level):

apiVersion: apps/v1
kind: Deployment
metadata:
  name: system-monitor
spec:
  replicas: 1
  selector:
    matchLabels:
      app: system-monitor
  template:
    metadata:
      labels:
        app: system-monitor
    spec:
      containers:
      - name: system-monitor
        image: your-docker-image:tag
        ports:
        - containerPort: 8000


And a Service for it.

We’ll do this once your Docker image is ready.
