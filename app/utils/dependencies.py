from fastapi import Depends, HTTPException,status
from fastapi.security import OAuth2PasswordBearer

from models.curator import Curator
from models.player_team import PlayerTeam
from models.user import User
from utils.auth_utils import decoded_token
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/token")
security = HTTPBearer()


async def get_current_auth_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
)-> User:
    try:
        payload = decoded_token(credentials.credentials)
        user_id = int(payload.get("user_id")) 
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Не найден ID пользователя в токене"
            )
        
        user = await User.get_or_none(id=user_id)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Пользователь не найден"
            )
        return user
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Ошибка аутентификации"
        )
    

async def get_user_role(user: User = Depends(get_current_user)):
    # Проверяем, является ли пользователь куратором
    curator = await Curator.get_or_none(user=user)
    if curator:
        return {"is_curator": True, "is_player": False}
    
    # Проверяем, является ли пользователь игроком
    player = await PlayerTeam.get_or_none(user=user)
    if player:
        return {"is_curator": False, "is_player": True}
    
    # Если не нашли ни одну роль
    return {"is_curator": False, "is_player": False}