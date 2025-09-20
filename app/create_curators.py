import asyncio

from utils.generate_password import generate_random_password
from utils.auth_utils import get_password_hash
from db import init_db, close_db
from config.logging import app_logger as logger
from models.models import User, Curator, Station





async def create_users():
    await init_db()
    # перед мероприятием поменять дефолтный пароль
    # hash_password = get_password_hash("admin")
    try:
        users = await User.all()
        if len(users) == 1:
            new_users = []
            new_password = []
            stations= await Station.all()
            """
            СОЗДАЮ ПРОФИЛИ Пользователей
            """
            for i, station in enumerate(stations, 1):
                password = await generate_random_password()
                new_password.append(password)
                user = User(
                        username=f"куратор{i}",
                        hash_password=get_password_hash(password),
                    )
                new_users.append(user)
                logger.info(f"Useraname:куратор{i}, password:{password} ")
                await user.save()

                """
                из пользователей делают кураторов
                """
                curator=Curator(
                        user=user,
                        name=f"Куратор {i}",
                    )
                await curator.save()

            logger.info("10 curators created! if not exist")
    except:
        logger.error("db connection error")
        raise
    finally:
        await close_db()


if __name__ == "__main__":
    asyncio.run(create_users())
