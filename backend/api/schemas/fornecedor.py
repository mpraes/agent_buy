from pydantic import BaseModel, Field, EmailStr, ConfigDict
from datetime import datetime
from typing import Optional, List, Literal
#Schema para criação de fornecedor
class CriaFornecedor(BaseModel):
    nome_razao: str = Field(..., min_length=3, max_length=100, description="Nome do fornecedor")
    email_contato: Optional[EmailStr] = Field(default=None, format="email", description="Email do fornecedor")
    telefone: Optional[str] = Field(default=None, pattern=r"^\d{11}$", description="Telefone do fornecedor")
    endereco: Optional[str] = Field(default=None, min_length=3, max_length=100, description="Endereço do fornecedor")
    cidade: Optional[str] = Field(default=None, min_length=3, max_length=100, description="Cidade do fornecedor")
    estado: Optional[str] = Field(default=None, min_length=2, max_length=2, description="Estado do fornecedor")
    cep: Optional[str] = Field(default=None, pattern=r"^\d{8}$", description="CEP do fornecedor")
    pais: Optional[str] = Field(default=None, min_length=3, max_length=100, description="País do fornecedor")
    cnpj: str = Field(..., pattern=r"^\d{14}$", description="CNPJ do fornecedor")
    inscricao_estadual: Optional[str] = Field(default=None, pattern=r"^\d{12}$", description="Inscrição Estadual do fornecedor")
    inscricao_municipal: Optional[str] = Field(default=None, pattern=r"^\d{12}$", description="Inscrição Municipal do fornecedor")
    site: Optional[str] = Field(default=None, format="uri", description="Site do fornecedor")
    observacoes: Optional[str] = Field(default=None, min_length=3, max_length=1000, description="Observações do fornecedor")
    status: Literal["ativo", "inativo"] = Field(default="ativo", min_length=3, max_length=100, description="Status do fornecedor")

#Schema para atualização de fornecedor
class AtualizaFornecedor(BaseModel):
    nome_razao: Optional[str] = Field(default=None, min_length=3, max_length=100, description="Nome do fornecedor")
    email_contato: Optional[EmailStr] = Field(default=None, format="email", description="Email do fornecedor")
    telefone: Optional[str] = Field(default=None, pattern=r"^\d{11}$", description="Telefone do fornecedor")
    endereco: Optional[str] = Field(default=None, min_length=3, max_length=100, description="Endereço do fornecedor")
    cidade: Optional[str] = Field(default=None, min_length=3, max_length=100, description="Cidade do fornecedor")
    estado: Optional[str] = Field(default=None, min_length=2, max_length=2, description="Estado do fornecedor")
    cep: Optional[str] = Field(default=None, pattern=r"^\d{8}$", description="CEP do fornecedor")
    pais: Optional[str] = Field(default=None, min_length=3, max_length=100, description="País do fornecedor")
    site: Optional[str] = Field(default=None, format="uri", description="Site do fornecedor")
    observacoes: Optional[str] = Field(default=None, min_length=3, max_length=1000, description="Observações do fornecedor")
    status: Optional[Literal["ativo", "inativo"]] = Field(default=None, min_length=3, max_length=100, description="Status do fornecedor")

class FornecedorResponse(BaseModel):
    id: int = Field(..., gt=0)
    nome_razao: str = Field(..., min_length=3, max_length=100, description="Nome do fornecedor")
    email_contato: Optional[EmailStr] = Field(default=None, format="email", description="Email do fornecedor")
    telefone: Optional[str] = Field(default=None, pattern=r"^\d{11}$", description="Telefone do fornecedor")
    endereco: Optional[str] = Field(default=None, min_length=3, max_length=100, description="Endereço do fornecedor")
    cidade: Optional[str] = Field(default=None, min_length=3, max_length=100, description="Cidade do fornecedor")
    estado: Optional[str] = Field(default=None, min_length=2, max_length=2, description="Estado do fornecedor")
    cep: Optional[str] = Field(default=None, pattern=r"^\d{8}$", description="CEP do fornecedor")
    pais: Optional[str] = Field(default=None, min_length=3, max_length=100, description="País do fornecedor")
    site: Optional[str] = Field(default=None, format="uri", description="Site do fornecedor")
    observacoes: Optional[str] = Field(default=None, min_length=3, max_length=1000, description="Observações do fornecedor")
    status: Optional[Literal["ativo", "inativo"]] = Field(default=None, min_length=3, max_length=100, description="Status do fornecedor")
    model_config = ConfigDict(from_attributes=True) # Para converter o modelo para o formato de resposta do SQLAlchemy

class FornecedorListResponse(BaseModel):
    fornecedores: List[FornecedorResponse]
    total: int = Field(..., gt=0, description="Total de fornecedores")
    pagina: int = Field(..., ge=1, description="Número da página")
    tamanho_pagina: int = Field(..., ge=1, description="Tamanho da página")
    total_paginas: int = Field(..., gt=0, description="Total de páginas")
    fornecedores_por_pagina: int = Field(..., gt=0, description="Fornecedores por página")
    model_config = ConfigDict(from_attributes=True) # Para converter o modelo para o formato de resposta do SQLAlchemy
