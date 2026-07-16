from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="BumaAI",
    description="Personal AI companion backend",
    version="0.1.0"
)


class ChatMessage(BaseModel):
    message: str


@app.get("/")
def home():
    return {
        "message": "BumaAI is alive 🧠",
        "version": "0.1.0"
    }


@app.post("/chat")
def chat(chat_message: ChatMessage):
    return {
        "reply": f"BumaAI received: {chat_message.message}"
    }