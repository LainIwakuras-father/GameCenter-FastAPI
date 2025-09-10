from typing import List, Optional, Dict, Any
from app.models.player_team import PlayerTeam
from app.models.user import User
from app.repositories.base import BaseRepository

class PlayerTeamRepository(BaseRepository):
    def __init__(self):
        super().__init__(PlayerTeam)


    async def get_all_with_user_station(self) -> List[PlayerTeam]:
        return await PlayerTeam.all().prefetch_related("user").all()

    async def get_by_id_with_user_station(self, id: int) -> Optional[PlayerTeam]:
        return await PlayerTeam.filter(id=id).prefetch_related("user").first()

    async def add_score(self, id: int, score_to_add: int) -> Optional[PlayerTeam]:
        return await self.update(id, {"score": PlayerTeam.score + score_to_add})

    async def get_top_3_by_score(self) -> List[PlayerTeam]:
        return await PlayerTeam.all().order_by("-score").limit(3).prefetch_related("user").all()

    async def set_current_station(self, id: int, station_number: int) -> Optional[PlayerTeam]:
        return await self.update(id, {"current_station": station_number})