import psutil
import time

def get_system_metric():
        
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()

        return {
            "timestamp": time.time(),
            "cpu_percent":cpu,
            "memory_percent":memory.percent,
            "memory_used_mb":memory.used/(1024*1024),
            "memory_total_mb":memory.total/(1024*1024),
            "available": memory.available
        }
    
if __name__=="__main__":
    print(get_system_metric())
    