# Mapeamento do Projeto Agent Buy - CRUD Fornecedores

## Estrutura do Projeto

```
backend/
├── api/
│   ├── routes/
│   │   └── fornecedores.py (VAZIO)
│   └── schemas/
│       └── fornecedor.py (COMPLETO)
├── domain/
│   └── fornecedor/
│       └── models.py (INCOMPLETO)
├── services/ (DIRETÓRIO VAZIO)
├── core/ (DIRETÓRIO VAZIO)
├── main.py (VAZIO)
└── config.py (VAZIO)
```

## O que JÁ EXISTE

### 1. Schemas (Pydantic) - `backend/api/schemas/fornecedor.py`
**Status: COMPLETO**

- `CriaFornecedor` - Schema para criação (POST)
  - Campos: nome_razao, email_contato, telefone, endereco, cidade, estado, cep, pais, cnpj, inscricao_estadual, inscricao_municipal, site, observacoes, status
  - Validações: min_length, max_length, pattern, format

- `AtualizaFornecedor` - Schema para atualização (PUT/PATCH)
  - Todos os campos são Optional (exceto os que não podem ser atualizados)
  - Mesmas validações do CriaFornecedor

- `FornecedorResponse` - Schema de resposta (GET único)
  - Inclui id + todos os campos do fornecedor
  - `model_config = ConfigDict(from_attributes=True)` para conversão SQLAlchemy

- `FornecedorListResponse` - Schema para listagem paginada (GET lista)
  - Lista de FornecedorResponse
  - Campos de paginação: total, pagina, tamanho_pagina, total_paginas, fornecedores_por_pagina

### 2. Model (SQLAlchemy) - `backend/domain/fornecedor/models.py`
**Status: INCOMPLETO**

- `StatusFornecedor` (Enum) - DEFINIDO
  - ATIVO = "ativo"
  - INATIVO = "inativo"

- `Fornecedor(Base)` - INCOMPLETO
  - Classe iniciada mas sem definição de colunas
  - Importa Base de `backend.core.database` (que não existe ainda)

## O que NÃO EXISTE (Falta Implementar)

### 1. Core/Database - `backend/core/database.py`
- Base do SQLAlchemy
- Configuração de sessão (SessionLocal)
- Engine de conexão
- Função de inicialização de banco

### 2. Config - `backend/config.py`
- Variáveis de ambiente
- Configuração de banco de dados
- Settings da aplicação

### 3. Services - `backend/services/fornecedor.py`
- `criar()` - Create
- `listar()` - Read (lista paginada)
- `buscar_por_id()` - Read (único)
- `atualizar()` - Update
- `deletar()` - Delete

### 4. Routes - `backend/api/routes/fornecedores.py`
- POST /fornecedores
- GET /fornecedores (com paginação)
- GET /fornecedores/{id}
- PUT /fornecedores/{id}
- DELETE /fornecedores/{id}

### 5. Main - `backend/main.py`
- Configuração do FastAPI
- Registro de rotas
- Middlewares
- Inicialização da aplicação

## Arquitetura Planejada

```
Cliente HTTP
    ↓
Routes (FastAPI) - Recebe requisições
    ↓
Schemas (Pydantic) - Valida entrada/saída
    ↓
Services - Lógica de negócio
    ↓
Models (SQLAlchemy) - Persistência
    ↓
Banco de Dados
```

## Dependências Instaladas

- `pydantic>=2.12.4` - Validação de dados
- `sqlalchemy>=2.0.44` - ORM
- FastAPI (não listado no pyproject.toml, mas necessário)

## Próximos Passos para Completar o CRUD

1. Criar `backend/core/database.py` - Base e sessão SQLAlchemy
2. Criar `backend/config.py` - Configurações da aplicação
3. Completar `backend/domain/fornecedor/models.py` - Definir colunas do modelo
4. Criar `backend/services/fornecedor.py` - Implementar lógica de negócio
5. Criar `backend/api/routes/fornecedores.py` - Implementar endpoints HTTP
6. Criar `backend/main.py` - Configurar FastAPI e registrar rotas

## Fluxo Completo do CRUD

```
Cliente faz requisição HTTP
    ↓
Routes (FastAPI) recebe
    ↓
Valida com Schemas (Pydantic)
    ↓
Chama Service (lógica de negócio)
    ↓
Service usa Model (SQLAlchemy)
    ↓
Persiste no Banco de Dados
    ↓
Retorna resposta (Schema)
```

## Endpoints Planejados

- **POST /fornecedores** → Create (criar fornecedor)
- **GET /fornecedores** → Read (lista paginada)
- **GET /fornecedores/{id}** → Read (único fornecedor)
- **PUT /fornecedores/{id}** → Update (atualizar fornecedor)
- **DELETE /fornecedores/{id}** → Delete (deletar fornecedor)

## Resumo da Arquitetura

Sim, é um CRUD completo seguindo uma arquitetura em camadas:

- **API Layer (Routes)** → recebe requisições
- **Service Layer** → lógica de negócio
- **Domain Layer (Models)** → persistência
- **Schemas** → validação de entrada/saída

Isso é um padrão comum em APIs REST e é exatamente o que a FASE 1 do projeto pede: "CRUD Fornecedores, Materiais, Pedidos".

Depois de finalizar o CRUD de Fornecedores, pode-se replicar a mesma estrutura para Materiais e Pedidos.

