# collectors/system_info.py
import psutil
import platform
from datetime import datetime

def get_system_metric():
    cpu_percent = psutil.cpu_percent(interval=1)
    virtual_mem = psutil.virtual_memory()
    boot_time = datetime.fromtimestamp(psutil.boot_time()).isoformat()

    return {
        "hostname": platform.node(),
        "os": platform.system(),
        "os_version": platform.version(),
        "cpu": {
            "percent": cpu_percent
        },
        "memory": {
            "total": virtual_mem.total,
            "available": virtual_mem.available,
            "used": virtual_mem.used,
            "percent": virtual_mem.percent,
        },
        "boot_time": boot_time,
    }

def get_disk_usage(path: str = "/"):
    disk = psutil.disk_usage(path)
    return {
        "path": path,
        "total": disk.total,
        "used": disk.used,
        "free": disk.free,
        "percent": disk.percent,
    }
