# RAG PDF Chatbot

A Retrieval-Augmented Generation (RAG) system that answers questions from any PDF document. Upload a PDF, ask a question, get an answer grounded in your document — no hallucinations, no guessing.

Built with FastAPI · ChromaDB · Gemini API · Python

---

## How It Works

1. **Upload** — Drop any PDF into the interface. The system extracts and chunks the text, then stores it as vector embeddings in ChromaDB.
2. **Ask** — Type any question about the document.
3. **Answer** — ChromaDB retrieves the most relevant chunks semantically, and Gemini generates an accurate, grounded answer.

```
PDF → Text Extraction (PyPDF) → Chunking → ChromaDB (Vector Store)
Question → Semantic Search → Relevant Chunks → Gemini API → Answer
```

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | FastAPI |
| Vector Database | ChromaDB |
| LLM | Google Gemini API |
| PDF Parsing | PyPDF |
| Frontend | HTML · CSS · JavaScript |

---

## Project Structure

```
RAG-PDF-Chatbot/
├── main.py                 # FastAPI app, routing, static files
├── requirements.txt        # Dependencies
├── routers/
│   ├── upload.py           # PDF upload + chunking + ChromaDB storage
│   ├── ask.py              # Semantic search + LLM query
│   └── llm_response.py     # Gemini API call
└── static/
    └── index.html          # Frontend UI
```

---

## Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/kamalijk007/RAG-PDF-Chatbot.git
cd RAG-PDF-Chatbot
```

### 2. Create a virtual environment (Python 3.11 recommended)
```bash
py -3.11 -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up your API key
Create a `.env` file in the root directory:
```
API_KEY=your_gemini_api_key_here
```
Get your free Gemini API key at [aistudio.google.com](https://aistudio.google.com)

### 5. Run the app
```bash
uvicorn main:app --reload
```

### 6. Open in browser
```
http://localhost:8000
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/upload` | Upload a PDF and store chunks in ChromaDB |
| POST | `/ask` | Ask a question, get an answer from the document |
| GET | `/docs` | Swagger UI — interactive API documentation |

---

## Notes

- Delete the `chroma_db/` folder before re-uploading a new PDF to avoid stale data
- Python 3.11 recommended — newer versions may cause ChromaDB compatibility issues
- Gemini API free tier is sufficient for testing and portfolio use

---

## Author

**Kamal Khan** — Backend & AI Engineer  
[linkedin.com/in/kamal-khan-ai](https://linkedin.com/in/kamal-khan-ai) · [github.com/kamalijk007](https://github.com/kamalijk007)
