from fastapi import FastAPI, Request
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

app = FastAPI()

# Load model + tokenizer once at startup
tokenizer = AutoTokenizer.from_pretrained("codeparrot/codeparrot-small")
model = AutoModelForCausalLM.from_pretrained("codeparrot/codeparrot-small")
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

    # Extract newly generated tokens only
    new_tokens = outputs[0][inputs.shape[-1]:]
    completion = tokenizer.decode(new_tokens, skip_special_tokens=True)

    # Truncate completion after first newline for cleaner output
    completion = completion.split('\n')[0]

    return {"completion": completion}
