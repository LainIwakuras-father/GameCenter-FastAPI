# Curator schemas
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