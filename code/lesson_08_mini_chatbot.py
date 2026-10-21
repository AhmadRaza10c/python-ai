"""Lesson 1.8: Rule-based chatbot for Sweet Crumbs bakery (example business)."""

BOT = "Sweet Crumbs Bot"
print(f"{BOT}: Hi! Ask about hours, prices, location or orders. Type 'bye' to exit.")

# Why: the name is asked ONCE before the loop, so the bot remembers it for the whole chat
name = input(f"{BOT}: What is your name? ").strip().title()
if name == "":
    name = "Friend"

count = 0
unanswered = 0
complaints = 0

while True:
    message = input(f"{name}: ").strip().lower()
    count += 1

    # Why: spaces around the text let us match whole words only,
    # so " late " is found in "my order is late" but NOT inside "chocolate"
    clean_text = message.replace("?", "").replace(".", "").replace(",", "").replace("!", "")
    padded = " " + clean_text + " "

    if message == "bye":
        print(f"{BOT}: Take care, {name}!")
        break
    elif message == "":
        print(f"{BOT}: Please type a question.")
    # Why: handover and complaints come first, so an unhappy customer always reaches a human
    elif message == "agent" or message == "human":
        print(f"{BOT}: Connecting you to a human...")
        break
    elif " refund " in padded or " complaint " in padded or " late " in padded:
        complaints += 1
        print(f"{BOT}: Sorry about that. A manager will call you within 1 hour.")
    elif "hour" in message or "open" in message or "timing" in message or " time " in padded:
        print(f"{BOT}: We are open 9 am to 10 pm, every day.")
    elif "price" in message or "cost" in message or "how much" in message:
        print(f"{BOT}: Cakes start at 1,500 PKR. Cupcakes are 250 PKR each.")
    elif "where" in message or "location" in message or "address" in message:
        print(f"{BOT}: We are on Main Boulevard, Lahore.")
    elif "order" in message or "delivery" in message:
        print(f"{BOT}: Order on WhatsApp. Delivery is free over 3,000 PKR.")
    # Why: short words like "hi" are checked with == / startswith, because "hi" hides inside "which"
    elif message == "hi" or message == "hello" or message.startswith("salam"):
        print(f"{BOT}: Hello {name}! How can I help?")
    else:
        unanswered += 1
        question = message.capitalize()[:150]
        print(f"{BOT}: I am not sure yet. In Module 2, an AI will answer: "
              f"You are the friendly assistant of Sweet Crumbs bakery. "
              f"Answer in 2 lines: {question}")

print("=" * 40)
print(f"Chat summary: {count} messages, {unanswered} unanswered.")
print(f"Complaints received: {complaints}")