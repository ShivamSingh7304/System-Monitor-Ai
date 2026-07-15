import psutil
from langchain.tools import tool

@tool
def cpu_stats():
    '''return current CPU stats'''
    return{
        "usage_percentage": psutil.cpu_percent(interval=1),
        "physical_cores": psutil.cpu_count(logical=False),
        "logical_cores": psutil.cpu_count(logical=True),
        "per_core_usage": psutil.cpu_percent(interval=1, percpu=True),
        "current_frequency_mhz": round((psutil.cpu_freq()).current, 2),
        "max_frequency_mhz": round((psutil.cpu_freq()).max, 2)
     }

if __name__ == "__main__":
    result=cpu_stats.invoke({})
    print(result)