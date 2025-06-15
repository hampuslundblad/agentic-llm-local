from fastapi import FastAPI
from chat_bot.main import stream_graph_updates
app = FastAPI()
from pydantic import BaseModel

class Message(BaseModel):
    content: str

@app.get("/")
async def root():
    response = stream_graph_updates("What is the capital of France?")
    return {"message": response}

@app.post("/api/message")
async def post_message(message: Message):
    response = stream_graph_updates(message.content)
    return {"message": response}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}