from fastapi import FastAPI
from backend.app.routes import decisions

app = FastAPI(
    title="Legal Assistant API",
    description="Арбитражный помощник: анализ, прогноз, фильтрация",
    version="0.1.0"
)

app.include_router(decisions.router)

@app.get("/")
def read_root():
    return {"message": "Legal Assistant API is running"}
