from datetime import datetime
from enum import Enum as PyEnum
from sqlalchemy import Column, Integer, String, DateTime, Text, Enum, func, UniqueConstraint
from backend.config import get_settings
from backend.core.database import Base

class StatusFornecedor(str, PyEnum):
    """Enum para o status do fornecedor"""
    ATIVO = "ativo"
    INATIVO = "inativo"

class Fornecedor(Base):
    """Modelo de fornecedor"""
    __tablename__ = 'fornecedor'
    @classmethod
    def __table_args__(cls):
        settings = get_settings()
        return (UniqueConstraint('cnpj', name='uq_fornecedor_cnpj'),
        {"schema": get_settings().db_schema})

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome_razao = Column(String(100), nullable=False)
    email_contato = Column(String(255), nullable=True)
    telefone = Column(String(11), nullable=True)
    endereco = Column(String(100), nullable=True)
    cidade = Column(String(100), nullable=True)
    estado = Column(String(2), nullable=True)
    cep = Column(String(8), nullable=True)
    pais = Column(String(100), nullable=True)
    cnpj = Column(String(14), nullable=False, unique=True)
    inscricao_estadual = Column(String(12), nullable=True)
    inscricao_municipal = Column(String(12), nullable=True)
    site = Column(String(255), nullable=True)
    observacoes = Column(Text, nullable=True)
    status = Column(Enum(StatusFornecedor), nullable=False, default=StatusFornecedor.ATIVO)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())