from transformers import AutoTokenizer, AutoModelWithLMHead

tokenizer = AutoTokenizer.from_pretrained("codeparrot/codeparrot-small")
model = AutoModelWithLMHead.from_pretrained("codeparrot/codeparrot-small")

inputs = tokenizer("def hello_world():", return_tensors="pt")
outputs = model(**inputs)
