from typing import List, Optional, Dict, Any
from app.repositories.player_team import PlayerTeamRepository

class PlayerTeamService():
    repository = PlayerTeamRepository()
    
    async def get_all_player_teams(self) -> List[Any]:
        return await self.repository.get_all()
    
    async def get_player_team_by_id(self, id: int) -> Optional[Any]:
        return await self.repository.get_by_id(id)
    
    async def create_player_team(self, team_data: Dict[str, Any]) -> Any:
        return await self.repository.create(**team_data)
    
    async def update_player_team(self, id: int, team_data: Dict[str, Any]) -> Optional[Any]:
        return await self.repository.update(id, **team_data)
    
    async def delete_player_team(self, id: int) -> bool:
        return await self.repository.delete(id=id)
    
    async def add_score_to_team(self, id: int, score_to_add: int) -> Optional[Any]:
        return await self.repository.add_score(id, score_to_add)
    
    async def get_top_3_teams(self) -> List[Any]:
        return await self.repository.get_top_3_by_score(limit=3)
    
    async def set_current_station(self, id: int, station_number: int) -> Optional[Any]:
        return await self.repository.set_current_station(id, station_number)
    
