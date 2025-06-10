from transformers import AutoTokenizer, AutoModelForCausalLM

def load_model():
    tokenizer = AutoTokenizer.from_pretrained("codeparrot/codeparrot-small")
    model = AutoModelForCausalLM.from_pretrained("codeparrot/codeparrot-small")
    model.eval()
    return tokenizer, model

def generate_completion(code, tokenizer, model):
    inputs = tokenizer(code, return_tensors="pt", truncation=True, max_length=512)
    outputs = model.generate(**inputs, max_new_tokens=20)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
