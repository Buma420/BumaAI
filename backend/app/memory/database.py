import json
from pathlib import Path


MEMORY_FILE = Path("memory.json")


def save_memory(memory: str):
    memories = load_memories()

    memories.append({
        "memory": memory
    })

    with open(MEMORY_FILE, "w") as file:
        json.dump(memories, file, indent=4)


def load_memories():
    if not MEMORY_FILE.exists():
        return []

    with open(MEMORY_FILE, "r") as file:
        return json.load(file)