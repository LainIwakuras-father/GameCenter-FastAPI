from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
import uuid


from utils.auth_utils import verify_password, get_password_hash
from models.models import Curator, PlayerTeam, Station, StationOrder, Task, User


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastadmin import fastapi_app as admin_app


from config.logging import app_logger as logger
from tortoise import Tortoise
import uvicorn


from api.all_routers import routers
from db import close_db, init_db


from fastadmin import register
from fastadmin import WidgetType, TortoiseModelAdmin
import fastadmin



# Админка для Task
@register(Task)
class TaskAdmin(TortoiseModelAdmin):
    list_display = ["id", "name", "question", "answer"]
    search_fields = ["name", "question"]
    list_filter = ["name"]


# Админка для User
@register(User)
class UserAdmin(TortoiseModelAdmin):
    # list_display = ["id", "username", "email", "is_active"]
    # search_fields = ["username", "email", "first_name", "last_name"]
    # list_filter = ["is_active", "is_superuser"]
    # exclude = ["password"]  # Скрываем пароль в админке

    list_display = ("id", "username", "is_superuser","is_active")
    list_display_links = ("id", "username")
    list_filter = ("id", "username", "is_superuser")
    search_fields = ("username",)
    formfield_overrides = {  # noqa: RUF012
        "username": (WidgetType.SlugInput, {"required": True}),
        "password": (WidgetType.PasswordInput, {"passwordModalForm": True}),
        "avatar_url": (
            WidgetType.Upload,
            {
                "required": False,
                # Disable crop image for upload field
                # "disableCropImage": True,
            },
        ),
    }

    async def authenticate(self, username: str, password: str) -> uuid.UUID | int | None:
        user = await self.model_cls.filter(username=username,  is_superuser=True).first()
        if not user:
            return None
        if not verify_password(password, user.hash_password):
            return None
        return user.id

    async def change_password(self, id: uuid.UUID | int, password: str) -> None:
        user = await self.model_cls.filter(id=id).first()
        if not user:
            return
        # direct saving password is only for tests - use hash
        user.password = password
        await user.save()

# Админка для Station
@register(Station)
class StationAdmin(TortoiseModelAdmin):
    list_display = ["id", "name", "points", "time"]
    search_fields = ["name", "description"]
    list_filter = ["points"]



# Админка для StationOrder
@register(StationOrder)
class StationOrderAdmin(TortoiseModelAdmin):
    list_display = ["id"]
    list_filter = [
        "first",
        "second",
        "third",
        "fourth",
        "fifth",
        "sixth", 
        "seventh",
        "eighth", 
        "ninth", 
        "tenth"
        ]
    
 #Админка для PlayerTeam
@register(PlayerTeam)
class PlayerTeamAdmin(TortoiseModelAdmin):
    list_display = ["id", "team_name", "score", "current_station"]
    search_fields = ["team_name"]
    list_filter = ["score", "current_station"]



# Админка для Curator
@register(Curator)
class CuratorAdmin(TortoiseModelAdmin):
    list_display = ["id", "name", "station"]
    search_fields = ["name"]
    list_filter = ["station"]











































# async def test():
      
#     await User.create()

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    try:         
        await init_db()
        logger.info("создаю БД")
        user = await User.get_or_none(username="admin")
        if not user:
            hash_password = get_password_hash("admin")
            await User.create(username="admin", hash_password=hash_password, is_superuser=True)
            logger.info("создаю админа если его не было")
                # from tortoise import Tortoise
                # print(Tortoise.apps)
        yield

    except Exception:
        raise
    finally:
        # db connections closed
        await close_db()
        logger.info("закрыл БД")





app = FastAPI(
    title="GamaCenterAPI",
    description="API к престоящему мероприятию",
    version="1.0.0", lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],#замени на список доменов, которые могут обращаться к нашему API
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

\
app.include_router(router=routers)




app.mount("/admin", admin_app)



if __name__ == "__main__":
    logger.info("Server is running....")
    uvicorn.run("main:app", host="127.0.0.1", port=8000,reload=True)