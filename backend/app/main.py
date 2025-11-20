from fastapi import FastAPI
from .core.database import engine
from .core import deps

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}
