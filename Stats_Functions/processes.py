import psutil
from langchain.tools import tool


@tool
def running_processes():
    """Return a list of currently running processes."""

    processes = []

    for process in psutil.process_iter(
        ['pid', 'name', 'username', 'cpu_percent', 'memory_percent']
    ):
        try:
            processes.append({
                "pid": process.info["pid"],
                "name": process.info["name"],
                "user": process.info["username"],
                "cpu_percent": round(process.info["cpu_percent"], 2),
                "memory_percent": round(process.info["memory_percent"], 2)
            })
        except (psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess):
            pass

    return processes


if __name__ == "__main__":
    result = running_processes.invoke({})
    for res in result:
        print(res)
        print()