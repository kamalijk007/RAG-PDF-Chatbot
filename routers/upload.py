import pypdf
import chromadb
from fastapi import APIRouter, UploadFile, File
import io
from routers.db import collection

router = APIRouter()

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    # Read PDF
    contents = await file.read()
    reader = pypdf.PdfReader(io.BytesIO(contents))
    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text()
    
    # Chunk it
    chunks = []
    for i in range(0, len(full_text), 150):
        chunks.append(full_text[i:i+150])
    
    # Store in ChromaDB

    collection.add(
        documents=chunks,
        ids=[f"chunk_{i}" for i in range(len(chunks))]
    )
    
    return {"message": f"Stored {len(chunks)} chunks successfully"}