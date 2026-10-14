"""Module 1 - Lesson 1.4: Business Prompt Builder
Why this file exists: To dynamically gather user input and build 
ready-to-use AI prompts for automated client solutions."""

name = input("Your name: ")
business = input("Business type: ")
problem = input("Biggest problem: ")
budget_input = input("Monthly budget in PKR: ")
budget = int(budget_input)

print(f"\nWelcome, {name}!")
print("--- Your AI Prompt ---")

prompt = f"Suggest 3 AI solutions for a {business} that struggles with {problem}. Budget: {budget} PKR per month."
print(prompt)