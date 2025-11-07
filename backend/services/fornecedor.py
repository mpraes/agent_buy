from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import Optional, Tuple
from backend.domain.fornecedor.models import Fornecedor
from backend.api.schemas.fornecedor import (
    CriaFornecedor,
    AtualizaFornecedor,
    FornecedorResponse,
    FornecedorListResponse
)

def cria_fornecedor(fornecedor_data: CriaFornecedor, db: Session) -> FornecedorResponse:
    """Cria um novo fornecedor"""
    try:
        novo_fornecedor = Fornecedor(**fornecedor_data.model_dump())

        db.add(novo_fornecedor)
        db.commit()
        db.refresh(novo_fornecedor)
        return FornecedorResponse.model_validate(novo_fornecedor)
    except IntegrityError as e:
        db.rollback()
        raise ValueError(f"Erro ao criar fornecedor: {str(e)}")

def lista_fornecedores(db: Session, pagina: int = 1, tamanho_pagina: int = 10) -> FornecedorListResponse: