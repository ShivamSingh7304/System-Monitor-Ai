import psutil
from langchain.tools import tool

@tool
def disk_status():
    """Return disk usage for all available drives."""

    drives = ["C:\\", "D:\\", "E:\\"]
    disk_info = {}

    for drive in drives:
        try:
            usage = psutil.disk_usage(drive)

            disk_info[drive[0]] = {
                "total_gb": round(usage.total / (1024**3), 2),
                "used_gb": round(usage.used / (1024**3), 2),
                "free_gb": round(usage.free / (1024**3), 2),
                "usage_percent": usage.percent
            }

        except FileNotFoundError:
            disk_info[drive[0]] = "Drive not found"

    return disk_info


if __name__ == "__main__":
    result = disk_status.invoke({})
    print(result)