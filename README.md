🧠 Research Insight Assistant (RAG Pipeline with Kedro)

A modular Research Paper Analysis System that processes PDFs and enables semantic search over their contents using a Retrieval-Augmented Generation (RAG) backbone.

🚀 Project Overview

This project builds an end-to-end pipeline to:

Ingest research papers (PDFs)
Extract and preprocess text
Split content into meaningful chunks
Generate embeddings
Store vectors in FAISS
Retrieve relevant context for user queries


🏗️ Architecture
PDFs -> Text Extraction -> Chunking -> Embeddings -> FAISS Vector Store -> Query -> Semantic Retrieval


⚙️ Tech Stack
Pipeline Orchestration: Kedro
LLM Framework: LangChain
Vector Database: FAISS
Embeddings: Sentence Transformers
Language: Python 3.12


📂 Project Structure
src/research_insight_assistant/
    pipelines/
        data_ingestion/
        chunking/
        embedding/
        retrieval/

Each pipeline is modular and independently testable.

🔄 Pipelines
1. Data Ingestion
Reads PDF files
Extracts raw text
2. Chunking
Splits text into smaller chunks
Uses overlap for better context retention
3. Embedding
Converts text chunks into vector embeddings
Stores them in FAISS index
4. Retrieval
Accepts a user query
Returns top-k relevant chunks using semantic similarity
▶️ How to Run
uv run kedro run
📌 Example Query (Current Stage)
query: "Explain the main contribution of the paper"

Output:

retrieved_chunks → most relevant sections from the paper
🚧 Current Status

✅ Completed:

End-to-end data pipeline
Semantic search using FAISS
Modular Kedro pipelines

❌ In Progress:

LLM-based answer generation
Prompt engineering
API / UI layer
LLMOps (monitoring, evaluation)


🔮 Next Steps
- Integrate LLM (Ollama / HuggingFace)
- Generate answers from retrieved context
- Add evaluation + self-healing RAG
- Deploy via FastAPI / HuggingFace Spaces


💡 Key Learnings
- Designing modular ML pipelines with Kedro
- Building scalable RAG systems
- Working with vector databases and embeddings
- Structuring production-ready ML projects