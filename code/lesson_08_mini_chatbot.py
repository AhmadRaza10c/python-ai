"""Lesson 1.8: Rule-based chatbot for Sweet Crumbs bakery (example business)."""

BOT = "Sweet Crumbs Bot"
print(f"{BOT}: Hi! I can help with hours, prices, location and orders. Type 'bye' to exit.")

# Memory: the bot remembers the user's name for the whole chat
name = input(f"{BOT}: What is your name? ").strip().title()
if name == "":
    name = "friend"

print(f"{BOT}: Nice to meet you, {name}!")

count = 0
unanswered = 0
while True:
    message = input(f"{name}: ").strip().lower()
    count += 1

    # 1. Exit Rule
    if message == "bye" or message == "exit":
        print(f"{BOT}: Goodbye, {name}! Thanks for visiting.")
        break

    # 2. Empty Input
    elif message == "":
        print(f"{BOT}: Please type a question.")

    # 3. Complaints first, so an unhappy customer always reaches a human
    elif "refund" in message or "complaint" in message or "late" in message:
        print(f"{BOT}: Sorry about that. A manager will call you within 1 hour.")

    # 4. Opening Hours
    elif "hour" in message or "open" in message or "time" in message:
        print(f"{BOT}: We are open 9 am to 10 pm, every day.")

    # 5. Prices
    elif "price" in message or "cost" in message or "how much" in message:
        print(f"{BOT}: Cakes start at 1,500 PKR. Cupcakes are 250 PKR each.")

    # 6. Location
    elif "where" in message or "location" in message or "address" in message:
        print(f"{BOT}: We are on Main Boulevard, Lahore.")

    # 7. Orders & Delivery
    elif "order" in message or "delivery" in message:
        print(f"{BOT}: Order on WhatsApp. Delivery is free over 3,000 PKR.")

    # 8. Greetings (Exact match, because "hi" is hiding inside words like "this" and "which")
    elif message == "hi" or message == "hello" or message.startswith("salam"):
        print(f"{BOT}: Hello again, {name}! How can I help?")

    # 9. Fallback (Rule fails -> Prepare prompt for Module 2 LLM)
    else:
        unanswered += 1
        prompt = f"You are the friendly assistant of Sweet Crumbs bakery. Answer in 2 lines: {message}"
        print(f"{BOT}: I am not sure yet. In Module 2, an AI will answer using this prompt:")
        print(f"  {prompt}")

print("=" * 40)
print(f"Chat summary: {count} messages, {unanswered} unanswered.")