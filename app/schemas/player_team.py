# PlayerTeam schemas
from datetime import datetime
from typing import Optional

from schemas.base import BaseSchema


class StationOrderNested(BaseSchema):
    id: int


class StationNested(BaseSchema):
    id: int


class ScoreAdd(BaseSchema):
    score: int


class ScoreResponse(BaseSchema):
    score: int
    current_station: int


class CurrentStation(BaseSchema):
    current_station: int


class CurrentStationResponse(BaseSchema):
    current_station: str


class PlayerTeam(BaseSchema):
    id: Optional[int] = None
    teamname: Optional[str] = None
    start_time: Optional[datetime] = None
    score: Optional[int] = 0
    user: int
    stations: Optional[StationOrderNested] = None
    current_station: Optional[StationNested] = None


class PlayerTeamCreate(PlayerTeam):
    pass


class PlayerTeamUpdate(PlayerTeam):
    pass


class PlayerTeamWithRelations(PlayerTeam):
    id: int
    user: Optional[StationNested] = None
    stations: Optional[StationOrderNested] = None
