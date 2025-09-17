from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
import uuid


import typing as tp

import bcrypt

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

"""
НАСТРОЙКА АДМИНКИ КНОПОЧКИ И ОТОБРАЖЕНИЯ
К моему сожалению, не понимаю почему , но работает только если эта часть кода будет в файле main.py
"""

# Админка для Task
@register(Task)
class TaskAdmin(TortoiseModelAdmin):
    list_display = ["id", "name", "question", "answer"]
    search_fields = ["name", "question"]
    list_filter = ["name"]
    list_display_links = ("name")

# Админка для User
@register(User)
class UserAdmin(TortoiseModelAdmin):
    # exclude = {"hash_password"}
    list_display = ("id", "username", "email", "is_superuser", "is_active", "created_at")
    list_display_links = ("id", "username")
    list_filter = ("id", "username")
    search_fields = ("username", "email", "first_name", "last_name")

    
    formfield_overrides = {  # noqa: RUF012
        
        "hash_password": (WidgetType.PasswordInput, {"passwordModalForm": False}),
    }

    async def authenticate(self, username: str, password: str) -> uuid.UUID | int | None:
        user = await self.model_cls.filter(username=username,  is_superuser=True).first()
        if not user:
            return None
        if not verify_password(password.encode(), user.hash_password):
            return None
        return user.id

    async def change_password(self, id: uuid.UUID | int, password: str) -> None:
        user = await self.model_cls.filter(id=id).first()
        if not user:
            return
        user.hash_password = get_password_hash(password.encode())
        await user.save(update_fields=("hash_password",))

# Админка для Station
@register(Station)
class StationAdmin(TortoiseModelAdmin):
    list_display = ["id", "name", "points", "time","task"]
    list_display_links = ["id", "name"]
    search_fields = ["name",]
    list_filter = ["points"]
    formfield_overrides = {  # noqa: RUF012
        "image": (WidgetType.Upload,{"required": False})
    }
    async def orm_save_upload_field(self, obj: tp.Any, field: str, base64: str) -> None:
        # convert base64 to bytes, upload to s3/filestorage, get url and save or save base64 as is to db (don't recomment it)
        setattr(obj, field, base64)
        await obj.save(update_fields=(field,))


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
    form_fields = ["user", "name", "station"]
    
    # # ПРАВИЛЬНАЯ настройка для отношений
    # formfield_overrides = {
    #     "user": {
    #         "type": WidgetType.Select,
    #         "attrs": {
    #             "required": True,
    #             "queryset": lambda: User.all(),
    #             "display_field": "username",
    #             "placeholder": "Выберите пользователя"
    #         }
    #     },
    #     "station": {
    #         "type": WidgetType.Select,
    #         "attrs": {
    #             "required": False,
    #             "queryset": lambda: Station.all(),
    #             "display_field": "name",
    #             "placeholder": "Выберите станцию"
    #         }
    #     },
    # }










































# async def test():
      
#     await User.create()

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    try:         
        await init_db()
        logger.info("создаю БД")
        # user = await User.get_or_none(username="admin")
        # if not user:
        #     hash_password = get_password_hash("admin")
        #     await User.create(username="admin", hash_password=hash_password, is_superuser=True)
        #     logger.info("создаю админа если его не было")
        #         # from tortoise import Tortoise
        #         # print(Tortoise.apps)

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
    uvicorn.run("main:app", host="0.0.0.0", port=8000)