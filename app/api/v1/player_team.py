from fastapi import APIRouter

router = APIRouter()

@router.get("/api/playerteam")
async def get_all_player_teams():
    pass

@router.get("/api/playerteam/{id}")
async def get_player_team_by_id(id: int):
    pass

@router.post("/api/playerteam")
async def create_player_team():
    pass

@router.put("/api/playerteam/{id}")
async def update_player_team(id: int):
    pass

@router.delete("/api/playerteam/{id}")
async def delete_player_team(id: int):
    pass

@router.post("/api/playerteam/{id}/add_score")
async def add_score_to_player_team(id: int):
    pass

@router.get("/api/playerteam/get_top_3/")
async def get_top_3_player_teams():
    pass

@router.post("/api/playerteam/{id}/set_current_station")
async def set_current_station(id: int):
    pass


