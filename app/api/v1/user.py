from fastapi import APIRouter, Depends

from utils.dependencies import get_user_role


router = APIRouter(tags=["user"])


@router.get("/api/user/get_user")
async def get_me(me = Depends(get_user_role)):
    return me
