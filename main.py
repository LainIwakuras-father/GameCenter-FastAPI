from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastadmin import fastapi_app as admin_app

from loguru import logger
from tortoise import Tortoise
import uvicorn


from app.utils.create_superuser import create_superuser
from app.api.all_routers import routers
from app.db.db import close_db, init_db
from app.models.user import User


from dotenv import load_dotenv
load_dotenv()
# async def test():
      
#     await User.create()

@asynccontextmanager
async def lifespan_app(app: FastAPI) -> AsyncGenerator[None, None]:
            await init_db()
            logger.info("создаю БД")
            # await create_superuser()
            # await test()
            # logger.info("создаю тестовые сущности")
            # db connected
            yield
            # app teardown
            # db connections closed
            await close_db()
            logger.info("закрыл БД")

app = FastAPI(
    title="GamaCenterAPI",
    description="API к престоящему мероприятию",
    version="0.0.1", lifespan=lifespan_app
)

app.mount("/admin", admin_app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],#замени на список доменов, которые могут обращаться к нашему API
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

\
app.include_router(router=routers)



# app.get("/health")
# async def health_check():
#     try:
#         await Tortoise.get_connection("default").execute_query("SELECT 1")
#         return {"status": "healthy"}
#     except Exception:
#         return {"status": "unhealthy"}, 500

if __name__ == "__main__":
    logger.info("Server is running....")
    uvicorn.run(app, host="127.0.0.1", port=8000)