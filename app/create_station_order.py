import asyncio

from utils.generate_password import generate_random_password
from utils.auth_utils import get_password_hash
from db import init_db, close_db
from config.logging import app_logger as logger
from models.models import StationOrder, Station, PlayerTeam


team_station_data = {
        "Веселые фермеры": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "Kikoriki": [2, 3, 4, 5, 1, 7, 8, 9, 10, 6],
        "Винкс": [3, 4, 5, 1, 2, 8, 9, 10, 6, 7],
        "Ам Нямы": [4, 5, 1, 2, 3, 9, 10, 6, 7, 8],
        "Барни": [5, 1, 2, 3, 4, 10, 6, 7, 8, 9],
        "Фанаты Райана Гослинга": [6, 8, 10, 7, 9, 1, 2, 3, 4, 5],
        "Телепузики": [7, 9, 6, 8, 10, 2, 3, 4, 5, 1],
        "Тигры в пиаре": [9, 6, 8, 10, 7, 4, 5, 1, 2, 3],
        "Смурфики": [10, 7, 9, 6, 8, 5, 1, 2, 3, 4],
        "Чёрный Альянс": [1, 4, 2, 5, 3, 6, 9, 7, 10, 8],
        "Миньоны": [2, 5, 3, 1, 4, 7, 10, 8, 6, 9],
        "Бабл-Тигры": [3, 1, 4, 2, 5, 8, 6, 9, 7, 10],
        "Чёткие бобры": [4, 2, 5, 3, 1, 9, 7, 10, 8, 6],
        "Dark web": [5, 3, 1, 4, 2, 10, 8, 6, 9, 7],
        "ПингWindowsы": [6, 10, 9, 8, 7, 1, 4, 2, 5, 3],
        "Бончоны": [7, 6, 10, 9, 8, 2, 5, 3, 1, 4],
        "Неизвестные": [8, 7, 6, 10, 9, 3, 1, 4, 2, 5],
        "ФавориТьфу": [9, 8, 7, 6, 10, 4, 2, 5, 3, 1],
        "Это сложно": [10, 9, 8, 7, 6, 5, 3, 1, 4, 2],
        "Команда": [2, 3, 4, 5, 1, 7, 8, 9, 10, 6],
        "Бесы": [3, 4, 5, 1, 2, 8, 9, 10, 6, 7],
        "ЛСШ ТИМ": [4, 5, 1, 2, 3, 9, 10, 6, 7, 8],
        "Скебобчики": [5, 1, 2, 3, 4, 10, 6, 7, 8, 9],
        "Dedы_007": [6, 8, 10, 7, 9, 1, 3, 5, 2, 4],
        "Я ГОВОРЮ МАКАН ВЫ ГОВОРИТЕ…": [7, 9, 6, 8, 10, 2, 4, 1, 3, 5],
        "догидог": [8, 10, 7, 9, 6, 3, 5, 2, 4, 1],
}

async def create_station_order():
    await init_db()
    # перед мероприятием поменять дефолтный пароль
    # hash_password = get_password_hash("admin")
    try:
        """
        СОЗДАЮ Заданные пути в мероприятии
        """
        stations_orders = await StationOrder.all()
        if stations_orders == []:
            

            for team_name, station_numbers in team_station_data.items():

                station_order_obj = await StationOrder.create(
                    first=await Station.get(id=station_numbers[0]),
                    second=await Station.get(id=station_numbers[1]),
                    third=await Station.get(id=station_numbers[2]),
                    fourth=await Station.get(id=station_numbers[3]),
                    fifth=await Station.get(id=station_numbers[4]),
                    sixth=await Station.get(id=station_numbers[5]),
                    seventh=await Station.get(id=station_numbers[6]),
                    eighth=await Station.get(id=station_numbers[7]),
                    ninth=await Station.get(id=station_numbers[8]),
                    tenth=await Station.get(id=station_numbers[9]),

                )

        
                logger.info(f"Created and linked station order for team {team_name}")

        logger.info("26 stationOrders created! if not exist")
    except:
        logger.error("db connection error")
        raise
    finally:
        await close_db()


if __name__ == "__main__":
    asyncio.run(create_station_order())
