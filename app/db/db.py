from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise
from tortoise.backends.base.config_generator import generate_config
from app.core.config import settings

# Конфигурация подключения к базе данных
DB_CONFIG = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "host": settings.DB_HOST,
                "port": settings.DB_PORT,
                "user": settings.DB_USER,
                "password": settings.DB_PASSWORD,
                "database": settings.DB_NAME,
                "minsize": 1,
                "maxsize": 10,
            }
        }
    },
    "apps": {
        "models": {
            "models": [
                "app.models.user",
                "app.models.station", 
                "app.models.station_order",
                "app.models.player_team",
                "app.models.curator",
                "app.models.task",
                # "aerich.models"  # Для миграций
            ],
            "default_connection": "default",
        }
    },
    "use_tz": False,
    "timezone": "UTC",
}

async def init_db():
    """
    Инициализация подключения к базе данных
    """
    await Tortoise.init(config=DB_CONFIG)
    
    # # Генерировать схемы автоматически (только для разработки)
    # if settings.ENVIRONMENT == "development":
    await Tortoise.generate_schemas()


async def close_db():
    """
    Закрытие подключений к базе данных
    """
    await Tortoise.close_connections()


def init_tortoisedb(app):
    """
    Инициализация Tortoise ORM для FastAPI приложения
    """
    register_tortoise(
        app,
        config=DB_CONFIG,
        generate_schemas=settings.ENVIRONMENT == "development",
        add_exception_handlers=True,
    )
