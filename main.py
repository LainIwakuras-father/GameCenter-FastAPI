from loguru import logger
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from app.api.all_routers import routers

app = FastAPI(title="GamaCenterAPI", description="API к престоящему мероприятию", version="0.0.1")



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],#замени на список доменов, которые могут обращаться к нашему API
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# @app.on_event("startup")
# async def on_startup():
#     """Инициализация базы данных при запуске приложения"""
#     await init_db()


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


app.include_router(router=routers)

if __name__ == "__main__":
    logger.info("Server is running....")
    uvicorn.run(app, host="127.0.0.1", port=8000)