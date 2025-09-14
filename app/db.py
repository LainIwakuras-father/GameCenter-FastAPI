from tortoise import Tortoise
from config.config import db_settings as settings

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
                "models.models",
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
    if settings.ENVIRONMENT == "development":
        await Tortoise.generate_schemas()


async def close_db():
    """
    Закрытие подключений к базе данных
    """
    await Tortoise.close_connections()
