import speedtest
from langchain.tools import tool

@tool
def speed_test():
    '''Gives us the current speed of the network'''
    st = speedtest.Speedtest()
    return{
        "download speed":round((st.download()/1_000_000),2),
        "upload speed":round((st.upload()/1_000_000),2)
    }

if __name__ =="__main__":
    result = speed_test.invoke({})
    print(result)
    print(speed_test.description)