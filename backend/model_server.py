from fastapi import FastAPI, Request
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

app = FastAPI()

# Load model + tokenizer once at startup
model_name = "codeparrot/codeparrot-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
model.eval()

@app.post("/complete")
async def complete(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")

    # Tokenize input
    inputs = tokenizer(prompt, return_tensors="pt").input_ids

    # Generate new tokens
    with torch.no_grad():
        outputs = model.generate(
            inputs,
            max_new_tokens=20,
            do_sample=True,
            temperature=0.8,
            top_k=50,
            top_p=0.95
        )

    # Extract the newly generated text only
    new_tokens = outputs[0][inputs.shape[-1]:]
    completion = tokenizer.decode(new_tokens, skip_special_tokens=True)

    return {"completion": completion}
