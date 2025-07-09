from fastapi import FastAPI
from .presentation.user_router import router as user_router

app = FastAPI(
    title="Python FastAPI DDD Template",
    description="A template for building microservices with Python, FastAPI, and DDD.",
    version="0.1.0"
)

app.include_router(user_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Python FastAPI DDD Template"}
