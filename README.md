# RAG PDF Chatbot

A Retrieval-Augmented Generation (RAG) system that answers questions from any PDF document using a local LLM. Built with FastAPI, ChromaDB, and KoboldCpp.

---

## What It Does

You give it a PDF. You ask it a question. It finds the answer — grounded in your actual document, no hallucinations, no guessing.

Instead of feeding an entire document to an LLM (which is slow and expensive), this system:
1. Breaks the PDF into small chunks
2. Stores those chunks in a vector database (ChromaDB)
3. When you ask a question, it finds the most relevant chunks using semantic search
4. Passes only those chunks to the LLM as context
5. Returns a focused, accurate answer

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| API | FastAPI |
| Vector Database | ChromaDB (persistent, local) |
| PDF Parsing | PyPDF |
| LLM | KoboldCpp (local, OpenAI-compatible endpoint) |
| Validation | Pydantic |

---

## Project Structure

```
RAG/
├── ingest.py       # Read PDF, chunk text, store in ChromaDB (run once)
├── query.py        # Search ChromaDB + call local LLM
├── local_llm.py    # ask_kobold() — sends prompt to KoboldCpp
├── main.py         # FastAPI app with POST endpoint
├── data/
│   └── your_file.pdf
└── chroma_db/      # Persistent vector store (auto-generated)
```

---

## Requirements

- Python 3.11 (ChromaDB is not compatible with Python 3.12+)
- [KoboldCpp](https://github.com/LostRuins/koboldcpp) running locally on port `5001`
- A PDF file to query

---

## Setup

**1. Clone the repo**
```bash
git clone https://github.com/your-username/rag-pdf-chatbot
cd rag-pdf-chatbot
```

**2. Create a Python 3.11 virtual environment**
```bash
py -3.11 -m venv rag_venv
rag_venv\Scripts\activate      # Windows
# source rag_venv/bin/activate  # Linux/Mac
```

**3. Install dependencies**
```bash
pip install fastapi uvicorn pypdf chromadb requests
```

**4. Add your PDF**

Place your PDF inside the `data/` folder and update the filename in `ingest.py`:
```python
reader = pypdf.PdfReader('data/your_file.pdf')
```

**5. Run the ingestion script** (once per document)
```bash
python ingest.py
```

This reads your PDF, splits it into 300-character chunks, and stores them in ChromaDB.

**6. Start KoboldCpp**

Make sure KoboldCpp is running locally with a model loaded. It should be accessible at:
```
http://127.0.0.1:5001/v1/chat/completions
```

**7. Start the FastAPI server**
```bash
uvicorn main:app --reload
```

---

## Usage

### Via Swagger UI
Open your browser at `http://127.0.0.1:8000/docs` and use the interactive API docs.

### Via curl
```bash
curl -X POST "http://127.0.0.1:8000/" \
  -H "Content-Type: application/json" \
  -d '{"user_prompt": "What is the main topic of the document?"}'
```

### Example Response
```json
{
  "answer": "Based on the document, the main topic is..."
}
```

---

## How It Works (Pipeline)

```
PDF File
   ↓
PyPDF (text extraction)
   ↓
Chunking (300 chars per chunk)
   ↓
ChromaDB (vector storage + semantic search)
   ↓
Top 4 relevant chunks retrieved
   ↓
KoboldCpp LLM (answer generation)
   ↓
FastAPI response
```

---

## Notes

- **Chunk size:** Currently set to 300 characters. Smaller chunks improve precision for specific facts. Larger chunks give more context for broad questions.
- **n_results:** Currently retrieves top 4 chunks. Increase for broader coverage, decrease to reduce noise.
- **Stale data:** If you update your PDF, delete the `chroma_db/` folder and re-run `ingest.py` to rebuild the index.
- **Local LLM:** This project uses KoboldCpp for fully local, private inference. No data is sent to external APIs.

---

## Built By

Kamal Khan — Backend & AI Engineer  
[linkedin.com/in/kamal-khan-ai](https://linkedin.com/in/kamal-khan-ai)
