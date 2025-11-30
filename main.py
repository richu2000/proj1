from collectors.system_info import get_system_metric
from collectors.process_info import get_top_process


if __name__=="__main__":
    print("running proj : ")
    print(get_system_metric())
    print("Top processes: ")
    print(get_top_process())
    