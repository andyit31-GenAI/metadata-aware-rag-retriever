# metadata-aware-rag-retriever
LangChain-compatible metadata-aware retriever for RAG pipelines. Supports LLM-driven filtering, fallback logic, and enhanced grounding using ChromaDB.

# SmartDocRAG Metadata-Aware Retriever

This is an open-source component from my production-grade Generative AI system, **SmartDocRAG**. It enhances **Retrieval-Augmented Generation (RAG)** pipelines by adding **metadata-aware filtering**, **LLM-driven query understanding**, and **fallback logic** for vague or underspecified questions.

Designed for use with **LangChain** and **ChromaDB**, this retriever improves the **precision and grounding** of LLM responses in enterprise scenarios such as claims processing, document summarization, and policy Q&A.

---

## Features

- LLM-driven metadata extraction from user queries (e.g., "policy type", "urgency", "region")
- Dynamic filtering over metadata fields in ChromaDB documents
- Fallback logic if filters return zero results (e.g., remove filters, retry)
- Designed to plug into LangChain’s retriever stack or used independently
- Clean, modular codebase with examples and test inputs

---

## File Structure

```bash
smartdocrag-retriever/
│
├── retriever.py          # Main retriever logic using Chroma + metadata filters
├── metadata_utils.py     # Extracts metadata filters from queries using an LLM
├── sample_metadata.json  # Dummy metadata values for testing
├── test_queries.json     # Sample natural language inputs + expected filters
└── README.md             # You're here!

