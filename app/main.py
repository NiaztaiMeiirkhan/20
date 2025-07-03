from fastapi import FastAPI
from app.routers.hello import router as hello_router

app = FastAPI(
    title="CD FastAPI Project",
    description="Пример FastAPI приложения с авторазвёртыванием на Render",
    version="1.0.0"
)

app.include_router(hello_router)
