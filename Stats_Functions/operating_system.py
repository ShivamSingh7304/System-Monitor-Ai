import platform
from langchain.tools import tool

@tool
def operating_system():
    '''returns info about operating system'''
    return{
        "os":platform.system(),
        "released version":platform.release()
    }

if __name__ == "__main__":
    result = operating_system.invoke({})
    print(result)
    print(operating_system.description)