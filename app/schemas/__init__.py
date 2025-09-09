from app.schemas.base import BaseSchema, BaseCreateSchema, BaseUpdateSchema
from app.schemas.curator import (
    CuratorBase, CuratorCreate, CuratorUpdate, 
    CuratorWithRelations
    
)
from app.schemas.player_team import (
    PlayerTeamBase, PlayerTeamCreate, PlayerTeamUpdate,
    PlayerTeamWithRelations,
    AddScoreRequest, SetStationRequest
)
from app.schemas.station import (
    StationBase, StationCreate, StationUpdate,
    StationWithRelations
)
from app.schemas.station_order import (
    StationOrderBase, StationOrderCreate, StationOrderUpdate,
    StationOrderWithRelations
)
from app.schemas.task import (
    TaskBase, TaskCreate, TaskUpdate
)

__all__ = [
    "BaseSchema", "BaseCreateSchema", "BaseUpdateSchema",
    "CuratorBase", "CuratorCreate", "CuratorUpdate", "CuratorWithRelations",
    "PlayerTeamBase", "PlayerTeamCreate", "PlayerTeamUpdate", "PlayerTeamWithRelations",
    "StationBase", "StationCreate", "StationUpdate", "StationWithRelations",
    "StationOrderBase", "StationOrderCreate", "StationOrderUpdate", "StationOrderWithRelations",
    "TaskBase", "TaskCreate", "TaskUpdate", "TaskWithRelations",
    "AddScoreRequest", "SetStationRequest"
]