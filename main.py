from fastapi import FastAPI , Response
from pydantic import Field , ConfigDict , BaseModel
from query import user_query



app =FastAPI()

#Models

class Prompt_Base(BaseModel):
    user_prompt : str = Field(min_length=1)

#End-points
@app.post('/')
def user_prompts(data:Prompt_Base):
    results = user_query(data.user_prompt)
    return {"answer": results}

















