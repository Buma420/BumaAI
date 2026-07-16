from fastapi import FastAPI

app = FastAPI(
    title="BumaAI",
    description="Personal AI companion backend",
    version="0.1.0"
)


@app.get("/")
def home():
    return {
        "message": "BumaAI is alive 🧠",
        "version": "0.1.0"
    }

    from fastapi import FastAPI

app = FastAPI(
    title="BumaAI",
    description="Personal AI companion backend",
    version="0.1.0"
)


@app.get("/")
def home():
    return {
        "message": "BumaAI is alive 🧠",
        "version": "0.1.0"
    }

    