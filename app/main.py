from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from base64 import b64encode
import io
import os
import random
import uuid


import typing as tp

from fastapi.staticfiles import StaticFiles

from utils.upload_files import save_upload_media
from utils.auth_utils import verify_password, get_password_hash
from models.models import Curator, PlayerTeam, Station, StationOrder, Task, User


from fastapi import FastAPI, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastadmin import fastapi_app as admin_app


from config.logging import app_logger as logger
import uvicorn


from api.all_routers import routers
from db import close_db, init_db
from config.config import db_settings
from fastadmin import register, WidgetType, TortoiseModelAdmin, action


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
    list_display_links = "name"


# Админка для User
@register(User)
class UserAdmin(TortoiseModelAdmin):
    # exclude = {"hash_password"}
    list_display = (
        "id",
        "username",
        "email",
        "is_superuser",
        "is_active",
        "created_at",
    )
    list_display_links = ("id", "username")
    list_filter = ("id", "username")
    search_fields = ("username", "email", "first_name", "last_name")

    formfield_overrides = {  # noqa: RUF012
        "hash_password": (WidgetType.PasswordInput, {"passwordModalForm": False}),
    }

    async def authenticate(
        self, username: str, password: str
    ) -> uuid.UUID | int | None:
        user = await self.model_cls.filter(username=username, is_superuser=True).first()
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

    @action(description="Deactivate")
    async def deactivate(self, ids: list[int]) -> None:
        await self.model_cls.filter(id__in=ids).update(is_active=False)


# Админка для Station
@register(Station)
class StationAdmin(TortoiseModelAdmin):
    list_display = ["id", "name", "points", "time", "task"]
    list_display_links = ["id", "name"]
    search_fields = [
        "name",
    ]
    list_filter = ["points"]
    formfield_overrides = {  # noqa: RUF012
        "time": (WidgetType.TimePicker,{"required": False}),
        "image": (WidgetType.Upload, {"required": False})
    }

    async def orm_save_upload_field(self, obj: tp.Any, field: str, base64: str) -> None:
        # convert base64 to bytes, upload to s3/filestorage, get url and save or save base64 as is to db (don't recomment it)
        """
        Переопределяем метод сохранения загруженных файлов
        """
        if field != "image":
        # Для других полей используем стандартное поведение
            return await super().orm_save_upload_field(obj, field, base64)
        try:

            # Декодируем base64
            if "," in base64:
                # Убираем префикс data:image/...;base64,
                base64_data = base64.split(",")[1]
             # Преобразуем строку в байты перед декодированием
            file_data = b64encode(base64_data.encode("utf-8"))
            
            # Создаем временный UploadFile объект
            file = UploadFile(
                filename=f"{random.randint(1,100)}.jpg",
                file=io.BytesIO(file_data),
                content_type="image/jpeg"
            )
            image_path = await save_upload_media(file, upload_to="images", )

            setattr(obj, field, image_path)
            await obj.save(update_fields=(field,))

        except Exception as e:
            logger.error(f"Error saving {field} to db: {e}")
            raise HTTPException(status_code=500, detail="Error saving image")

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
        "tenth",
    ]


# Админка для PlayerTeam
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


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    try:
        await init_db()
        logger.info("создаю БД")
        if db_settings.ENVIRONMENT == "development":
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
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
    ],  # замени на список доменов, которые могут обращаться к нашему API
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=routers)


app.mount("/admin", admin_app)

path = os.path.join(os.path.dirname(__file__), "static")
os.makedirs(path, exist_ok=True)
app.mount("/static", StaticFiles(directory="app/static"), name="static")


if __name__ == "__main__":
    logger.info("Server is running....")
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
