import os
from dotenv import load_dotenv
from pathlib import Path
from fastadmin.settings import Settings as AdminSettings

BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_PATH = BASE_DIR / ".env"
# UPLOAD_FOLDER = Path(f"uploads/images")
# UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)
# Загружаем переменные окружения


load_dotenv(ENV_PATH)


class DBSettings:
    DB_PORT: int = int(os.getenv("DB_PORT", 5432))
    DB_NAME: str = os.getenv("DB_NAME")
    DB_USER: str = os.getenv("DB_USER", "postgres")
    DB_PASSWORD: str = os.getenv("DB_PASS")
    DB_HOST: str = os.getenv("DB_HOST")

    # REDIS_HOST: str = os.getenv("REDIS_HOST", "localhost")
    # REDIS_PORT: str = os.getenv("REDIS_PORT", "6379")

    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")

    # @property
    # def REDIS_URL(self) -> str:
    #     return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}"

    @property
    def DB_URL(self) -> str:
        if self.ENVIRONMENT == "development":
            return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        else:
            return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@db:{self.DB_PORT}/{self.DB_NAME}"


class AUTH_Settings:
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 15))
    REFRESH_TOKEN_EXPIRE_MINUTES: int = int(
        os.getenv("REFRESH_TOKEN_EXPIRE_MINUTES", 1)
    )

    @property
    def get_auth_data(self) -> dict:
        return {
            "secret_key": self.SECRET_KEY,
            "algorithm": self.ALGORITHM,
            "expire_minutes": self.ACCESS_TOKEN_EXPIRE_MINUTES,
        }


class ADMIN_Settings(AdminSettings):
    # class ADMIN_Settings:
    ADMIN_USER_MODEL: str = os.getenv("ADMIN_USER_MODEL", "User")
    ADMIN_USER_MODEL_USERNAME_FIELD: str = os.getenv("ADMIN_USER_MODEL_USERNAME_FIELD")
    ADMIN_SECRET_KEY: str = os.getenv("ADMIN_SECRET_KEY")


db_settings = DBSettings()
auth_settings = AUTH_Settings()
admin_settings = ADMIN_Settings()
