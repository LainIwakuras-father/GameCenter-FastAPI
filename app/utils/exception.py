from functools import wraps
from loguru import logger
from fastapi import HTTPException, status


def handle_http_exceptions(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except HTTPException as e:
            logger.error(f"Exception: {e}")
            raise e
        except Exception as e:
            logger.error(f"Exception: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Произошла непредвиденная ошибка: {e}",
            )

    return wrapper


class TokenExpiredException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Токен истек"
        )


class TokenNoFoundException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Токен не найден"
        )


class AccessTokenRequired(HTTPException):
    """User has provided a refresh token when an access token is needed"""

    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User has provided a refresh token when an access token is needed",
        )


class RefreshTokenRequired(HTTPException):
    """User has provided an access token when a refresh token is needed"""

    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User has provided an access token when a refresh token is needed",
        )


ImageUploadException = HTTPException(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    detail="Ошибка загрузки изображения",
)


UserAlreadyExistsException = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="Пользователь уже существует"
)

PasswordMismatchException = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="Пароли не совпадают!"
)

IncorrectEmailOrPasswordException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Неверная почта или пароль",
)

NoJwtException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED, detail="Токен не валидный!"
)

NoUserIdException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Не найден ID пользователя",
)

ForbiddenException = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN, detail="Недостаточно прав!"
)
