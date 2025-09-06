# PlayerTeam schemas
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict

from app.schemas.user import User


class PlayerTeamBase(BaseModel):
    teamname: Optional[str] = None
    start_time: Optional[datetime] = None
    score: Optional[int] = 0
    stations_id: Optional[int] = None
    current_station: int = 1

class PlayerTeamCreate(PlayerTeamBase):
    user_id: int

class PlayerTeam(PlayerTeamBase):
    id: int
    user_id: int
    model_config = ConfigDict(from_attributes=True)


class PlayerTeamWithUser(PlayerTeam):
    user: User