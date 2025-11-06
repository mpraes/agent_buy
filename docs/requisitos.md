# AgentBuy - Versão Enriquecida

## 🎯 Proposta de Valor (reescrita)

```markdown
AgentBuy é um ERP inteligente de supply chain para manufaturas PME que:
- Automatiza decisões de compra via agente IA (não apenas registra pedidos)
- Previne ruptura de estoque E gastos desnecessários via previsão de demanda
- Opera via chat natural (WhatsApp) ou dashboards (não requer treinamento)
- Integra dados dispersos (estoque, notas, histórico, previsões) em decisões
```

---

## 📦 Módulos Expandidos

### ✅ Existentes (validar)
- Fornecedores
- Pedidos de Compra
- Entradas (NF-e)
- Controle de Estoque
- Materiais (Masterdata)
- Previsão Demanda

### ➕ Novos (críticos para PME)

**Ordens de Produção**
```
- Vincula materiais aos produtos finais
- LLM calcula necessidade automática
- Desencadeia sugestões de compra
```

**Análise ABC**
```
- Classifica materiais por impacto (curva ABC)
- Diferentes políticas por classe (A=mais frequente, C=menos frequente)
```

**Alertas Inteligentes**
```
- Ruptura iminente (predição)
- Preço anômalo (histórico)
- Qualidade (taxa de devolução)
- Lead time vencendo
```

**Sugestões de Compra (Agentico)**
```
- LLM analisa: estoque atual, previsão, lead time, capacidade caixa
- Propõe: quanto comprar, de quem, quando, risco de não comprar
- Usuário aprova/rejeita via chat
```

**Histórico de Preços**
```
- Rastreia preço por fornecedor/período
- Negocia: "comprei a R$50, agora quer R$60?"
- Identifica melhores fornecedores
```

---

## 🤖 Inteligência Agentica (Core Value)

### Fluxos LLM

```python
# 1️⃣ CHAT: "Cadê o parafuso M8?"
LLM detecta: pergunta sobre material
├─ Busca estoque atual
├─ Carrega previsão demanda (próximos 30 dias)
├─ Valida lead time do fornecedor
├─ Retorna: "Temos 100 unidades. Em 15 dias previsão consome 80.
│           Lead time = 10 dias. Sugestão: COMPRAR 200 AGORA"
└─ Usuário: "OK" → Cria pedido automaticamente

# 2️⃣ SUGESTÃO AUTOMÁTICA
Robo roda a cada 6h
├─ Análise ABC para cada material
├─ Calcula ponto de reordenação
├─ Se estoque < ponto → propõe compra
├─ Compara 3 fornecedores
└─ Aguarda aprovação (chat ou dashboard)

# 3️⃣ ANÁLISE DE RISCO
Entrada de NF
├─ Compara quantidades esperadas vs recebidas
├─ Flagga qualidade (se frequente = aviso)
├─ Valida prazo de entrega
└─ Sugere ação: "Fornecedor X atrasou 3x. Considere Y?"

# 4️⃣ NEGOCIAÇÃO INTELIGENTE
Usuário: "Quero comprar parafuso M8 de novo"
LLM:
├─ Histórico: pagou R$50, R$48, R$52 (últimas 3x)
├─ Mercado: fornecedor Y cobra R$46
├─ Sugestão: "Negocie com X antes de mudar para Y"
```

---

## 🏗️ Arquitetura Sugerida

```
┌─────────────────────────────────────────────────────┐
│                    INTERFACE                         │
├──────────────────┬──────────────────────────────────┤
│  WhatsApp Chat   │     Dashboard (JS/React)          │
│  (Conversação)   │     (Visualização + Ação)        │
└──────────────────┴──────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────┐
│              LLM ORCHESTRATOR                        │
├─────────────────────────────────────────────────────┤
│ - Parse intent (pergunta vs. ação)                  │
│ - Valida contexto (qual empresa, período)           │
│ - Routing (qual módulo ativar)                      │
│ - Executa função ou retorna resposta                │
└─────────────────────────────────────────────────────┘
                          ↓
┌──────────┬──────────┬──────────┬──────────────────┐
│ Estoque  │ Pedidos  │ Previsão │ Fornecedores    │
│ Service  │ Service  │ Service  │ Service         │
└──────────┴──────────┴──────────┴──────────────────┘
                          ↓
┌─────────────────────────────────────────────────────┐
│           PostgreSQL                                 │
│  (Fornecedores, Pedidos, Estoque, NF, Histórico)   │
└─────────────────────────────────────────────────────┘
```

