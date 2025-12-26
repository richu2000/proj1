# api/app.py
from fastapi import FastAPI
from collectors.system_info import get_system_metric, get_disk_usage

app = FastAPI(title="System Monitoring API")

@app.get("/")
def read_root():
    return {"status": "ok", "message": "System Monitoring API is running"}

@app.get("/metrics/system")
def read_system_metrics():
    return get_system_metric()

@app.get("/metrics/disk")
def read_disk_metrics(path: str = "/"):
    # Example: /metrics/disk?path=/
    return get_disk_usage(path)
