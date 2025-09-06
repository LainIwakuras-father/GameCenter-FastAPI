from app.api.v1 import (
    auth,
    curator,
    task,
    player_team,
    station,
    station_order
    )


from fastapi import APIRouter



routers = APIRouter()

all_routers = [
    auth.router,
    task.router,
    curator.router,
    player_team.router,
    station.router,
    station_order.router
]

for router in all_routers:
    routers.include_router(router)