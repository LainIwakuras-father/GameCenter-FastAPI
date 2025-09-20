import asyncio

from utils.auth_utils import get_password_hash
from db import init_db, close_db
from config.logging import app_logger as logger
from models.models import User


async def create_player_teams():
    await init_db()
    # перед мероприятием поменять дефолтный пароль
    hash_password = get_password_hash("admin")
    try:
        users = await User.all()
        if len(users) == 1:
            new_users = []
            """
            СОЗДАЮ ПРОФИЛИ КУРАТОРАМ 
            """
            for i in range(11):
                new_users.append(
                    User(
                        username=f"капитан{i}",
                        hash_password=hash_password,
                    )
                )
            logger.info(new_users)
            await User.bulk_create(new_users)
            logger.info("10 users of player_teams created! if not exist")

    except:
        logger.error("db connection error")
        raise
    finally:
        await close_db()


if __name__ == "__main__":
    asyncio.run(create_player_teams())
