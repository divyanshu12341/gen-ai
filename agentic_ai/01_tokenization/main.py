import tiktoken

enc = tiktoken.get_encoding("o200k_base")
text = "Hey there my name is Divyanshu Jain "
tokens = enc.encode(text)
print("Tokens",tokens)
decoded = enc.decode(tokens)
print("Decoded token ",decoded)

# Vector embeddings gives semantic meanings to tokens 
# 