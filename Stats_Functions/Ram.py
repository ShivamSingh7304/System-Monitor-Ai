from langchain.tools import tool
import psutil

@tool
def ram_stats():
    """Returns the current RAM usage of the system."""
    memory = psutil.virtual_memory()

    return {
        "total_gb": round(memory.total / (1024**3), 2),
        "used_gb": round(memory.used / (1024**3), 2),
        "available_gb": round(memory.available / (1024**3), 2),
        "usage_percent": memory.percent
    }

if __name__ == "__main__":
    result=ram_stats.invoke({})
    print(result)