# Curator schemas
from typing import Optional
from pydantic import BaseModel, ConfigDict

from schemas.base import BaseSchema



class CuratorBase(BaseSchema):
    name: Optional[str] = None
    station_id: Optional[int] = None
    user_id: int
    
class CuratorCreate(CuratorBase):
    pass

class CuratorUpdate(CuratorBase):
    pass

class UserNested(BaseSchema):
    id: int
    username: str
    email: Optional[str] = None

class StationNested(BaseSchema):
    id: int
    name: str
    description: Optional[str] = None

class CuratorWithRelations(CuratorBase):
    id: int
    user: Optional[UserNested] = None
    station: Optional[StationNested] = None