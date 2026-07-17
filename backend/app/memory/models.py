from pydantic import BaseModel


class Memory(BaseModel):
    content: str
    memory_type: str
    importance: int