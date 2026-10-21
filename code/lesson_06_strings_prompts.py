"""Lesson 1.6: Prompt Cleaner & Formatter for AI Models"""

# 1. User inputs (raw & messy)
raw_name = input("Enter your name: ")
raw_question = input("Enter your question: ")

# 2. Cleaning inputs
# .strip() removes outer spaces, .title() capitalizes each word
clean_name = raw_name.strip().title()
# .capitalize() makes only the first character uppercase
clean_question = raw_question.strip().capitalize()

# 3. Check if question mentions "python" (case-insensitive)
mentions_python = "python" in clean_question.lower()

# 4. Limit length & Token estimation
# Slice to maximum 150 characters
limited_question = clean_question[:150]
# Rule of thumb: ~4 characters = 1 token
estimated_tokens = round(len(limited_question) / 4)

# 5. Multi-line Prompt Template
final_prompt = f"""You are a professional AI tutor helping {clean_name}.
Provide a clear and concise answer in maximum 3 sentences.

User Question: {limited_question}"""

# 6. Displaying results
print("\n" + "=" * 45)
print("--- CLEANED SUMMARY ---")
print(f"User Name        : {clean_name}")
print(f"Original Length  : {len(clean_question)} characters")
print(f"Prompt Length    : {len(limited_question)} characters")
print(f"Estimated Tokens : ~{estimated_tokens}")
print(f"Mentions Python? : {mentions_python}")
print("=" * 45)
print("\n--- FINAL PROMPT SENT TO AI ---")
print(final_prompt)