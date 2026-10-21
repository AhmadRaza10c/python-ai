"""Lesson 1.5: AI Model Profile Card and Cost Estimator."""

# Model Profile Variables (4 Core Types)
model_name: str = "gemini-4-argon"
max_tokens: int = 500
temperature: float = 0.7
is_streaming: bool = False

# Price per 1,000 tokens (PKR)
price_per_1k_tokens: float = 0.50   

# 2. Print Profile Card with Values and Types
print("=== AI Model Profile Card ===")
print(f"Model Name   : {model_name} | Type: {type(model_name)}")
print(f"Max Tokens   : {max_tokens} | Type: {type(max_tokens)}")
print(f"Temperature  : {temperature} | Type: {type(temperature)}")
print(f"Streaming    : {is_streaming} | Type: {type(is_streaming)}")
print("=============================\n")

# 3. User Input & Cost Estimation

tokens_input = input("Enter tokens used in chat: ")
tokens_used = int(tokens_input)

# Cost formula: (tokens / 1000) * price_per_1k
estimated_cost = (tokens_used / 1000) * price_per_1k_tokens

print("\n--- Cost Breakdown ---")
print(f"Tokens Used    : {tokens_used}")
print(f"Estimated Cost : {round(estimated_cost, 2)} PKR")