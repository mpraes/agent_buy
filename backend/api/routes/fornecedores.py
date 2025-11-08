from backend.api.schemas.fornecedor import FornecedorResponse
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.services.fornecedor import cria_fornecedor
from backend.api.schemas.fornecedor import CriaFornecedor, FornecedorResponse
from backend.exceptions import (
    FornecedorIntegrityError,
    FornecedorDatabaseError
)

router = APIRouter(
    prefix='/fornecedores',
    tags=['fornecedores']
)

@router.post('/', response_model=FornecedorResponse, status_code=status.HTTP_201_CREATED)
def criar_fornecedor(
    fornecedor_data: CriaFornecedor,
    db: Session = Depends(get_db)
) -> FornecedorResponse:
    try:
        return cria_fornecedor(fornecedor_data, db)
    except FornecedorIntegrityError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except FornecedorDatabaseError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))