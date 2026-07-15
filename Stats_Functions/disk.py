import psutil
from langchain.tools import tool

@tool
def disk_status():
    '''Return current Disk stats'''
    usage = psutil.disk_usage("C:\\")
    
    return{
        "total_gb": round(usage.total / (1024**3), 2),
        "used_gb": round(usage.used / (1024**3), 2),
        "free_gb": round(usage.free / (1024**3), 2),
        "usage_percent": usage.percent
    }

if __name__ =="__main__":
    result = disk_status.invoke({})
    print(result)
    print(disk_status.description)