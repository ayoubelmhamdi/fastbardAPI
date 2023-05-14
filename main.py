
from fastapi import FastAPI
# from fastapi import Request
from pydantic import BaseModel

from Bard import Chatbot

app = FastAPI()


class Message(BaseModel):
    session_id: str
    message: str


@app.post("/ask")
async def ask(message: Message) -> str:
    topk = Chatbot(message.session_id).ask(message.message)
    return topk["content"]
