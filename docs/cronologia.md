# AgentBuy - Cronologia de Desenvolvimento

## 🔵 SEMANA 1: Fundação Mínima

### Dia 1-2: Setup + BD
```
✅ Criar repo Git
✅ PostgreSQL local (Docker)
✅ Projeto Python (FastAPI)
✅ SQLAlchemy models básicos:
   - Fornecedor
   - Produto
   - PedidoCompra
   - ItemPedido
✅ migrations (Alembic)
```

**Teste**: Criar 3 fornecedores no BD via CLI

---

### Dia 3-4: APIs CRUD
```
✅ POST /fornecedores (criar)
✅ GET /fornecedores (listar)
✅ GET /fornecedores/{id} (detalhe)
✅ POST /produtos
✅ GET /produtos
✅ POST /pedidos-compra
✅ GET /pedidos-compra
```

**Teste**: Usar Postman/curl para criar fornecedor + produto + pedido

---

### Dia 5: Dashboard Mínimo
```
✅ React vazio
✅ 1 página: Listar Fornecedores (tabela)
✅ 1 página: Listar Produtos (tabela)
✅ 1 página: Listar Pedidos (tabela)
✅ Conectar ao backend
```

**Teste**: Dashboard exibe dados do BD

---

## 🟡 SEMANA 2: Lógica de Negócio

### Dia 1-2: Estoque
```
✅ Adicionar coluna: Produto.estoque (int)
✅ Ao criar ItemPedido:
   - Valida se produto tem estoque
   - Reduz estoque
✅ Ao receber pedido (status = "recebido"):
   - Aumenta estoque
✅ Endpoint GET /produtos/{id}/estoque
```

**Teste**: Criar pedido → estoque reduz. Receber → estoque sobe.

---

### Dia 3: Entrada de NF
```
✅ Model: NotaFiscal
   - id
   - pedido_id
   - numero_nf
   - data_emissao
   - total
   - status (pendente, conferida)

✅ Endpoint POST /notas-fiscais
✅ Validação: NF vinculada a pedido
✅ Ao conferir NF → atualiza estoque
```

**Teste**: Gerar NF, conferir, ver estoque atualizar

---

### Dia 4: Lead Time + Previsão Básica
```
✅ Fornecedor.lead_time_dias (int)
✅ Produto.consumo_mensal (float)
✅ Lógica: 
   Quantidade_Compra = Consumo_30dias + Buffer_Segurança
   
✅ Endpoint POST /sugestoes-compra
   GET /sugestoes-compra
```

**Teste**: Criar sugestão de compra via endpoint

---

### Dia 5: UI - Dashboards Essenciais
```
✅ Dashboard 1: Estoque Atual (tabela + aviso baixo estoque)
✅ Dashboard 2: Pedidos Pendentes
✅ Dashboard 3: Sugestões de Compra
✅ Botão: "Aprovar Sugestão" → cria pedido
```

**Teste**: Clicar em "Aprovar" cria pedido automaticamente

---

## 🟠 SEMANA 3: LLM + Chat

### Dia 1-2: Integração Claude
```
✅ Instalar: pip install anthropic
✅ Criar service: LLMService
✅ Funções disponíveis (tool_use):
   - get_estoque_produto(produto_id)
   - get_sugestoes_compra()
   - get_pedidos_pendentes()
   - criar_pedido_compra(fornecedor_id, itens)

✅ Endpoint POST /chat
   - Input: mensagem do usuário
   - Output: resposta LLM + ações executadas
```

**Teste**: Chat pergunta → LLM retorna resposta

---

### Dia 3: Exemplos Chat Funcionais
```
✅ "Quanto temos de parafuso?"
   → LLM chama get_estoque_produto()
   → Retorna valor

✅ "Me sugira compras"
   → LLM chama get_sugestoes_compra()
   → Retorna lista formatada

✅ "Aprova compra de 1000 parafusos de Fornecedor X?"
   → LLM chama criar_pedido_compra()
   → Cria pedido
```

**Teste**: Trocar 10 mensagens via /chat

---

### Dia 4: Integração WhatsApp
```
✅ Conta Twilio gratuita
✅ Setup webhook WhatsApp
✅ Endpoint POST /webhook/whatsapp
   - Recebe mensagem
   - Envia para /chat
   - Retorna resposta via WhatsApp

✅ Testar via app Twilio
```

**Teste**: Mandar mensagem WhatsApp → receber resposta

---

### Dia 5: UI Chat
```
✅ Componente Chat no React
✅ Conectar a POST /chat
✅ Histórico de conversa
✅ Mostrar ações executadas (ex: "Pedido criado")
```

**Teste**: Chat web + chat WhatsApp funcionando

---

## 🟢 SEMANA 4+: Refinamento + Features Avançadas

### Prioridade 1: Confiabilidade
```
✅ Validações rigorosas
✅ Tratamento de erros
✅ Logs estruturados
✅ Testes unitários (pytest)
✅ Deploy (Railway ou Heroku)
```

### Prioridade 2: Dados Reais
```
✅ Histórico de preços (Fornecedor X)
✅ Análise ABC (curva de Pareto)
✅ Lead time real (últimas 10 compras)
✅ Taxa de on-time (chegou no prazo?)
```

### Prioridade 3: Inteligência
```
✅ Previsão de demanda (regressão linear)
✅ Alertas automáticos (a cada 6h)
✅ Recomendação de fornecedor
✅ Análise de risco (preço anômalo)
```

---

## 📅 Timeline Visual

```
SEMANA 1        SEMANA 2         SEMANA 3        SEMANA 4+
├─ BD ✅         ├─ Estoque ✅    ├─ LLM ✅       ├─ Histórico ✅
├─ APIs ✅       ├─ NF ✅         ├─ Chat ✅      ├─ ABC ✅
├─ UI básica ✅  ├─ Sugestão ✅   ├─ WhatsApp ✅  ├─ Previsão ✅
                 ├─ Lead time ✅  ├─ UI Chat ✅   ├─ Deploy ✅
                 ├─ Dashboard ✅                  └─ Beta → Clientes
```

---

## ✅ Checklist Semanal

### Semana 1 - Mínimo Viável
- [ ] BD rodando
- [ ] 5 endpoints CRUD funcionando
- [ ] Dashboard exibe dados
- [ ] Git com commit diário

### Semana 2 - Lógica
- [ ] Estoque se atualiza
- [ ] NF integrada
- [ ] Sugestões de compra
- [ ] 3 dashboards completos

### Semana 3 - Inteligência
- [ ] LLM respondendo
- [ ] WhatsApp ativo
- [ ] Chat web funcionando
- [ ] 5 exemplos de conversation funcionando

### Semana 4+ - Produção
- [ ] Testes escritos (>80% coverage)
- [ ] Dados históricos carregados
- [ ] Deploy em staging
- [ ] Pronto para 1º cliente

---

## 🚀 Como Começar HOJE

```bash
# 1. Criar estrutura
mkdir agentbuy
cd agentbuy
git init

# 2. Setup Python
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install fastapi sqlalchemy psycopg2-binary alembic pydantic

# 3. Docker Postgres
docker run --name agentbuy-db \
  -e POSTGRES_PASSWORD=senha123 \
  -e POSTGRES_DB=agentbuy \
  -p 5432:5432 \
  -d postgres:15

# 4. Criar main.py
# (já vou preparar o template)
```

---

Quer que eu crie o **template pronto** para Dia 1-2 (BD + models)?