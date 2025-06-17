from typing import Annotated

from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


from langchain_ollama import ChatOllama

from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver

from IPython.display import Image, display


from judge_bot_rag.tools import card_lookup_tool

from prompts.main import judge_prompt_long
from matplotlib import pyplot as plt
from matplotlib import image as mpimg



class State(TypedDict):
    # Messages have the type "list". The `add_messages` function
    # in the annotation defines how this state key should be updated
    # (in this case, it appends messages to the list, rather than overwriting them)
    messages: Annotated[list, add_messages]


prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            judge_prompt_long,
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

def call_model(state: State) -> State:
    prompt = prompt_template.invoke(state)
    response = llm.invoke(prompt)
    return {"messages": response}


llm = ChatOllama(model="llama3.2", base_url="http://localhost:11434")

tools = [card_lookup_tool]
llm = llm.bind_tools(tools)
# Start building the graph

#Define nodes
graph_builder = StateGraph(State)

graph_builder.add_node("model_node", call_model)
tool_node = ToolNode(tools=tools)
graph_builder.add_node("tools", tool_node)



graph_builder.add_edge(START, "model_node")


graph_builder.add_conditional_edges(
    "model_node",
    tools_condition,
)

graph_builder.add_edge("tools", "model_node")

graph_builder.add_edge("model_node", END)


# Note in prod use something like SQLiteSaver or PostgresSaver
memory = MemorySaver()

# graph = graph_builder.compile()
graph = graph_builder.compile(checkpointer=memory)


def stream_graph_updates(user_input: str):
    config = {"configurable": {"thread_id": "3"}}
    events = graph.stream(
        {"messages": [{"role": "user", "content": user_input}]}, config, stream_mode="values")

    print(user_input)

    for event in events:
        event["messages"][-1].pretty_print()
        final_event = event  # This feels so hacky
    return final_event["messages"][-1].content

#stream_graph_updates("I cast necromentia while my opponent controls leyline of sanctity, what happens?")
stream_graph_updates("What does nature's lore do and what does walking ballista do?")
Image(graph.get_graph().draw_mermaid_png())
#plt.show()
