from datetime import datetime
import random
from typing import List

from app.models.models import PlayerTeam, Station, StationOrder


async def shuffle_stations(ids: List[int]) -> str:
    """
    Устанавливает случайный порядок станций для выбранных команд
    """
    # Получаем все доступные станции
    all_stations = await Station.all()

    if len(all_stations) < 10:
        raise ValueError(
            "Недостаточно станций для создания маршрута. Нужно как минимум 10 станций."
        )

    # Получаем выбранные команды
    teams = await PlayerTeam.filter(id__in=ids).prefetch_related("stations")

    for team in teams:
        # Выбираем 10 случайных станций и перемешиваем
        random_stations = random.sample(all_stations, 10)
        random.shuffle(random_stations)

        # Создаем новый порядок станций
        station_order = await StationOrder.create(
            first=random_stations[0],
            second=random_stations[1],
            third=random_stations[2],
            fourth=random_stations[3],
            fifth=random_stations[4],
            sixth=random_stations[5],
            seventh=random_stations[6],
            eighth=random_stations[7],
            ninth=random_stations[8],
            tenth=random_stations[9],
        )

        # Обновляем команду
        team.stations = station_order
        team.current_station = random_stations[
            0
        ]  # Устанавливаем первую станцию как текущую

        # Сбрасываем прогресс команды
        team.score = 0
        team.start_time = (
            datetime.now()
        )  # Если у вас есть поле для времени начала

        await team.save()

    return f"Случайные станции установлены для {len(teams)} команд"
