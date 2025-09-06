# Curator schemas
from typing import Optional
from pydantic import BaseModel, ConfigDict

from app.schemas.user import User




class CuratorBase(BaseModel):
    station_id: Optional[int] = None
    name: Optional[str] = None

class CuratorCreate(CuratorBase):
    user_id: int

class Curator(CuratorBase):
    id: int
    user_id: int
    model_config = ConfigDict(from_attributes=True)


class CuratorWithUser(Curator):
    user: User