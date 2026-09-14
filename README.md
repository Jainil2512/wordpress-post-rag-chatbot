# WordPress Custom Post Type RAG Chatbot

An intelligent Retrieval-Augmented Generation (RAG) terminal chatbot built using LangChain, LangGraph, Ollama, LLAMA3 model and ChromaDB. This application connects to a WordPress site via REST API, ingests custom post types into a local vector store, and provides context-aware answers to user queries directly in the terminal.

---

Features

- WordPress REST API Integration: Dynamically fetches posts, pages, and custom post types (CPTs) from any WordPress site.
- Local LLM & Embeddings via Ollama: Completely private and offline-capable language model execution (e.g., `llama3`, `mistral`, `nomic-embed-text`).
- Stateful Conversational Graphs: Managed using **LangGraph** to handle multi-turn conversations, query routing, and retrieval workflows smoothly.
- Fast Vector Storage: Powered by **ChromaDB** for efficient similarity search and document indexing.

# Architecture & Workflow

[ WordPress Site ]
│
▼ (REST API / CPTs)
[ Ingestion Pipeline ] ──► [ Text Splitter ] ──► [ Embeddings (Ollama) ]
│
▼
[ ChromaDB Vector Store ]
│
[ Terminal CLI User ] ◄───► [ LangGraph Agent ] ◄───────────┘


1. Ingestion: WordPress custom post types are pulled using the REST API (`/wp-json/wp/v2/<post-type>`).
2. Indexing: Extracted posts are split into chunks and embedded using Ollama embeddings before being stored in ChromaDB.
3. Retrieval & Response: When a user asks a question in the terminal, LangGraph queries ChromaDB for relevant content and passes it to the Ollama local LLM to generate an accurate response.

---

# Tech Stack

- **Frameworks**: [LangChain](https://www.langchain.com/), [LangGraph](https://www.langchain.com/langgraph)
- **Local LLM Runtime**: [Ollama](https://ollama.com/)
- **Vector Database**: [ChromaDB](https://www.trychroma.com/)
- **Data Source**: WordPress REST API
- **Language**: Python 3.10+

---

## Getting Started

# Prerequisites

1. Python: Ensure Python `3.10` or higher is installed.
2. Ollama: Download and install Ollama from [ollama.com](https://ollama.com/).
   - Pull your preferred LLM and embedding models:
     ```bash
     ollama pull llama3
     ollama pull nomic-embed-text
     ```
3. WordPress Site: Ensure your WordPress site has REST API enabled for your custom post types (`'show_in_rest' => true`).
