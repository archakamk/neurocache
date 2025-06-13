from fastapi import FastAPI
from pydantic import BaseModel
from model import load_model, generate_completion

app = FastAPI()
tokenizer, model = load_model()

class CodeRequest(BaseModel):
    code: str

@app.post("/complete")
async def complete_code(request: CodeRequest):
    completion = generate_completion(request.code, tokenizer, model)
    return {
        "completion": completion
    }