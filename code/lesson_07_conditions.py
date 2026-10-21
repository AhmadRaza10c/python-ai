"""Lesson 1.7: Smart Model Router - sends each task to the cheapest model that is good enough."""

# Why: strip().lower() so " Code " and "CODE" still work
task = input("Task (code / private / chat): ").strip().lower()
tokens = int(input("Estimated tokens: "))
paid_answer = input("Is this a paid user? (yes/no): ").strip().lower()

# Why: private data must stay on the computer, so it goes to the local model with price 0
if task == "code":
    model = "claude (cloud, strong at code)"
    price_per_1k = 0.8  # example price in PKR
elif task == "private":
    model = "llama3.2 (local, Ollama)"
    price_per_1k = 0
else:
    model = "small cloud model (cheap)"
    price_per_1k = 0.3

# Why: a long request costs more, so we warn the user before it is sent
if tokens > 4000:
    print("Warning: long request, consider shortening it.")
else:
    print("Length is fine.")

# Stretch: free users cannot send long requests (uses "and")
if paid_answer == "no" and tokens > 2000:
    print("Upgrade to send long requests.")

cost = tokens / 1000 * price_per_1k
print(f"Chosen model: {model}")
print(f"Estimated cost: {cost:.2f} PKR")