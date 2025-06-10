from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from model import load_model, generate_completion

app = FastAPI()
tokenizer, model = load_model()

class CodeRequest(BaseModel):
    code: str

@app.post("/complete")
def complete_code(request: CodeRequest):
    try:
        output = generate_completion(request.code, tokenizer, model)
        return {"completion": output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
