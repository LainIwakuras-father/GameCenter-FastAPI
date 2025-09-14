from typing import List, Optional
from models.models import PlayerTeam
from models.models import User
from repositories.base import BaseRepository

class PlayerTeamRepository(BaseRepository):
    def __init__(self):
        super().__init__(PlayerTeam)


    async def get_all_with_user_station(self) -> List[PlayerTeam]:
        return await PlayerTeam.all().prefetch_related("user").all()

    async def get_by_id_with_user_station(self, id: int) -> Optional[PlayerTeam]:
        return await PlayerTeam.filter(id=id).prefetch_related("user").first()

    async def add_score(self, id: int, score_to_add: int) -> Optional[PlayerTeam]:
        instance = await self.model.get_or_none(id=id)
        if instance:
            score = instance.score 
            await instance.update_from_dict({"score":score + score_to_add}).save()
            return instance
        return None

    async def get_top_3_by_score(self) -> List[PlayerTeam]:
        return await PlayerTeam.all().order_by("-score").limit(3).prefetch_related("user")

    async def set_current_station(self, id: int, station_number: int) -> Optional[PlayerTeam]:
        return await self.update(id, {"current_station": station_number})