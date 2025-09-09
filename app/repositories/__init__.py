from .curator import CuratorRepository
from .player_team import PlayerTeamRepository
from .station import StationRepository
from .station_order import StationOrderRepository
from .task import TaskRepository

# Создаем экземпляры репозиториев
curator_repository = CuratorRepository()
player_team_repository = PlayerTeamRepository()
station_repository = StationRepository()
station_order_repository = StationOrderRepository()
task_repository = TaskRepository()

__all__ = [
    "CuratorRepository",
    "PlayerTeamRepository",
    "StationRepository",
    "StationOrderRepository",
    "TaskRepository",
    "curator_repository",
    "player_team_repository",
    "station_repository",
    "station_order_repository",
    "task_repository",
]