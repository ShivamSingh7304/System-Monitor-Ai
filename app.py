from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, ToolMessage

from Stats_Functions.cpu import cpu_stats
from Stats_Functions.battery import battery_stats
from Stats_Functions.disk import disk_status
from Stats_Functions.Ram import ram_stats
from Stats_Functions.speed_test import speed_test
from Stats_Functions.operating_system import operating_system

load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile")

tools = [cpu_stats, battery_stats, disk_status, ram_stats, speed_test, operating_system]

llm_with_tools = llm.bind_tools(tools)

tool_map = {tool.name: tool for tool in tools}

print("AI System Monitor")
print("Type 'exit' to quit.")

messages = []

while True:
    query = input("\nYou: ")

    if query.lower() in ["exit", "quit", "bye"]:
        print("Goodbye!")
        break

    messages.append(HumanMessage(content=query))

    while True:
        ai_message = llm_with_tools.invoke(messages)
        messages.append(ai_message)

        if not ai_message.tool_calls:
            print(f"\nAssistant: {ai_message.content}")
            break

        for tool_call in ai_message.tool_calls:
            tool = tool_map[tool_call["name"]]

            try:
                result = tool.invoke(tool_call["args"])
            except Exception as e:
                result = f"Tool execution failed: {e}"

            messages.append(
                ToolMessage(content=str(result), tool_call_id=tool_call["id"])
            )