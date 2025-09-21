import asyncio


from utils.generate_password import generate_random_password
from utils.auth_utils import get_password_hash
from db import init_db, close_db
from config.logging import app_logger as logger
from models.models import StationOrder, User, PlayerTeam

teams_list = [
    {"name": "Веселые фермеры"},
    {"name": "Kikoriki"},
    {"name": "Винкс"},
    {"name": "Ам Нямы"},
    {"name": "Барни"},
    {"name": "Фанаты Райана Гослинга"},
    {"name": "Телепузики"},
    {"name": "Тигры в пиаре"},
    {"name": "Смурфики"},
    {"name": "Чёрный Альянс"},
    {"name": "Миньоны"},
    {"name": "Бабл-Тигры"},
    {"name": "Чёткие бобры"},
    {"name": "Dark web"},
    {"name": "ПингWindowsы"},
    {"name": "Бончоны"},
    {"name": "Неизвестные"},
    {"name": "ФавориТьфу"},
    {"name": "Это сложно"},
    {"name": "Команда"},
    {"name": "Бесы"},
    {"name": "ЛСШ ТИМ"},
    {"name": "Скебобчики"},
    {"name": "Dedы_007"},
    {"name": "Я ГОВОРЮ МАКАН ВЫ ГОВОРИТЕ…"},
    {"name": "догидог"}
]



async def create_player_teams():
    await init_db()
    # перед мероприятием поменять дефолтный пароль
    # hash_password = get_password_hash("admin")
    try:
        users = await User.all()
        orders = StationOrder.all()
        if len(users) == 11:
            new_users = []
            new_password = []
            """
            СОЗДАЮ ПРОФИЛИ КАПИТАНАМ
            """
            for i,teamname in enumerate(teams_list,1):
                
                password = await generate_random_password()
                new_password.append(password)
                user = User(
                        username=f"капитан{i}",
                        hash_password=get_password_hash(password),
                )
                
                logger.info(f"Username:капитан{i}, password:{password}")
                await user.save()


                """
                из пользователей делаю капитанов
                            
                """
                
                
                player= PlayerTeam(
                      user=user,
                      team_name=teamname["name"],
                      stations=await StationOrder.get(id=i)
                )
                await player.save()
        logger.info("10 player teams created! if not exist")
    except:
        logger.error("db connection error")
        raise
    finally:
        await close_db()



        


if __name__ == "__main__":
    asyncio.run(create_player_teams())
