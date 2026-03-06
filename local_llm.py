import requests

def ask_kobold(question, context):
    prompt = f"""Use the following context to answer the question.

Context: {context}

Question: {question}"""

    response = requests.post(
        "http://127.0.0.1:5001/v1/chat/completions",
        json={
            "model": "kobold",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
    )
    
    return response.json()['choices'][0]['message']['content']