from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("gpt2")

print(tokenizer.tokenize("I love AI"))
print(tokenizer.tokenize("Machine learning is powerful."))
print(tokenizer.tokenize("I LOVE ai"))
print(tokenizer.tokenize("Hello, world! How are you?"))
print(tokenizer.tokenize("I have 25 apples and 3 bananas."))
print(tokenizer.tokenize("Bugun 7-darsni tugatdik"))
tokens = tokenizer.tokenize("I love AI")
for t in tokens:
    print(repr(t), "->", repr(tokenizer.convert_tokens_to_string([t])))
