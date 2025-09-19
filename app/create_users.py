import asyncio

from utils.auth_utils import get_password_hash
from db import init_db, close_db
from config.logging import app_logger as logger
from models.models import User



 # Список всех кураторов из таблицы
curators = [
                # пл. Искусств
                {"last_name": "Жук", "first_name": "Арина",},
                {"last_name": "Кузнецов", "first_name": "Максим"},
                {"last_name": "Гадаборшева", "first_name": "Маликат"},
                {"last_name": "Мампеева", "first_name": "Алина"},
                
                # Спас на Крови
                {"last_name": "Угрюмов", "first_name": "Иван"},
                {"last_name": "Гулевич", "first_name": "Алина"},
                {"last_name": "Савельев", "first_name": "Александр"},
                {"last_name": "Красковская", "first_name": "Фаина"  },           
                # Екатерининский сквер
                {"last_name": "Левицкий", "first_name": "Владимир" },
                {"last_name": "Буслаева", "first_name": "Татьяна" },
                {"last_name": "Кулдашева", "first_name": "Виктория" },
                {"last_name": "Леонов", "first_name": "Леон"},
                
                # Казанский собор
                {"last_name": "Гадалин", "first_name": "Илья"},
                {"last_name": "Бытенская", "first_name": "Элина"},
                {"last_name": "Ганин", "first_name": "Денис"},
                {"last_name": "Володин", "first_name": "Никита",},
                
                # Б. Конюшенная
                {"last_name": "Михайлова", "first_name": "Дарья"},
                {"last_name": "Фахридинов", "first_name": "Азим"},
                {"last_name": "Суворова", "first_name": "Яна"},
                {"last_name": "Лапин", "first_name": "Егор"},
                
                # Исаакиевский сквер
                {"last_name": "Пустовойт", "first_name": "Мария" },
                {"last_name": "Турчина", "first_name": "Татьяна"},
                {"last_name": "Лапшина", "first_name": "Елизавета"},
                {"last_name": "Тахарова", "first_name": "Юмжана"},
                
                # Адмиралтейство
                {"last_name": "Галеев", "first_name": "Данил" },
                {"last_name": "Николаев", "first_name": "Владислав" },
                {"last_name": "Яченко", "first_name": "Денис"},
                {"last_name": "Гусаков", "first_name": "Виктор"},
                
                # РГПУ им. А.И.Герцена
                {"last_name": "Болтнев", "first_name": "Егор"},
                {"last_name": "Орлова", "first_name": "Юлия" },
                {"last_name": "Имакаева", "first_name": "Элина"},
                {"last_name": "Масюткин", "first_name": "Николай" },
                
                # Дворцовая площадь
                {"last_name": "Кузнецов", "first_name": "Игорь" },
                {"last_name": "Иванова", "first_name": "Елена" },
                {"last_name": "Куклева", "first_name": "Кристина" },
                {"last_name": "Михайлова", "first_name": "Мария" },
                
                # Медный всадник
                {"last_name": "Гарипов", "first_name": "Тимур" },
                {"last_name": "Хмелинин", "first_name": "Кирилл" },
                {"last_name": "Разин", "first_name": "Матвей"},
                {"last_name": "Леонидова", "first_name": "Рената"},
            ]







async def create_users():
    await init_db()
    #перед мероприятием поменять дефолтный пароль
    hash_password = get_password_hash("admin")
    try:
        users = await User.all()
        if len(users) == 1:
            new_users = []
            """
            СОЗДАЮ ПРОФИЛИ КУРАТОРАМ 
            """
            for i, curator in enumerate(curators,1):
                new_users.append(User(
                    username=f"куратор{i}",
                    hash_password=hash_password,
                    first_name=curator['first_name'],
                    last_name=curator['last_name'],
                ))
            logger.info(new_users)
            await User.bulk_create(new_users)
            logger.info("40 users created! if not exist")

    except:
        logger.error("db connection error")
        raise
    finally:
        await close_db()


if __name__ == "__main__":
    asyncio.run(create_users())
