from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager


import os

import uuid


import typing as tp

from fastapi.staticfiles import StaticFiles

from utils.random_station import shuffle_stations
from utils.exception import ImageUploadException
from utils.upload_files import convert_base64_to_file, save_upload_media
from utils.auth_utils import verify_password, get_password_hash
from models.models import Curator, PlayerTeam, Station, StationOrder, Task, User


from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastadmin import fastapi_app as admin_app


from config.logging import app_logger as logger
import uvicorn


from api.all_routers import routers
from db import close_db, init_db
from config.config import STATIC_DIR, db_settings
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
        "first_name",
        "last_name",
        "is_superuser",
        "is_active",
      
    )
    list_display_links = ("id", "username")
    list_filter = ("id", "username")
    search_fields = ("username", "email", "first_name", "last_name")

    formfield_overrides = {  # noqa: RUF012
        "hash_password": (WidgetType.PasswordInput, {"passwordModalForm": False}),
    }


    actions = [
        *TortoiseModelAdmin.actions,
        "deactivate",
        "activate",
    ]

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

    @action(description="Activate")
    async def activate(self, ids: list[int]) -> None:
        await self.model_cls.filter(id__in=ids).update(is_active=True)


# Админка для Station
@register(Station)
class StationAdmin(TortoiseModelAdmin):
    list_display = ["id", "name", "points", "time", "task", "image", "assignment"]
    list_display_links = ["id", "name"]
    search_fields = [
        "name",
    ]
    list_filter = ["points"]

    """
    ОБРАБОТКА ФОТОК ЗАГРУЖЕННЫХ ЧЕРЕЗ АДМИНКУ С СОХРАНИЕМ ОТНОСИТЕЛЬНОГО ПУТИ В БАЗУ ДАННЫХ
    """
    # formfield_overrides = {  # noqa: RUF012
    #     "time": (WidgetType.TimePicker,{"required": False}),
    #     "image": (WidgetType.Upload, {"required": False})
    # }

    # async def orm_save_upload_field(self, obj: tp.Any, field: str, base64: str) -> None:
    #     # convert base64 to bytes, upload to s3/filestorage, get url and save or save base64 as is to db (don't recomment it)
    #     """
    #     Переопределяем метод сохранения загруженных файлов
    #     """
    #     if field != "image":
    #     # Для других полей используем стандартное поведение
    #         return await super().orm_save_upload_field(obj, field, base64)
    #     try:
    #         decode_file, format_file = await convert_base64_to_file(base64)
            
    #         image_path = await save_upload_media(
    #             file=decode_file,
    #             file_format=format_file
    #         )

    #         setattr(obj, field, image_path)
    #         await obj.save(update_fields=(field,))

    #     except Exception as e:
    #         logger.error(f"Error saving {field} to db: {e}")
    #         ImageUploadException()

# Админка для StationOrder
@register(StationOrder)
class StationOrderAdmin(TortoiseModelAdmin):
    list_display = [
        "id",
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
    list_display = ["id", "team_name","start_time", "score", "current_station","stations"]
    search_fields = ["team_name"]
    list_filter = ["score", "current_station"]


    formfield_overrides = {  # noqa: RUF012
        "start_time": (WidgetType.DateTimePicker, {"required": False}),
    }


    actions =(
        *TortoiseModelAdmin.actions,
        "set_random_stations"
    )
    @action(description="определить случайные станции команде и сохранить")
    async def set_random_stations(self, ids: list[int]):
        await shuffle_stations(ids)
        # return HTTPException(
        #     status_code=200,
        #     details=details
        # )



        # """
        # Устанавливает случайный порядок станций для выбранных команд
        # """
        # # Получаем все доступные станции
        # all_stations = await Station.all()
        
        # if len(all_stations) < 10:
        #     raise ValueError("Недостаточно станций для создания маршрута. Нужно как минимум 10 станций.")
        
        # # Получаем выбранные команды
        # teams = await PlayerTeam.filter(id__in=ids).prefetch_related("stations")
        
        # for team in teams:
        #     # Выбираем 10 случайных станций и перемешиваем
        #     random_stations = random.sample(all_stations, 10)
        #     random.shuffle(random_stations)
            
        #     # Создаем новый порядок станций
        #     station_order = await StationOrder.create(
        #         first=random_stations[0],
        #         second=random_stations[1],
        #         third=random_stations[2],
        #         fourth=random_stations[3],
        #         fifth=random_stations[4],
        #         sixth=random_stations[5],
        #         seventh=random_stations[6],
        #         eighth=random_stations[7],
        #         ninth=random_stations[8],
        #         tenth=random_stations[9],
        #     )
            
        #     # Обновляем команду
        #     team.stations = station_order
        #     team.current_station = random_stations[0]  # Устанавливаем первую станцию как текущую
            
        #     # Сбрасываем прогресс команды
        #     team.score = 0
        #     team.start_time = datetime.now()  # Если у вас есть поле для времени начала
            
        #     await team.save()
        
        # return f"Случайные станции установлены для {len(teams)} команд"







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
        #эту часть кода переместить в db.py
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
        "http://app:80",
        "http://xn--80afhj2apdp7a.xn--p1ai:3000",
        "http://app:8000",
        "http://играцентр.рф:3000",
        "http://играцентр.рф:8000",
        "http://api.играцентр.рф:3000",
        "http://api.играцентр.рф:8000",
    ],  # замени на список доменов, которые могут обращаться к нашему API
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=routers)


app.mount("/admin", admin_app)


os.makedirs(STATIC_DIR, exist_ok=True)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


if __name__ == "__main__":
    logger.info("Server is running....")
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
