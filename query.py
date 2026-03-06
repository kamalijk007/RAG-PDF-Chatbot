import chromadb
import requests
from local_llm import ask_kobold


def user_query(user_question):
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_or_create_collection("bio_docs")
    results = collection.query(query_texts=[user_question], n_results=4)
    context = " ".join(results['documents'][0])
    answer = ask_kobold(user_question, context)
    return answer