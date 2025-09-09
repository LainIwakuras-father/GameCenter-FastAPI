# PlayerTeam schemas
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict

from app.schemas.base import BaseSchema


class PlayerTeamBase(BaseModel):
    teamname: Optional[str] = None
    start_time: Optional[datetime] = None
    score: Optional[int] = 0
    stations_id: Optional[int] = None
    current_station: int = 1
    user_id: int

class PlayerTeamCreate(PlayerTeamBase):
    pass

class PlayerTeamUpdate(PlayerTeamBase):
   pass


class UserNested(BaseSchema):
    id: int
    username: str

class StationOrderNested(BaseSchema):
    id: int

class PlayerTeamWithRelations(PlayerTeamBase):
    id: int
    user: Optional[UserNested] = None
    stations: Optional[StationOrderNested] = None

# Схемы для специальных операций
class AddScoreRequest(BaseModel):
    score_to_add: int

class SetStationRequest(BaseModel):
    station_number: int