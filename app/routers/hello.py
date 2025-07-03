from fastapi import APIRouter

router = APIRouter(prefix="/hello", tags=["Hello"])

@router.get("/", summary="Скажи привет", description="Простой endpoint для проверки.")
async def say_hello():
    return {"message": "Hello from CD FastAPI!"}
