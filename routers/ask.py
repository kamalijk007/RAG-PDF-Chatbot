from fastapi import APIRouter
import chromadb
from pydantic import BaseModel
from routers.llm_response import ask_gemini
from routers.db import collection

class user_question(BaseModel):
    question: str

router = APIRouter()

@router.post("/ask")
def user_query(data: user_question):
    results = collection.query(query_texts=[data.question], n_results=8)
    context = " ".join(results['documents'][0])
    answer = ask_gemini(data.question, context)
    return answer