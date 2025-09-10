from fastapi import APIRouter

from app.schemas.player_team import  PlayerTeamCreate
from app.services.player_team import PlayerTeamService

router = APIRouter(tags=["playerteam"])

player_team_service = PlayerTeamService()

@router.get("/api/playerteam")
async def get_all_player_teams():
    return await player_team_service.get_all_player_teams()

@router.get("/api/playerteam/{id}")
async def get_player_team_by_id(id: int):
    return await player_team_service.get_player_team_by_id(id=id)

@router.post("/api/playerteam")
async def create_player_team(team_data:PlayerTeamCreate ):
    return await player_team_service.create_player_team(team_data=team_data.model_dump())

@router.put("/api/playerteam/{id}")
async def update_player_team(id: int,team_data:PlayerTeamCreate):
    return await player_team_service.update_player_team(id=id, team_data=team_data)

@router.delete("/api/playerteam/{id}")
async def delete_player_team(id: int):
    return await player_team_service.delete_player_team(id=id)

@router.post("/api/playerteam/{id}/add_score")
async def add_score_to_player_team(id: int, score: int):
    return await player_team_service.add_score_to_team(id=id,score_to_add=score)

@router.get("/api/playerteam/get_top_3/")
async def get_top_3_player_teams():
    return await player_team_service.get_top_3_teams()

@router.post("/api/playerteam/{id}/set_current_station")
async def set_current_station(id: int,station_number:int):
    return await player_team_service.set_current_station(id=id, station_number=station_number)


