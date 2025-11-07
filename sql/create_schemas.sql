-- Criar schemas para dev e prd
CREATE SCHEMA IF NOT EXISTS dev;
CREATE SCHEMA IF NOT EXISTS prd;

-- Dar permissões (ajuste conforme necessário)
GRANT ALL ON SCHEMA dev TO postgres;
GRANT ALL ON SCHEMA prd TO postgres;