from fastapi import FastAPI
from judge_bot_rag.main import stream_graph_updates
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    content: str

@app.get("/")
async def root():
    return {"message": "yes the api works"}

@app.post("/api/message")
async def post_message(message: Message):
    response = stream_graph_updates(message.content)
    return {"message": response}
