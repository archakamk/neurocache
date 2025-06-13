from transformers import AutoTokenizer, AutoModelWithLMHead

def load_model():
    tokenizer = AutoTokenizer.from_pretrained("codeparrot/codeparrot-small")
    model = AutoModelWithLMHead.from_pretrained("codeparrot/codeparrot-small")
    model.eval()
    return tokenizer, model

def generate_completion(prompt, tokenizer, model, max_new_tokens=15):
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
    outputs = model.generate(**inputs, max_new_tokens=max_new_tokens, do_sample=True)
    full_output = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return full_output[len(prompt):].strip()
