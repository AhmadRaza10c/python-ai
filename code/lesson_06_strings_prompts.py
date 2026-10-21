"""Lesson 1.6: Prompt Cleaner - cleans, measures and safely sizes a customer question."""

raw_name = input("Your name: ")
raw_question = input("Your question: ")

# Why: strip() removes extra spaces and title()/capitalize() fix random capitals,
# so the AI always receives a tidy name and question
clean_name = raw_name.strip().title()
clean_question = raw_question.strip().capitalize()

# Stretch: hide a bad word before the prompt is built
clean_question = clean_question.replace("stupid", "***")

characters = len(clean_question)

# Why: about 4 characters = 1 token, so this is a quick size estimate before paying an AI
estimated_tokens = round(characters / 4)

# Why: lower() first, so "Python", "PYTHON" and "python" are all found
mentions_python = "python" in clean_question.lower()

# Why: slicing to 150 characters stops one huge question from becoming an expensive prompt
short_question = clean_question[:150]

prompt = f"""You are a friendly Python tutor.
Greet {clean_name} by name and answer in 3 short lines.
Question: {short_question}"""

# Stretch: estimated cost with 2 decimals (example price 0.5 PKR per 1K tokens)
estimated_cost = estimated_tokens / 1000 * 0.5

print("=" * 40)
print(f"Cleaned question: {clean_question}")
print(f"Characters: {characters}, about {estimated_tokens} tokens")
print(f"Mentions Python: {mentions_python}")
print(f"Estimated cost: {estimated_cost:.2f} PKR")
print("=" * 40)
print(prompt)