import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # DB_PORT: int
    # DB_NAME: str
    # DB_USER: str
    # DB_PASSWORD: str
    # DB_HOST: str
    SECRET_KEY: str
    ALGORITHM: str

    @property
    def DB_URL(self)->str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    class Config:
        env_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env")

settings = Settings()

def get_auth_data():
    return {"secret_key": settings.SECRET_KEY, "algorithm": settings.ALGORITHM}