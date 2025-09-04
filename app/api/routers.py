from fastapi import APIRouter



routers = APIRouter()

all_routers = [
    
]

for router in all_routers:
    routers.include_router(router)