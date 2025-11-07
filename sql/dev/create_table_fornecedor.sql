-- Criar tipo ENUM (sem IF NOT EXISTS - não é suportado em todas as versões)
-- Se já existir, vai dar erro, mas pode ignorar
CREATE TYPE status_fornecedor AS ENUM ('ativo', 'inativo');

-- Criar tabela no schema dev
CREATE TABLE dev.fornecedor (
    id SERIAL PRIMARY KEY,
    nome_razao VARCHAR(100) NOT NULL,
    email_contato VARCHAR(255),
    telefone VARCHAR(11),
    endereco VARCHAR(100),
    cidade VARCHAR(100),
    estado CHAR(2),
    cep VARCHAR(8),
    pais VARCHAR(100),
    cnpj VARCHAR(14) NOT NULL UNIQUE,
    inscricao_estadual VARCHAR(12),
    inscricao_municipal VARCHAR(12),
    site VARCHAR(255),
    observacoes TEXT,
    status VARCHAR(10) DEFAULT 'ativo',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);