from fastapi import FastAPI

app = FastAPI(
    title="My FastAPI App",
    description="Приложение с автоматическим развертыванием на Render",
    version="1.0.0",
    contact={
        "name": "Мейірхан",
        "email": "youremail@example.com"
    }
)

@app.get("/hello", tags=["Demo"], summary="Приветствие", description="Простой тестовый эндпоинт")
async def hello():
    return {"message": "Привет от FastAPI и Render!"}
