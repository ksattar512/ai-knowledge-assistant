# 🤖 Enterprise RAG Knowledge Assistant

## 🚀 Overview
Enterprise RAG Knowledge Assistant is a production-style Retrieval-Augmented Generation (RAG) starter architecture for building secure AI knowledge systems over business documents.

It is designed for enterprise use cases such as internal knowledge bases, policy assistants, document intelligence, customer support automation, and operational decision support.

---

## 🧠 Business Problem
Organizations often struggle with:

- Scattered documents across SharePoint, email, drives, portals, and local folders
- Slow knowledge discovery
- Repeated questions to operations/support teams
- Inconsistent answers across departments
- Lack of AI governance, auditability, and source traceability

---

## ⚙️ Solution
This project demonstrates a structured RAG system that:

- Ingests enterprise documents
- Chunks content for retrieval
- Generates embeddings
- Stores vectors in a searchable vector database
- Retrieves the most relevant context
- Generates grounded AI answers
- Returns source references for traceability

---

## 🏗️ Architecture

```text
[User / App / Bot]
        ↓
[FastAPI Query Endpoint]
        ↓
[Security + Request Validation]
        ↓
[Retriever Service]
        ↓
[Vector Store]
        ↓
[Prompt Builder]
        ↓
[LLM Provider]
        ↓
[Grounded Answer + Sources]
```

---

## 📂 Repository Structure

```text
enterprise-rag-knowledge-assistant/
│── app/
│   ├── api/
│   ├── core/
│   ├── models/
│   ├── security/
│   ├── services/
│   ├── utils/
│   └── main.py
│── data/
│   ├── documents/
│   └── vectorstore/
│── docs/
│── tests/
│── .env.example
│── requirements.txt
│── Dockerfile
│── docker-compose.yml
│── README.md
```

---

## 🛠️ Tech Stack
- Python
- FastAPI
- RAG Architecture
- Vector Search
- LLM Provider Abstraction
- Docker-ready deployment structure

---

## ⚡ Quick Start

### 1. Create virtual environment
```bash
python -m venv venv
```

### 2. Activate environment
Windows:
```bash
venv\Scripts\activate
```

Linux/Mac:
```bash
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment
Copy `.env.example` to `.env`.

### 5. Add documents
Place `.txt` files inside:

```text
data/documents/
```

A sample document is already included.

### 6. Build vector index
```bash
python -m app.services.document_loader
```

### 7. Run API
```bash
uvicorn app.main:app --reload
```

---

## 🔎 API Example

### Query
```http
POST /api/query
```

```json
{
  "question": "What is the company policy for document approvals?",
  "top_k": 4
}
```

### Response
```json
{
  "answer": "Grounded answer generated from retrieved context.",
  "sources": [
    {
      "source": "sample-policy.txt",
      "score": 0.87
    }
  ]
}
```

---

## 🧩 Enterprise Features Included
- Config-driven architecture
- API-first design
- Source-aware answers
- Vector search abstraction
- LLM provider abstraction
- Security middleware placeholder
- Docker deployment support
- Extendable for SharePoint, Teams bots, SaaS apps, and MS 365 automation

---

## 🔮 Future Enhancements
- SharePoint connector
- PDF/DOCX ingestion
- Azure OpenAI integration
- Role-based document access
- Admin dashboard
- Teams bot integration
- Multi-tenant SaaS mode
- Evaluation and hallucination scoring
- Audit logging

---

## 👤 Author
Built as part of an enterprise AI architecture portfolio covering RAG, LLM apps, SaaS, bots, MS 365, blockchain, and multi-cloud systems.
