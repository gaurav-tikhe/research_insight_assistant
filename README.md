# 🧠 Research Insight Assistant

> A modular, production-ready RAG pipeline for semantic research paper analysis — built with Kedro, LangChain, and FAISS.

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white)
![Kedro](https://img.shields.io/badge/Kedro-Pipeline-FFC900?style=flat-square&logo=kedro&logoColor=black)
![LangChain](https://img.shields.io/badge/LangChain-Framework-1C3C3C?style=flat-square&logo=langchain&logoColor=white)
![FAISS](https://img.shields.io/badge/FAISS-Vector%20DB-0467DF?style=flat-square)
![Status](https://img.shields.io/badge/Status-In%20Progress-orange?style=flat-square)

---

## 📌 Overview

**Research Insight Assistant** is an end-to-end pipeline that ingests research papers (PDFs), processes them into semantically meaningful chunks, generates embeddings, and enables intelligent retrieval using a RAG (Retrieval-Augmented Generation) backbone.

The system is designed for modularity and production-readiness — each stage is an independently testable Kedro pipeline.

---

## 🏗️ Architecture

```
PDFs
 └──▶ Text Extraction
        └──▶ Chunking (with overlap)
               └──▶ Embeddings (Sentence Transformers)
                      └──▶ FAISS Vector Store
                             └──▶ Query Interface
                                    └──▶ Semantic Retrieval
```

---

## ⚙️ Tech Stack

| Layer | Tool |
|---|---|
| Pipeline Orchestration | [Kedro](https://kedro.org/) |
| LLM Framework | [LangChain](https://www.langchain.com/) |
| Vector Database | [FAISS](https://faiss.ai/) |
| Embeddings | [Sentence Transformers](https://www.sbert.net/) |
| Language | Python 3.12 |

---

## 📂 Project Structure

```
src/research_insight_assistant/
├── pipelines/
│   ├── data_ingestion/     # PDF reading & raw text extraction
│   ├── chunking/           # Text splitting with overlap
│   ├── embedding/          # Vector generation & FAISS indexing
│   └── retrieval/          # Semantic query & top-k chunk retrieval
```

---

## 🔄 Pipeline Breakdown

### 1. 📥 Data Ingestion
- Reads PDF files from the data catalog
- Extracts raw text content for downstream processing

### 2. ✂️ Chunking
- Splits extracted text into smaller, coherent segments
- Applies configurable overlap to preserve cross-chunk context

### 3. 🔢 Embedding
- Converts text chunks into dense vector embeddings via Sentence Transformers
- Stores all vectors in a FAISS index for fast similarity search

### 4. 🔍 Retrieval
- Accepts a natural language user query
- Returns the top-k most semantically relevant chunks from the index

---

## ▶️ Getting Started

### Prerequisites

- Python 3.12+
- [`uv`](https://github.com/astral-sh/uv) (recommended) or `pip`

### Installation

```bash
git clone https://github.com/your-username/research-insight-assistant.git
cd research-insight-assistant
uv sync
```

### Run the Full Pipeline

```bash
uv run kedro run
```

### Run a Specific Pipeline

```bash
uv run kedro run --pipeline data_ingestion
uv run kedro run --pipeline chunking
uv run kedro run --pipeline embedding
uv run kedro run --pipeline retrieval
```

---

## 💬 Example Query

```python
query = "Explain the main contribution of the paper"
```

**Output:**

```
retrieved_chunks → [
  "This paper proposes a novel attention mechanism...",
  "The key contribution is a 40% reduction in inference latency...",
  "We demonstrate state-of-the-art results on three benchmarks..."
]
```

---

## 📊 Current Status

| Feature | Status |
|---|---|
| End-to-end data pipeline | ✅ Complete |
| Semantic search via FAISS | ✅ Complete |
| Modular Kedro pipelines | ✅ Complete |
| LLM-based answer generation | 🔄 In Progress |
| Prompt engineering | 🔄 In Progress |
| API / UI layer | 🔄 In Progress |
| LLMOps (monitoring & evaluation) | 🔄 In Progress |

---

## 🔮 Roadmap

- [ ] Integrate LLM for answer generation (Ollama / HuggingFace)
- [ ] Build prompt templates for context-grounded responses
- [ ] Add RAG evaluation metrics (faithfulness, relevance, groundedness)
- [ ] Implement self-healing RAG with feedback loops
- [ ] Deploy via FastAPI or HuggingFace Spaces
- [ ] Add LLMOps observability (LangSmith / Arize / Weights & Biases)

---

## 💡 Key Learnings

- Designing modular, testable ML pipelines with **Kedro**
- Building scalable RAG systems from scratch
- Working with **vector databases** and **dense embeddings**
- Structuring **production-ready ML projects** with clean separation of concerns

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to check the [issues page](https://github.com/your-username/research-insight-assistant/issues).

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<p align="center">Built with 🔬 curiosity and ⚙️ modularity</p>