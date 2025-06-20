from typing import Annotated

from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages

from langchain_ollama import ChatOllama

from chat_bot.tools import search_tool, wiki_tool


from IPython.display import Image, display

from langgraph.prebuilt import ToolNode, tools_condition

from langgraph.checkpoint.memory import MemorySaver
from langgraph.types import Command, interrupt
from langchain_core.tools import tool


class State(TypedDict):
    # Messages have the type "list". The `add_messages` function
    # in the annotation defines how this state key should be updated
    # (in this case, it appends messages to the list, rather than overwriting them)
    messages: Annotated[list, add_messages]




def chatbot(state: State):
    return {"messages": [llm_with_tools.invoke(state["messages"])]}


@tool
def human_assistance(query: str) -> str:
    """Request assistance from a human."""
    human_response = interrupt({"query": query})
    return human_response["data"]


llm = ChatOllama(model="llama3.2", base_url="http://localhost:11434")

tools = [search_tool, wiki_tool]

llm_with_tools = llm.bind_tools(tools)

# Start building the graph

graph_builder = StateGraph(State)

graph_builder.add_node("chatbot", chatbot)

tool_node = ToolNode(tools=tools)

graph_builder.add_node("tools", tool_node)

graph_builder.add_conditional_edges(
    "chatbot",
    tools_condition,
)
# The first argument is the unique node name
# The second argument is the function or object that will be called whenever
# the node is used.
graph_builder.add_edge("tools", "chatbot")
graph_builder.add_edge(START, "chatbot")

# Note in prod use something like SQLiteSaver or PostgresSaver
memory = MemorySaver()

#graph = graph_builder.compile()
graph = graph_builder.compile(checkpointer=memory)

def stream_graph_updates(user_input: str):
    config = {"configurable": {"thread_id": "1"}}
    events = graph.stream(
        {"messages": [{"role": "user", "content": user_input}]}, config, stream_mode="values")

    print(user_input)

    for event in events:
        
       # for value in event.values():
        #    print("Assistant:", value["messages"][-1].content)
        
        event["messages"][-1].pretty_print()
        final_event = event
    return final_event["messages"][-1].content
    
    # return event["messages"][-1].content


#response = stream_graph_updates("Lookup using wikipedia what is the capital of France?")
#print("Response", response)
