"""Lesson 1.5: AI Model Profile Card with a cost estimate."""

# Why: one variable per fact, so the card is easy to update when the model changes
model_name = "llama3.2"
context_window = 128000
price_per_1k_pkr = 0.5
runs_locally = True

print("--- AI Model Profile Card ---")
print(f"Model: {model_name} {type(model_name)}")
print(f"Context window: {context_window} tokens {type(context_window)}")
print(f"Price per 1K tokens: {price_per_1k_pkr} PKR {type(price_per_1k_pkr)}")
print(f"Runs locally: {runs_locally} {type(runs_locally)}")

# Why: input() always returns text, so we convert it with int() before doing maths
tokens_per_chat = int(input("Tokens per chat: "))

# Why: round() keeps the cost short and readable for the client
estimated_cost = round(tokens_per_chat / 1000 * price_per_1k_pkr, 2)
print(f"Tokens per chat: {tokens_per_chat}")
print(f"Estimated cost: {estimated_cost} PKR")

# Stretch: monthly cost for 30 days
chats_per_day = int(input("Chats per day: "))
monthly_cost = round(tokens_per_chat / 1000 * price_per_1k_pkr * chats_per_day * 30, 2)
print(f"Estimated monthly cost (30 days): {monthly_cost} PKR")