from typing import List
from fastapi import APIRouter, Depends

from utils.dependencies import IsAuthenticated
from schemas.player_team import (
    CurrentStation,
    CurrentStationResponse,
    PlayerTeam,
    PlayerTeamCreate,
    ScoreAdd,
    ScoreResponse,
)
from services.player_team import PlayerTeamService

router = APIRouter(
    tags=["playerteam"], dependencies=[Depends(IsAuthenticated)]
)

player_team_service = PlayerTeamService()


@router.get("/api/playerteam")
async def get_all_player_teams():
    return await player_team_service.get_all_player_teams()


@router.get("/api/playerteam/{id}")
async def get_player_team_by_id(id: int):
    return await player_team_service.get_player_team_by_id(id=id)


# ручка создает Команду и рандомные станции для нее
@router.post("/api/playerteam")
async def create_player_team(team_data: PlayerTeamCreate):
    return await player_team_service.create_player_team(
        team_data=team_data.model_dump()
    )


@router.put("/api/playerteam/{id}")
async def update_player_team(id: int, team_data: PlayerTeamCreate):
    return await player_team_service.update_player_team(
        id=id, team_data=team_data.model_dump()
    )


@router.delete("/api/playerteam/{id}")
async def delete_player_team(id: int):
    return await player_team_service.delete_player_team(id=id)


@router.post("/api/playerteam/{id}/add_score", response_model=ScoreResponse)
async def add_score_to_player_team(id: int, score: ScoreAdd):
    score_add, current_station = await player_team_service.add_score_to_team(
        id=id, score_to_add=score.model_dump()["score"]
    )
    return ScoreResponse(score=score_add, current_station=current_station)


@router.get("/api/playerteam/get_top_3/", response_model=List[PlayerTeam])
async def get_top_3_player_teams():
    return await player_team_service.get_top_3_teams()


@router.post(
    "/api/playerteam/{id}/set_current_station",
    response_model=CurrentStationResponse,
)
async def set_current_station(id: int, station_number: CurrentStation):
    current_station = await player_team_service.set_current_station(
        id=id, station_number=station_number
    )
    return CurrentStationResponse(current_station=current_station)
