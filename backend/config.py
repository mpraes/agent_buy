from pydantic_settings import BaseSettings  # pyright: ignore[reportMissingImports]
from pydantic import Field
from dotenv import load_dotenv
from functools import lru_cache

class Settings(BaseSettings):
    """Configurações da aplicação"""

    database_url: str = Field(..., env="DATABASE_URL")
    
    app_name: str = Field(..., env="APP_NAME")
    app_env: str = Field(..., env="APP_ENV")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False

@lru_cache()
def get_settings() -> Settings:
    """Retorna Configurações da aplicação"""
    return Settings()