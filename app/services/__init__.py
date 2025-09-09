from app.services.curator import CuratorService

from app.services.player_team import PlayerTeamService
from app.services.station import StationService
from app.services.station_order import StationOrderService
from app.services.task import TaskService

# Создаем экземпляры сервисов
curator_service = CuratorService()
player_team_service = PlayerTeamService()
station_service = StationService()
station_order_service = StationOrderService()
task_service = TaskService()

__all__ = [
    "CuratorService",
    "PlayerTeamService",
    "StationService",
    "StationOrderService",
    "TaskService",
    "curator_service",
    "player_team_service",
    "station_service",
    "station_order_service",
    "task_service",
]