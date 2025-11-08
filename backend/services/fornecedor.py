from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from backend.domain.fornecedor.models import Fornecedor
from backend.api.schemas.fornecedor import (
    CriaFornecedor,
    AtualizaFornecedor,
    FornecedorResponse,
    FornecedorListResponse
    )
from backend.exceptions import (
    FornecedorNotFoundError, 
    FornecedorValidationError, 
    FornecedorIntegrityError,
    FornecedorDatabaseError)    


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
        raise FornecedorIntegrityError(f"Erro de integridade ao criar fornecedor: {str(e)}")
    except Exception as e:
        db.rollback()
        raise FornecedorDatabaseError(f"Erro inesperado ao criar fornecedor: {str(e)}")

def lista_fornecedores(db: Session, pagina: int = 1, tamanho_pagina: int = 10) -> FornecedorListResponse:
    """Lista fornecedores com paginação"""
    if pagina < 1:
        raise FornecedorValidationError("Página deve ser maior ou igual a 1")
    if tamanho_pagina < 1:
        raise FornecedorValidationError("Tamanho da página deve ser maior ou igual a 1")
    if tamanho_pagina > 100:
        raise FornecedorValidationError("Tamanho da página deve ser menor ou igual a 100")

    try:
        #Query para buscar fornecedores com paginação
        query = db.query(Fornecedor)

        total = query.count()

        fornecedores = (
            query.order_by(Fornecedor.id.desc())
            .offset((pagina - 1) * tamanho_pagina)
            .limit(tamanho_pagina)
            .all()
        )

        total_paginas = (total + tamanho_pagina - 1) // tamanho_pagina

        fornecedores_response = [
            FornecedorResponse.model_validate(fornecedor) for fornecedor in fornecedores
        ]

        return FornecedorListResponse(
            fornecedores=fornecedores_response,
            total=total,
            pagina=pagina,
            tamanho_pagina=tamanho_pagina,
            total_paginas=total_paginas,
            fornecedores_por_pagina=len(fornecedores_response)
        )
    except Exception as e:
        raise FornecedorDatabaseError(f"Erro ao listar fornecedores: {str(e)}")


def busca_fornecedor_por_id(id: int, db: Session) -> FornecedorResponse:
    """Busca um fornecedor por ID"""
    try:
        fornecedor = db.query(Fornecedor).filter(Fornecedor.id == id).first()
        if not fornecedor:
            raise FornecedorNotFoundError("Fornecedor não encontrado")
        return FornecedorResponse.model_validate(fornecedor)
    except FornecedorNotFoundError:
        raise
    except Exception as e:
        raise FornecedorDatabaseError(f"Erro ao buscar fornecedor por ID: {str(e)}")

def atualiza_fornecedor(id: int, fornecedor_data: AtualizaFornecedor, db: Session) -> FornecedorResponse:
    """Atualiza um fornecedor(apenas os campos que são passados)"""
    try:
        fornecedor = db.query(Fornecedor).filter(Fornecedor.id == id).first()
        if not fornecedor:
            raise FornecedorNotFoundError("Fornecedor não encontrado")
        
        update_data = fornecedor_data.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            if value is not None: #Opcional, para evitar atualizações de campos que não foram passados
                setattr(fornecedor, field, value)
        
        db.commit()
        db.refresh(fornecedor)
        return FornecedorResponse.model_validate(fornecedor)
    
    except FornecedorNotFoundError:
        db.rollback()
        raise
    except IntegrityError as e:
        db.rollback()
        raise FornecedorIntegrityError(f"Erro de integridade ao atualizar fornecedor: {str(e)}")
    except Exception as e:
        db.rollback()
        raise FornecedorDatabaseError(f"Erro inesperado ao atualizar fornecedor: {str(e)}")


def deleta_fornecedor(id: int, db: Session) -> None:
    """Deleta um fornecedor"""
    try:
        fornecedor = db.query(Fornecedor).filter(Fornecedor.id == id).first()
        if not fornecedor:
            raise FornecedorNotFoundError("Fornecedor não encontrado")
        db.delete(fornecedor)
        db.commit()
    except FornecedorNotFoundError:
        db.rollback()
        raise
    except IntegrityError as e:
        db.rollback()
        raise FornecedorIntegrityError(
            f"Erro de integridade ao deletar fornecedor: {str(e)}"
            )
    except Exception as e:
        db.rollback()
        raise FornecedorDatabaseError(
            f"Erro inesperado ao deletar fornecedor: {str(e)}"
            )