---

## 💬 Exemplos de Chat (UX/Agência)

```
👤 Usuário: "Quantos parafusos M8 temos?"
🤖 AgentBuy: "Temos 500 unidades. Estoque bom por 20 dias 
             (consumo previsto). Lead time fornecedor: 15 dias.
             Status: ✅ OK"

👤 Usuário: "E se a produção aumentar 30%?"
🤖 AgentBuy: "Nesse caso consumo vai para 30 dias.
             Sugestão: COMPRAR AGORA 800 unidades de Fornecedor X
             (entrega em 15d, cabe no caixa).
             Risco de não comprar: ruptura em 5 dias.
             Quer proceder?"

👤 Usuário: "Sim"
🤖 AgentBuy: "✅ Pedido #1023 criado. Enviando para X.
             Te aviso quando chegar."

👤 Usuário: "Qual meu melhor fornecedor de parafuso?"
🤖 AgentBuy: "Histórico últimos 6 meses:
             - Fornecedor X: 12 compras, 98% on-time, R$50/un
             - Fornecedor Y: 3 compras, 100% on-time, R$48/un
             - Fornecedor Z: 5 compras, 80% on-time, R$52/un
             Recomendação: X (confiável) ou Y (barato)"
```

---

## 🚀 Fases de Desenvolvimento

```
FASE 1 (MVP - 2 semanas)
├─ CRUD Fornecedores, Materiais, Pedidos
├─ Chat básico: "quanto temos de X?"
├─ Dashboard simples (estoque atual)
└─ Backend Python + BD Postgres

FASE 2 (Inteligência - 3 semanas)
├─ LLM conectado (Claude API)
├─ Previsão demanda (regressão simples)
├─ Sugestões automáticas de compra
├─ Integração NF-e entrada
└─ Alertas (chat + email)

FASE 3 (PME-Ready - 2 semanas)
├─ Dashboard completo (React)
├─ Análise ABC
├─ Histórico de preços
├─ Relatórios (estoque, gastos, lead time)
└─ Multi-empresa

FASE 4 (Otimização)
├─ Previsão avançada (ML)
├─ Negociação automática
├─ API de integração (outros ERPs)
```

---

## 🔧 Tech Stack (Validado)

```python
# Backend
- FastAPI (APIs para chat + dashboard)
- Anthropic Claude (LLM orchestration)
- SQLAlchemy ORM
- Pydantic (validação)
- Celery (jobs agenticos)

# BD
- PostgreSQL (relacional)
- Redis (cache de previsões)

# Frontend
- React (dashboard)
- Material-UI ou Shadcn (componentes)
- Chart.js (gráficos estoque/previsão)

# Integração
- Twilio (WhatsApp API)
- XML de NF-e (Brasil)
```

---

## 📊 Diferenciais vs Concorrentes

| Recurso | AgentBuy | Erp Padrão |
|---------|----------|-----------|
| Chat natural | ✅ | ❌ |
| Sugestão automática de compra | ✅ | ❌ |
| Previsão demanda integrada | ✅ | Opcional/pago |
| Análise de risco fornecedor | ✅ | ❌ |
| Interface WhatsApp | ✅ | ❌ |
| Curva de aprendizado | Baixa | Alta |

---

## 💰 Modelo de Negócio (sugestão)

```
- SaaS: R$ 299/mês (startup)
- Escalas: 
  - Plano Básico: 1 dep, 5 usuários → R$ 299
  - Plano Pro: 3 deps, 20 usuários → R$ 799
  - Enterprise: Unlimited → R$ 2.490
- Setup: R$ 2.000 (consultoria, importação dados)
```

---
