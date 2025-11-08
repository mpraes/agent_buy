# Agent Buy - Sistema de Gestão de Compras

Sistema de gestão de compras com foco em fornecedores, materiais e pedidos.

## 📋 Status do Projeto

### ✅ Implementado

#### Infraestrutura
- ✅ Projeto Python com FastAPI
- ✅ PostgreSQL via Docker
- ✅ Configuração de ambiente (.env)
- ✅ Estrutura de pastas organizada

#### Banco de Dados
- ✅ Modelo SQLAlchemy para Fornecedor
- ✅ Schema `dev` e `prd` configurados
- ✅ Tabela `fornecedor` criada no schema `dev`
- ✅ Constraints e validações no banco

#### Backend - Service Layer
- ✅ `cria_fornecedor()` - Criar fornecedor
- ✅ `lista_fornecedores()` - Listar com paginação
- ✅ `busca_fornecedor_por_id()` - Buscar por ID
- ✅ `atualiza_fornecedor()` - Atualizar (partial update)
- ✅ `deleta_fornecedor()` - Deletar fornecedor

#### Backend - API Layer
- ✅ `POST /fornecedores/` - Criar fornecedor (funcionando)
- ⏳ `GET /fornecedores/` - Listar fornecedores
- ⏳ `GET /fornecedores/{id}` - Buscar por ID
- ⏳ `PUT /fornecedores/{id}` - Atualizar fornecedor
- ⏳ `DELETE /fornecedores/{id}` - Deletar fornecedor

#### Validações e Tratamento de Erros
- ✅ Schemas Pydantic para validação
- ✅ Exceções customizadas:
  - `FornecedorNotFoundError`
  - `FornecedorValidationError`
  - `FornecedorIntegrityError`
  - `FornecedorDatabaseError`
- ✅ Tratamento de transações (rollback em erros)
- ✅ Validação de paginação

## 🏗️ Arquitetura

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
Banco de Dados (PostgreSQL)
```

## 📁 Estrutura do Projeto

```
agent_buy/
├── backend/
│   ├── api/
│   │   ├── routes/
│   │   │   └── fornecedores.py      # Rotas HTTP
│   │   └── schemas/
│   │       └── fornecedor.py        # Schemas Pydantic
│   ├── core/
│   │   └── database.py              # Configuração SQLAlchemy
│   ├── domain/
│   │   └── fornecedor/
│   │       └── models.py            # Modelo SQLAlchemy
│   ├── services/
│   │   └── fornecedor.py            # Lógica de negócio
│   ├── exceptions.py                # Exceções customizadas
│   ├── config.py                    # Configurações
│   └── main.py                      # Aplicação FastAPI
├── docker/
│   └── docker-compose.yml           # Configuração PostgreSQL
├── sql/
│   ├── create_schemas.sql           # Scripts de schema
│   └── dev/
│       └── create_table_fornecedor.sql
├── docs/                            # Documentação
├── .env                             # Variáveis de ambiente
└── README.md
```

## 🚀 Como Rodar

### Pré-requisitos

- Python 3.13+
- Docker e Docker Compose
- PostgreSQL (via Docker)

### 1. Configurar Ambiente

```bash
# Copiar .env.example para .env
cp .env.example .env

# Editar .env com suas credenciais reais
# IMPORTANTE: O arquivo .env está no .gitignore e NÃO será commitado
```

### 2. Iniciar PostgreSQL via Docker

```bash
# Iniciar container PostgreSQL
docker-compose -f docker/docker-compose.yml up -d

# Verificar se está rodando
docker ps | grep postgres
```

### 3. Criar Schemas no Banco

```bash
# Acessar PostgreSQL
docker exec -it agentbuy-postgres psql -U postgres -d agentbuy_db

# Criar schemas
CREATE SCHEMA IF NOT EXISTS dev;
CREATE SCHEMA IF NOT EXISTS prd;

# Sair
\q
```

### 4. Instalar Dependências

```bash
# Usando uv (recomendado)
uv sync

# Ou usando pip
pip install -e .
```

### 5. Iniciar API

```bash
# Desenvolvimento (com reload)
uvicorn backend.main:app --reload

