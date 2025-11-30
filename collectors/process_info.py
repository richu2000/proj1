import psutil
import time

def get_top_process(limit=5):
    processes=[]
    for proc in psutil.process_iter(['pid','name','cpu_percent','memory_percent']):
        try:
            processes.append(proc.info)
        except:
            pass
    
    ##sort by cpu usage
    processes = sorted(processes,key=lambda x: x['cpu_percent'] if x['cpu_percent'] is not None else 0.0, reverse=True)

    return{
        "timestamp":time.time(),
        "top_processes":processes[:limit]
    }

if __name__=="__main__":
    print(get_top_process())