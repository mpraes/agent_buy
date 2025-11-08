from pydantic_settings import BaseSettings  # pyright: ignore[reportMissingImports]
from pydantic import Field
from dotenv import load_dotenv
from functools import lru_cache

load_dotenv()

class Settings(BaseSettings):
    """Configurações da aplicação"""
    database_url: str = Field(..., env="DATABASE_URL") 
    app_name: str = Field(..., env="APP_NAME")
    app_env: str = Field(..., env="APP_ENV")

    @property
    def db_schema(self) -> str:
        """Retorna o schema do banco baseado no ambiente"""
        return "dev" if self.app_env.lower() == "development" else "prd"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False

@lru_cache()
def get_settings() -> Settings:
    """Retorna Configurações da aplicação"""
    return Settings()