# Produção
uvicorn backend.main:app --host 0.0.0.0 --port 8000
```

### 6. Acessar Documentação

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc
- **API Root**: http://127.0.0.1:8000/

## 🧪 Testar API

### Criar Fornecedor (POST)

```bash
curl -X POST "http://127.0.0.1:8000/fornecedores/" \
  -H "Content-Type: application/json" \
  -d '{
    "nome_razao": "Empresa Teste LTDA",
    "cnpj": "12345678000190",
    "email_contato": "contato@empresa.com",
    "telefone": "11987654321",
    "status": "ativo"
  }'
```

### Verificar no Banco

```bash
# Ver fornecedores criados
docker exec -it agentbuy-postgres psql -U postgres -d agentbuy_db -c "SELECT * FROM dev.fornecedor;"
```

## 📚 Tecnologias

- **FastAPI** - Framework web moderno e rápido
- **SQLAlchemy** - ORM para Python
- **Pydantic** - Validação de dados
- **PostgreSQL** - Banco de dados relacional
- **Docker** - Containerização
- **Uvicorn** - Servidor ASGI

## 🔧 Configuração

### Variáveis de Ambiente (.env)

**⚠️ IMPORTANTE**: O arquivo `.env` está no `.gitignore` e **NÃO será commitado** no Git.

Use o arquivo `.env.example` como template:

```bash
# Copiar template
cp .env.example .env

# Editar com suas credenciais
DATABASE_URL=postgresql://usuario:senha@localhost:5432/nome_banco
APP_NAME=Agent Buy
APP_ENV=development  # ou production
```

### Schemas do Banco

- **dev**: Ambiente de desenvolvimento
- **prd**: Ambiente de produção

O schema é selecionado automaticamente baseado em `APP_ENV`.

## 📝 Próximos Passos

### Fase 1: Completar CRUD de Fornecedores
- [ ] Implementar `GET /fornecedores/` - Listar fornecedores
- [ ] Implementar `GET /fornecedores/{id}` - Buscar por ID
- [ ] Implementar `PUT /fornecedores/{id}` - Atualizar fornecedor
- [ ] Implementar `DELETE /fornecedores/{id}` - Deletar fornecedor
- [ ] Adicionar tratamento de exceções HTTP nas rotas
- [ ] Adicionar filtros na listagem (por status, nome, etc.)

### Fase 2: Melhorias e Validações
- [ ] Adicionar validação de CNPJ (formato e dígitos verificadores)
- [ ] Adicionar validação de CEP (consultar API externa)
- [ ] Adicionar logs estruturados
- [ ] Adicionar testes unitários para services
- [ ] Adicionar testes de integração para rotas

### Fase 3: Outros Módulos
- [ ] CRUD de Produtos
- [ ] CRUD de Pedidos de Compra
- [ ] CRUD de Itens de Pedido
- [ ] Relacionamentos entre entidades

### Fase 4: Funcionalidades Avançadas
- [ ] Gestão de estoque
- [ ] Notas fiscais
- [ ] Sugestões de compra
- [ ] Dashboard com métricas

## 🐛 Troubleshooting

### Erro: "Connection refused"
- Verificar se PostgreSQL está rodando: `docker ps | grep postgres`
- Verificar URL de conexão no `.env`
- Verificar se a porta 5432 está disponível

### Erro: "Schema não encontrado"
- Verificar se o schema `dev` ou `prd` existe no banco
- Verificar valor de `APP_ENV` no `.env`
- Executar `CREATE SCHEMA IF NOT EXISTS dev;`

### Erro: "Tabela não encontrada"
- Verificar se as tabelas foram criadas no schema correto
- Executar `init_db()` para criar tabelas
- Verificar logs do SQLAlchemy (`echo=True`)

## 📖 Documentação Adicional

- [Mapeamento CRUD Fornecedores](docs/mapeamento_crud_fornecedores.md)
- [Cronologia de Desenvolvimento](docs/cronologia.md)

## 👥 Contribuindo

1. Criar branch para feature
2. Implementar mudanças
3. Testar localmente
4. Fazer commit com mensagem descritiva
5. Abrir Pull Request

## 📄 Licença

[Adicionar licença]

---

**Última atualização**: 2025-01-08
**Versão**: 0.1.0

