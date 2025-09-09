from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from loguru import logger
import uvicorn



from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.all_routers import routers
from app.db.db import close_db, init_db, init_tortoise



@asynccontextmanager
async def lifespan_app(app: FastAPI) -> AsyncGenerator[None, None]:
            await init_db()
            logger.info("создаю БД")
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
init_tortoise(app)
logger.info("Иницилизация ORM")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],#замени на список доменов, которые могут обращаться к нашему API
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

\
app.include_router(router=routers)

if __name__ == "__main__":
    logger.info("Server is running....")
    uvicorn.run(app, host="127.0.0.1", port=8000)