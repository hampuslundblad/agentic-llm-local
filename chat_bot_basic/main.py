from typing import Annotated

from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages

from langchain_core.messages import SystemMessage   
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


from langchain_ollama import ChatOllama

from IPython.display import Image, display

from prompts.main import judge_prompt_long
from langgraph.checkpoint.memory import MemorySaver


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

# Start building the graph

graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", call_model)


graph_builder.add_edge(START, "chatbot")

# Note in prod use something like SQLiteSaver or PostgresSaver
memory = MemorySaver()

# graph = graph_builder.compile()
graph = graph_builder.compile(checkpointer=memory)


def stream_graph_updates(user_input: str):
    config = {"configurable": {"thread_id": "2"}}
    events = graph.stream(
        {"messages": [{"role": "user", "content": user_input}]}, config, stream_mode="values")

    print(user_input)

    for event in events:
        event["messages"][-1].pretty_print()
        final_event = event  # This feels so hacky
    return final_event["messages"][-1].content

#stream_graph_updates("I cast necromentia while my opponent controls leyline of sanctity, what happens?")