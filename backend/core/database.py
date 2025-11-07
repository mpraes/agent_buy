from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from typing import Generator
from backend.config import get_settings

settings = get_settings()

# Conexão com o banco de dados
engine = create_engine(settings.database_url, echo=True)

# Base para modelos SQLAlchemy
Base = declarative_base()

# SessionLocal para criar sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator[Session, None, None]:
    """
    Dependency para FastAPI que fornece uma sessão do banco de dados.
    Garante que a sessão seja fechada após o uso.
    """
    db = SessionLocal()
    try:
        # Configura o schema padrão para a sessão
        db.execute(text(f"SET search_path TO {settings.db_schema}, public"))
        yield db
    finally:
        db.close()


def init_db() -> None:
    """
    Inicializa o banco de dados criando todas as tabelas definidas nos modelos.
    """
    # Importa os modelos para que sejam registrados no Base
    from backend.domain.fornecedor.models import Fornecedor  # noqa: F401
    
    # Cria todas as tabelas
    Base.metadata.create_all(bind=engine)