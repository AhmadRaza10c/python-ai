"""AI Front Desk for Sweet Crumbs bakery (example business).

Answers common questions with free rules, gives exact price quotes (discount + delivery),
and turns every question it cannot answer into a cost-checked AI prompt.
Uses Module 1 tools only: no lists, dictionaries, for loops or functions.
"""

# Why: constants sit at the top, so the owner can change a price or fee in one place
BOT_NAME = "Sweet Crumbs Desk"
BUSINESS = "Sweet Crumbs bakery"
CUPCAKE_PRICE = 250
BROWNIE_PRICE = 300
CAKE_PRICE = 1500
BULK_MIN_QTY = 10
BULK_DISCOUNT = 0.10
DELIVERY_FEE = 200
FREE_DELIVERY_LIMIT = 3000
CLOUD_PRICE_PER_1K = 0.1  # example price in PKR per 1K tokens, not a real quote

print("=" * 50)
print("   Sweet Crumbs Desk: rules, quotes and AI-ready prompts")
print("=" * 50)
print("Ask anything, type /quote for a price, or bye to exit.")

# Why: the name is asked once, before the loop, so the desk remembers it for the whole chat
name = input(f"{BOT_NAME}: What is your name? ").strip().title()
if name == "":
    name = "Friend"

count = 0
answered = 0
unanswered = 0
quotes = 0
quoted_value = 0
complaints = 0
ai_cost = 0

while True:
    message = input(f"{name}: ").strip().lower()
    if message != "":
        count += 1

    # Why: spaces around the text match whole words only, so " late " is found
    # in "my order is late" but NOT inside "chocolate"
    clean_text = message.replace("?", "").replace(".", "").replace(",", "").replace("!", "")
    padded = " " + clean_text + " "

    if message == "":
        print(f"{BOT_NAME}: Please type a question.")
    elif message == "bye":
        print(f"{BOT_NAME}: Goodbye, {name}!")
        break
    # Bonus: human handover ends the chat
    elif message == "agent" or message == "human":
        print(f"{BOT_NAME}: Connecting you to a human...")
        break
    # Why: complaints come first, so an unhappy customer always reaches a human
    elif " refund " in padded or " complaint " in padded or " late " in padded:
        complaints += 1
        answered += 1
        print(f"{BOT_NAME}: Sorry about that. A manager will call you within 1 hour.")
    elif message == "/quote":
        item = input(f"{BOT_NAME}: Which item? ").strip().lower()
        quantity_text = input(f"{BOT_NAME}: How many? ").strip()

        if item == "cupcake":
            unit_price = CUPCAKE_PRICE
        elif item == "brownie":
            unit_price = BROWNIE_PRICE
        elif item == "chocolate cake":
            unit_price = CAKE_PRICE
        else:
            unit_price = 0

        # Bonus: isdigit() stops letters from crashing int()
        if quantity_text.isdigit():
            quantity = int(quantity_text)
        else:
            quantity = 0

        if unit_price == 0:
            print(f"{BOT_NAME}: Sorry, {item} is not on our menu.")
        elif quantity < 1:
            print(f"{BOT_NAME}: Please type the quantity as a whole number, like 12.")
        else:
            subtotal = unit_price * quantity
            if quantity >= BULK_MIN_QTY:
                discount = subtotal * BULK_DISCOUNT
            else:
                discount = 0
            # Why: delivery is judged AFTER the discount, so the customer is charged fairly
            after_discount = subtotal - discount
            if after_discount >= FREE_DELIVERY_LIMIT:
                delivery = 0
            else:
                delivery = DELIVERY_FEE
            total = after_discount + delivery

            quotes += 1
            answered += 1
            quoted_value += total
            print(f"{BOT_NAME}: {quantity} x {item} = {subtotal:,} PKR")
            print(f"     Discount: -{discount:,.0f} PKR | Delivery: {delivery:,} PKR")
            print(f"     Total: {total:,.0f} PKR")
    elif "hour" in message or "open" in message or "timing" in message or " time " in padded:
        answered += 1
        print(f"{BOT_NAME}: We are open 9 am to 10 pm, every day.")
    elif "delivery" in message:
        answered += 1
        print(f"{BOT_NAME}: Delivery is {DELIVERY_FEE:,} PKR, free from {FREE_DELIVERY_LIMIT:,} PKR.")
    elif "price" in message or "cost" in message or "how much" in message:
        answered += 1
        print(f"{BOT_NAME}: Cupcake {CUPCAKE_PRICE:,} PKR, brownie {BROWNIE_PRICE:,} PKR, "
              f"chocolate cake {CAKE_PRICE:,} PKR. Type /quote for an exact price.")
    elif "where" in message or "location" in message:
        answered += 1
        print(f"{BOT_NAME}: We are on Main Boulevard, Lahore.")
    # Why: short words like "hi" use == / startswith, because "hi" hides inside "which"
    elif message == "hi" or message == "hello" or message.startswith("salam"):
        answered += 1
        print(f"{BOT_NAME}: Hello {name}! Ask me anything or type /quote.")
    else:
        unanswered += 1
        question = message.capitalize()[:150]
        tokens = round(len(question) / 4)

        # Why: private details never leave the computer, so they go to the local model at cost 0
        if "phone" in message or "cnic" in message or "my address" in message:
            model = "llama3.2 (local, private)"
            cost = 0
        else:
            model = "small cloud model (cheap)"
            cost = tokens / 1000 * CLOUD_PRICE_PER_1K
        ai_cost += cost

        prompt = f"""You are the assistant of {BUSINESS}.
Answer {name} in 2 short lines. Question: {question}"""
        print(f"{BOT_NAME}: Good question! Routed to: {model} (~{tokens} tokens)")
        print(f"     Prompt: {prompt}")

print("=" * 50)
print("Session report")
print(f"Messages: {count} | Answered by rules: {answered} | Unanswered: {unanswered}")
print(f"Quotes: {quotes} | Quoted value: {quoted_value:,.0f} PKR | Complaints: {complaints}")
print(f"Estimated AI cost for unanswered questions: {ai_cost:.4f} PKR")
print("=" * 50)

