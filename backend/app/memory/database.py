import json
from pathlib import Path
from app.memory.models import Memory


MEMORY_FILE = Path("memory.json")


def save_memory(memory: Memory):
    memories = load_memories()

    memories.append(memory.model_dump())

    with open(MEMORY_FILE, "w") as file:
        json.dump(memories, file, indent=4)


def load_memories():
    if not MEMORY_FILE.exists():
        return []

    with open(MEMORY_FILE, "r") as file:
        return json.load(file)