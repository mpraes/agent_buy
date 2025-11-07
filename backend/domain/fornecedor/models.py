from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Enum, UniqueConstraint

from backend.core.database import Base

from enum import Enum as PyEnum

class StatusFornecedor(PyEnum):
    ATIVO = "ativo"
    INATIVO = "inativo"


class Fornecedor(Base):