from fastapi import FastAPI
from pydantic import BaseModel
from app.memory.database import save_memory, load_memories
from app.memory.models import Memory 

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

    memory = Memory(
        content=chat_message.message,
        memory_type="conversation",
        importance=5
    )

    save_memory(memory)

    memories = load_memories()

    return {
        "reply": f"BumaAI remembered: {chat_message.message}",
        "memory_count": len(memories)
    }