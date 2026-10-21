"""Lesson 1.7: Smart Model Router with Cost Estimation and Warnings"""

# 1. User inputs
task = input("Enter task type (code / private / chat): ").strip().lower()
tokens = int(input("Enter estimated tokens: "))

# 2. Routing logic & Pricing (PKR per 1,000 tokens)
if task == "private":
    model = "llama3.2 (Local via Ollama)"
    price_per_1k = 0.0 
elif task == "code":
    model = "claude-3-5-sonnet (Cloud - High Capability)"
    price_per_1k = 1.5
else:
    model = "small-cloud-model (Cloud - Cost-effective)"
    price_per_1k = 0.3 

# 3. Guardrail / Length Warning
if tokens > 4000:
    warning = "⚠️ Warning: Very long request! Consider shortening to save costs."
elif tokens <= 0:
    warning = "⚠️ Warning: Token count must be greater than 0."
else:
    warning = "✅ Token length is optimal."

# 4. Cost calculation
estimated_cost = (tokens / 1000) * price_per_1k

# 5. Output Card
print("\n" + "=" * 45)
print("--- SMART ROUTER DECISION ---")
print(f"Task Selected  : {task}")
print(f"Tokens Count   : {tokens:,}")
print(f"Assigned Model : {model}")
print(f"Estimated Cost : {round(estimated_cost, 2)} PKR")
print(f"Status Note    : {warning}")
print("=" * 45)
