from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

def ask_gemini(question: str, context: str) -> str:
    client = genai.Client(api_key=os.getenv("API_KEY"))
    prompt = f"Answer the question based on this context:\n\n{context}\n\nQuestion: {question}"
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )
    return response.text