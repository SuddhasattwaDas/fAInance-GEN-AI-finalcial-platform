<div align="center">


# 💰 fAInance

### AI-Powered Personal Finance Platform

**Escape debt. Plan investments. Detect fraud. Understand every decision.**

*Your own AI advisory team — behind a single React UI.*

<br/>

<!-- Tech stack -->
![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)

<!-- Meta -->
![Status](https://img.shields.io/badge/status-demo--ready-brightgreen?style=flat-square)
![Always Demoable](https://img.shields.io/badge/AI-graceful%20fallback-blueviolet?style=flat-square)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-orange?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)

<br/>

[**✨ Features**](#-highlights) &nbsp;•&nbsp;
[**🎯 Flagship**](#-the-flagship-debt-escape-planner) &nbsp;•&nbsp;
[**🏗️ Architecture**](#️-system-architecture) &nbsp;•&nbsp;
[**⚡ Quick Start**](#-quick-start) &nbsp;•&nbsp;
[**📡 API**](#-api-reference)

</div>

---

## 🚀 What is fAInance?

Traditional financial advice is **expensive, biased, and hard to access** — especially for people trapped in high-interest debt or new to investing.

fAInance changes that. It gives every user a full **AI-powered advisory team** through one clean interface:

> 🧠 A multi-agent backend (LangGraph) routes each request to the right specialist — debt strategist, portfolio analyst, fraud investigator, and more — while **every AI call has a deterministic fallback**, so the app is **always demoable, even without an LLM key.**

<div align="center">

| 💸 **Escape debt** | 📈 **Grow wealth** | 🛡️ **Stay safe** | 🎓 **Learn fast** |
|:---:|:---:|:---:|:---:|
| Month-by-month payoff plans + a bank negotiation script | Portfolio drift + plain-English commentary | Document forensics that catch tampering | Gamified modules with XP & badges |

</div>

---

## ✨ Highlights

<table>
<tr>
<td width="50%" valign="top">

### 🎯 Debt Escape Planner *(flagship)*
Turns *"I'm drowning, where do I start?"* into a concrete plan. Simulates **avalanche vs. snowball** month-by-month, flags **toxic debts**, evaluates **consolidation**, and writes a **script you can read to your bank**.

</td>
<td width="50%" valign="top">

### 🔍 Explainable AI
Loan-approval and credit-score decisions come with **SHAP/LIME-style attributions** — no black boxes. Every recommendation shows *why*.

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🛡️ Fraud Shield
Inspects uploaded documents for tampering using **EXIF analysis, perceptual hashing, and Error-Level Analysis (ELA)** plus rule-based checks.

</td>
<td width="50%" valign="top">

### 🤖 Multi-Agent Orchestration
A **LangGraph `StateGraph`** wires together 9 specialist agents behind a single intent router — advisor, portfolio, stock, news, fraud, education & chat.

</td>
</tr>
</table>

---

## 🖼️ Screenshots

> 📸 *Drop your screenshots or a demo GIF here to make the README pop.*

<div align="center">

| Dashboard | Debt Escape Planner | Explainable Loan Predictor |

![WhatsApp Image 2025-02-09 at 11 48 59_d6135947](https://github.com/user-attachments/assets/6c3150c2-7592-41a6-9755-4c9d5c2e6bf3)
![image](https://github.com/user-attachments/assets/fb8ed43e-a4c2-4598-8b6e-bd0d50d602f1)
![image](https://github.com/user-attachments/assets/2b216b49-98f7-4cbc-a150-32c36a4227ad)

</div>

---

## 🎯 The Flagship: Debt Escape Planner

> **Route:** `/debt` &nbsp;·&nbsp; **API prefix:** `/api/debt`

Add every debt you owe — credit cards, personal loans, BNPL, EMIs — set a monthly budget with a slider, and get the **fastest and cheapest path out.**

<details open>
<summary><b>📋 What the planner returns</b></summary>

<br/>

**1️⃣ Two payoff strategies, simulated month-by-month**

| Strategy | How it works | Best for |
|---|---|---|
| ⛰️ **Avalanche** | Minimums on all, everything extra to the **highest-APR** debt | Minimizing total interest (mathematically optimal) |
| ❄️ **Snowball** | Minimums on all, everything extra to the **smallest balance** | Momentum — clearing the first debt sooner keeps you on plan |

Each strategy returns: months to debt-free, total interest paid, total money paid, per-debt payoff dates, and a monthly rollup for charting.

**2️⃣ Recommended strategy + rationale** — defaults to avalanche, but switches to snowball if it clears the first debt materially sooner *and* interest stays within 5% of avalanche.

**3️⃣ Toxic-debt detection** — auto-flags:
- 🔴 APR ≥ 30% (`toxic`) or ≥ 24% (`high`)
- ⚠️ Payday-style loans (renew at 300%+ effective APR)
- ♾️ Debts where the minimum doesn't cover interest (grow forever)
- 🐌 Debts that take 240+ months at the minimum only

**4️⃣ Consolidation analysis** — simulates rolling every balance into one loan and **only recommends it when savings exceed 5%** of status-quo avalanche interest.

**5️⃣ Negotiation script** — a per-debt phone script for your lender's hardship team, with concrete asks (rate reduction, hardship plan, fee waiver + balance transfer for cards). Deterministic base, LLM-polished when a key is set.

**6️⃣ Budget-too-low guard** — if the budget can't cover `interest + minimums`, the plan is refused with the minimum viable amount, because any "plan" at that pace would be misleading.

</details>

<details>
<summary><b>✅ Verified guardrails (real numbers)</b></summary>

<br/>

Sample plan — **₹307,000** across two credit cards + a personal loan, **₹20,000/mo** budget — simulates cleanly in **19 months** under both strategies:

```
avalanche : months=19  interest=₹53,467.29  first-cleared = HDFC card (month 9)
snowball  : months=19  interest=₹54,609.91  first-cleared = ICICI card (month 6)
toxic     : HDFC card, ICICI card
consolidation @ ~14% → NOT recommended (48-mo term stretches interest)
```

Guardrails baked into the math:
- ⛔ Max simulation horizon is **600 months** — the loop can never hang.
- 🚩 Any debt whose minimum can't cover interest is **flagged, not silently looped forever.**
- 💡 Consolidation is recommended **only when the savings are real.**

</details>

---

## 🧩 Feature Set

| Area | Route | API prefix | Purpose |
|---|---|---|---|
| 🎯 **Debt Escape Planner** | `/debt` | `/api/debt` | Avalanche/snowball payoff, toxic detection, consolidation, negotiation scripts *(flagship)* |
| 💬 AI Advisor | `/advisor` | `/api/advisor` | RAG-backed advice on loans, cards, investing, mutual funds, budget |
| 📊 Loan Predictor | `/loan` | `/api/loan` | Loan-approval prediction + SHAP/LIME contributions + credit-score prediction |
| 📈 Portfolio | `/portfolio` | `/api/portfolio` | Snapshot, target vs. actual allocation, drift, AI commentary |
| 🏦 Stock Agent | `/stock` | `/api/stock` | yfinance quotes + LLM narrative (mock fallback if unavailable) |
| 📰 News | `/news` | `/api/news` | NewsAPI headlines + LLM summarization |
| 🛡️ Fraud Shield | `/fraud` | `/api/fraud` | Document forensics (EXIF, perceptual hash, ELA) + rules |
| 🎓 Education | `/education` | `/api/education` | Gamified learning modules with XP, levels, badges |
| 🤖 Chatbot | `/chat` | `/api/chatbot` | BankFAQ-augmented conversational agent |
| 🔐 Auth + Profile | `/login`, `/settings` | `/api/auth`, `/api/user` | JWT auth and profile management |

---

## 🏗️ System Architecture

**Design in one line:** *thin HTTP routes → pure-Python services → LangGraph agents, with a single LLM chokepoint that gracefully degrades.*

```
┌─────────────────────────────────────────────────────────────────────┐
│                       FRONTEND (React + Vite)                        │
│   Pages/AI/*  ──calls──▶  api/client.ts (axios + JWT interceptor)     │
│   AuthContext (JWT)              LanguageContext (i18n)               │
└──────────────────────────────┬──────────────────────────────────────┘
                               │  /api/*  (Vite proxy → :5000)
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│                            BACKEND (Flask)                            │
│   app.py ── registers ──▶ routes/*.py   (one blueprint per feature)   │
│   routes/*.py ── delegates logic to ──▶ services/*.py                 │
│                    (pure Python, zero Flask imports, unit-testable)   │
│                                                                       │
│   Multi-agent endpoints routed through:                              │
│      agents/orchestrator.py  (LangGraph StateGraph)                  │
│         ├─ router_agent          intent classification               │
│         ├─ advisor_agent         loan / card / investment            │
│         ├─ explainability_agent  SHAP-style attributions             │
│         ├─ portfolio_agent       snapshot + drift + commentary       │
│         ├─ stock / news / fraud / education / chatbot agents         │
│         └─ state.py              shared AgentState schema             │
│                                                                       │
│   All LLM calls funnel through services/llm_service.py               │
│      ├─ PORTKEY_API_KEY set   → real call to Portkey gateway         │
│      └─ PORTKEY_API_KEY unset → deterministic mock (never breaks)    │
│                                                                       │
│   Persistence: models/store.py — thread-safe in-memory store         │
│   (profiles, holdings, loan history). Swap for a real DB in prod.    │
└─────────────────────────────────────────────────────────────────────┘
```

<details>
<summary><b>🔄 Request lifecycle — Debt Escape Planner example</b></summary>

<br/>

1. `DebtPage.tsx` collects debts + budget → `POST /api/debt/plan` (JWT auto-attached).
2. `routes/debt.py` validates payload & auth, then calls `services/debt_service.py`.
3. `debt_service.py` (pure logic, no Flask): runs avalanche sim → runs snowball sim → flags toxic debts → evaluates consolidation → picks the recommended strategy.
4. `routes/debt.py` serializes the result to JSON.
5. `DebtPage.tsx` renders payoff charts, toxic-debt badges, and the negotiation script.

This **route → service split** means every simulation can be unit-tested with plain Python — no Flask app context, no HTTP mocking, no LLM key.

</details>

<details>
<summary><b>💡 Why this shape</b></summary>

<br/>

- **Blueprints per feature** — each domain (debt, loans, portfolio, fraud…) is independently ownable and testable.
- **`services/` has zero Flask imports** — logic is portable: reuse it from a script, notebook, or future worker/queue.
- **LangGraph only where it earns its keep** — multi-step reasoning uses the graph; simple CRUD (auth, profile) skips it.
- **Single LLM chokepoint** — one place to swap providers, add retries/guardrails, or fall back to mocks. Every feature benefits automatically.
- **In-memory store today, real DB tomorrow** — `models/store.py` is a thin interface, so swapping in Postgres/Mongo never touches route or service code.

</details>

---

## ⚡ Quick Start

> **Prerequisites:** Python **3.11+** (works on 3.14) · Node.js **18+**

### 🐍 1. Backend

```bash
cd backend
python -m pip install -r requirements.txt

# Optional: RAG (FAISS + sentence-transformers), SHAP/LIME, yfinance
# python -m pip install -r requirements-optional.txt

cp .env.example .env          # then fill in keys (see below)
python app.py                 # → http://localhost:5000
```

🩺 Health check → `http://localhost:5000/api/health`

### ⚛️ 2. Frontend

```bash
cd frontend
npm install
npm run dev                   # → http://localhost:5173
```

Vite proxies every `/api/*` call to Flask on port 5000.

### 🎬 3. First use

1. Open `http://localhost:5173` → click **Get started**.
2. Sign up → land on the dashboard.
3. The red **"Escape credit-card & loan debt"** hero card takes you to the flagship — **three sample debts are pre-loaded**, so you can try it in one click. 🎉
4. Personalize other features at `/settings` (income, expenses, credit score, risk tolerance).

---

## 🔑 Environment Variables

Set in `backend/.env` (copy from `backend/.env.example`):

| Variable | Required? | Purpose |
|---|:---:|---|
| `PORTKEY_API_KEY` | ⭐ Recommended | Enables real LLM calls via the Portkey gateway. Without it, every agent uses deterministic mocks — the app still runs. |
| `PORTKEY_BASE_URL` | Optional | Defaults to `https://portkey.bain.dev/v1`. |
| `PORTKEY_MODEL_CHAT` | Optional | Chat model id. Default `@personal-openai/gpt-5.4`. |
| `PORTKEY_MODEL_CODEX` | Optional | Code / structured-response model id. |
| `NEWS_API_KEY` | Optional | Enables `/api/news/summarize` against real headlines. |
| `SECRET_KEY` | Optional | Flask secret. Default `dev-secret`. |
| `JWT_SECRET_KEY` | Optional | JWT signing secret. Default `dev-jwt-secret`. |
| `PORT` | Optional | Backend port. Default `5000`. |
| `FRONTEND_ORIGIN` | Optional | CORS origin. Default `http://localhost:5173`. |
| `RAG_*_INDEX`, `DATA_*` | Optional | Paths to prebuilt FAISS indexes and CSVs — see `config.py`. |
| `UPLOAD_DIR` | Optional | Fraud upload directory. Default `backend/uploads`. |

> 💡 **No key? No problem.** If `PORTKEY_API_KEY` is empty, `llm_service` falls back to a deterministic mock so the app is **always demoable.**

---

## 📡 API Reference

All endpoints (except `/api/auth/*` and `/api/health`) require a **JWT bearer token** — the frontend `api/client.ts` handles this automatically.

<details>
<summary><b>🎯 Debt Escape Planner (flagship)</b></summary>

<br/>

**`POST /api/debt/plan`**

```json
{
  "debts": [
    { "name": "HDFC card", "kind": "credit_card", "balance": 85000, "apr": 38, "min_payment": 4250 },
    { "name": "ICICI card", "kind": "credit_card", "balance": 42000, "apr": 34, "min_payment": 2100 },
    { "name": "Bajaj PL",   "kind": "personal_loan", "balance": 180000, "apr": 15, "min_payment": 6800 }
  ],
  "monthly_budget": 20000,
  "consolidation_apr_pct": 12,
  "consolidation_term_months": 48
}
```

Response *(abbreviated)*:

```json
{
  "ok": true,
  "summary": {
    "total_balance": 307000,
    "weighted_apr_pct": 23.97,
    "monthly_budget": 20000,
    "monthly_minimum_required": 13150,
    "num_debts": 3
  },
  "recommended_strategy": "avalanche",
  "rationale": "Avalanche saves the most interest. It's the mathematically optimal choice.",
  "strategies": {
    "avalanche": { "months": 19, "total_interest": 53467.29, "payoff_dates": {"HDFC card": 9}, "monthly_totals": [] },
    "snowball":  { "months": 19, "total_interest": 54609.91, "payoff_dates": {"ICICI card": 6}, "monthly_totals": [] }
  },
  "toxic_debts": [{ "name": "HDFC card", "apr": 38.0, "reasons": [], "severity": "toxic" }],
  "consolidation": { "eligible": true, "recommend": false, "estimated_savings": -45033.65 },
  "coach_message": "..."
}
```

If `monthly_budget` is below the interest-plus-minimums threshold, the response returns `ok: false, error: "budget_too_low"` with the minimum viable amount so the UI can nudge the slider.

**`POST /api/debt/negotiate`**

```json
{ "debt": { "name": "HDFC card", "balance": 85000, "apr": 38, "kind": "credit_card" }, "situation": "" }
```

Returns a phone script plus 3–4 concrete asks and a target APR to negotiate down to.

**`GET /api/debt/tips`** — verified static guidance, useful offline.

</details>

<details>
<summary><b>📚 Other endpoints</b></summary>

<br/>

See `ARCHITECTURE.md` for the full notebook → endpoint mapping. Highlights:

- `POST /api/auth/signup` · `POST /api/auth/login`
- `GET /api/user/profile` · `PATCH /api/user/profile`
- `POST /api/advisor/query` · `POST /api/advisor/loan` · `GET /api/advisor/mutual-fund`
- `POST /api/loan/predict` · `POST /api/loan/credit-score`
- `GET /api/portfolio/insights` · `POST /api/portfolio/holding`
- `POST /api/stock/analyze`
- `GET /api/news/summarize?q=...`
- `POST /api/fraud/analyze` *(multipart form)*
- `GET /api/education/modules` · `GET /api/education/progress`
- `POST /api/chatbot/message`

</details>

---

## 📁 Repository Structure

<details>
<summary><b>Click to expand the full tree</b></summary>

<br/>

```
fAInance-GEN-AI-financial-platform/
├── README.md                          this file
├── ARCHITECTURE.md                    LangGraph + notebook mapping (deep dive)
│
├── backend/                           Flask + LangGraph API
│   ├── app.py                         Flask entry, registers all blueprints
│   ├── config.py                      env-driven config (Portkey, RAG paths, uploads)
│   ├── requirements.txt               core deps
│   ├── requirements-optional.txt      faiss, sentence-transformers, shap, lime, yfinance
│   │
│   ├── routes/                        Flask blueprints (one per feature)
│   │   ├── auth.py                    /api/auth       signup / login / me
│   │   ├── user.py                    /api/user       profile CRUD
│   │   ├── debt.py                    /api/debt       FLAGSHIP: plan, negotiate, tips
│   │   ├── advisor.py                 /api/advisor    RAG advisor
│   │   ├── loan.py                    /api/loan       predict + credit-score
│   │   ├── portfolio.py               /api/portfolio  holdings + insights
│   │   ├── stock.py                   /api/stock      quote + analysis
│   │   ├── news.py                    /api/news       headlines + summary
│   │   ├── fraud.py                   /api/fraud      document analysis
│   │   ├── education.py               /api/education  modules + progress
│   │   └── chatbot.py                 /api/chatbot    conversational agent
│   │
│   ├── services/                      pure logic (no Flask deps)
│   │   ├── debt_service.py            FLAGSHIP: avalanche/snowball sim, toxic
│   │   │                              detection, consolidation math, script gen
│   │   ├── llm_service.py             Portkey (Bain gateway) with mock fallback
│   │   ├── rag_service.py             FAISS retriever
│   │   ├── ml_service.py              loan/credit-score/card/investment models
│   │   ├── fraud_service.py           EXIF + perceptual hash + ELA
│   │   ├── stock_service.py           yfinance wrapper
│   │   ├── news_service.py            NewsAPI client
│   │   └── faq_service.py             TF-IDF BankFAQs retriever
│   │
│   ├── agents/                        LangGraph specialists (orchestrator + agents)
│   │   ├── orchestrator.py            StateGraph wiring
│   │   ├── router_agent.py            intent classification
│   │   ├── advisor_agent.py           loan / card / investment / mutual / budget
│   │   ├── explainability_agent.py    SHAP-style attributions + plain-English
│   │   ├── portfolio_agent.py         snapshot + drift + commentary
│   │   ├── stock_agent.py             yfinance + LLM narrative
│   │   ├── news_agent.py              NewsAPI + summarization
│   │   ├── fraud_agent.py             scam advice + document forensics
│   │   ├── education_agent.py         module recommendations
│   │   ├── chatbot_agent.py           FAQ-augmented chat
│   │   └── state.py                   shared AgentState schema
│   │
│   ├── models/store.py                thread-safe in-memory store (profiles, history)
│   ├── utils/                         hashing, validators
│   ├── data/                          learning_modules.json, memes.json, BankFAQs.csv
│   └── uploads/                       runtime fraud-doc uploads (gitignored)
│
├── frontend/                          React + Vite + Tailwind
│   ├── package.json                   dev/build/preview/lint scripts
│   ├── vite.config.js                 proxies /api → localhost:5000
│   ├── tsconfig.json                  TS with allowJs
│   │
│   └── src/
│       ├── App.tsx                    router + AuthProvider
│       ├── main.tsx                   ReactDOM root
│       ├── index.css                  Tailwind primitives + card/chip/btn helpers
│       │
│       ├── api/
│       │   ├── client.ts              axios instance + JWT interceptor
│       │   └── types.ts               shared TS types for all endpoints
│       │
│       ├── context/
│       │   ├── AuthContext.tsx        JWT auth state
│       │   └── LanguageContext.jsx    i18n language selection
│       │
│       └── components/
│           ├── Navbar.tsx             top nav with links to every feature
│           └── Pages/
│               ├── LandingPage.tsx    marketing landing
│               ├── LoginPage.tsx      login form
│               ├── SignupPage.tsx     signup + Three.js background
│               ├── ProfilePage.tsx    user profile
│               ├── HomePage.tsx       dashboard with flagship debt hero
│               └── AI/
│                   ├── DebtPage.tsx       FLAGSHIP: Debt Escape Planner
│                   ├── AdvisorPage.tsx    AI advisor Q&A
│                   ├── LoanPage.tsx       loan predictor + SHAP explanations
│                   ├── PortfolioPage.tsx  portfolio insights
│                   ├── StockPage.tsx      stock agent
│                   ├── NewsPage.tsx       financial news summarizer
│                   ├── FraudPage.tsx      fraud shield
│                   ├── EducationPage.tsx  gamified learning
│                   ├── ChatbotPage.tsx    conversational agent
│                   └── SettingsPage.tsx   profile settings
│
└── (reference)                        original Jupyter notebooks kept for reference
```

</details>

---

## 🎨 Design Principles

- 🧱 **Route/service separation.** `routes/*.py` handles HTTP (parsing, auth, status codes); `services/*.py` holds pure business logic with zero Flask imports — testable and reusable anywhere.
- 🪫 **Graceful LLM degradation.** Every AI call flows through `llm_service.py`, which mocks deterministically when no key is set — the app is never blocked on external credentials.
- 🛡️ **Guardrailed simulation math.** The debt simulator caps at a 600-month horizon, flags debts that can never be paid off at the minimum, and only recommends consolidation when savings are real.
- 🔗 **Typed frontend/backend contract.** `frontend/src/api/types.ts` mirrors backend response shapes so feature pages stay in sync with the API.
- 🔌 **Swap-friendly persistence.** `models/store.py` is an in-memory stand-in for a production database — routes and services never touch storage directly.

---

## 🛠️ Contributing

Adding a new feature is a five-step pattern:

1. Add `services/<name>_service.py` for the logic *(no Flask imports)*.
2. Add a `routes/<name>.py` blueprint and register it in `app.py`.
3. Add typed API surface in `frontend/src/api/types.ts`.
4. Build the page under `frontend/src/components/Pages/AI/`.
5. Keep AI calls behind the mock-friendly `llm_service.chat()` so the app stays demoable without keys.

Pull requests are welcome! 🙌

---

<div align="center">

### ⭐ If fAInance helped you, drop a star!

*Built with 💰 and a lot of ☕ to make financial freedom accessible to everyone.*

<br/>

![Made with Python](https://img.shields.io/badge/Made%20with-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Powered by LangGraph](https://img.shields.io/badge/Powered%20by-LangGraph-1C3C3C?style=flat-square&logo=langchain&logoColor=white)

</div>
