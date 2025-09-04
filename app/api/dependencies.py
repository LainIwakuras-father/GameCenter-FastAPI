from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.services import (
    StationService,
    PlayerTeamService,
    UserService,
    AuthService,
    CuratorService,
    TaskService,
    StationOrderService
)

# Базовая зависимость для базы данных
async def get_db_session() -> AsyncSession:
    async with get_db() as session:
        yield session

# Зависимости для сервисов
async def get_station_service(db: AsyncSession = Depends(get_db_session)) -> StationService:
    return StationService()

async def get_player_team_service(db: AsyncSession = Depends(get_db_session)) -> PlayerTeamService:
    return PlayerTeamService()

async def get_user_service(db: AsyncSession = Depends(get_db_session)) -> UserService:
    return UserService()

async def get_auth_service(db: AsyncSession = Depends(get_db_session)) -> AuthService:
    return AuthService()

async def get_curator_service(db: AsyncSession = Depends(get_db_session)) -> CuratorService:
    return CuratorService()

async def get_task_service(db: AsyncSession = Depends(get_db_session)) -> TaskService:
    return TaskService()

async def get_station_order_service(db: AsyncSession = Depends(get_db_session)) -> StationOrderService:
    return StationOrderService()

# Аннотированные типы для удобства использования
StationServiceDep = Annotated[StationService, Depends(get_station_service)]
PlayerTeamServiceDep = Annotated[PlayerTeamService, Depends(get_player_team_service)]
UserServiceDep = Annotated[UserService, Depends(get_user_service)]
AuthServiceDep = Annotated[AuthService, Depends(get_auth_service)]
CuratorServiceDep = Annotated[CuratorService, Depends(get_curator_service)]
TaskServiceDep = Annotated[TaskService, Depends(get_task_service)]
StationOrderServiceDep = Annotated[StationOrderService, Depends(get_station_order_service)]