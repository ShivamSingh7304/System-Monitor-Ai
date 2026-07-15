import psutil
from langchain.tools import tool

@tool
def battery_stats():
    '''Return current battery stats'''

    return{
        "battery percentage":(psutil.sensors_battery()).percent,
        "power plugged":(psutil.sensors_battery()).power_plugged
    }


if __name__ == "__main__":
    result= battery_stats.invoke({})
    print(result)
    print(battery_stats.description)