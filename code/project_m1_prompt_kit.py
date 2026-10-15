"""AI Prompt Kit for a Local Business.

Asks a business owner 5 questions and prints 3 ready-to-use AI prompts
(marketing, customer service, growth). Made for small shop owners who
want AI help but don't know what to type."""
 
#code
business_name = input("Business name: ")
business_type = input("Business type: ")
city = input("City: ")
main_customers = input("Main customers: ")
# int() because input() always returns text, and the budget is a number
monthly_budget = int(input("Monthly budget (PKR): "))


print(f"Business Name: {business_name}")
print(f"Business Type: {business_type}")
print(f"City: {city}")
print(f"Main Customers: {main_customers}")
print(f"Monthly Budget: {monthly_budget} PKR")

# separators make the output easy to read and to screenshot

print("=========================================")
print(f"   AI Prompt Kit for {business_name}   ")
print("=========================================")

# each prompt names a role, task, audience and tone, because vague prompts get vague answers

print("\n[1] Marketing")
print(f"Write a short Instagram post for {business_name}, a {business_type} in {city}. "
      f"Target {main_customers}. Friendly tone, 1 call to action.")

print("\n[2] Customer Service")
print(f"You are the manager of {business_name}. Write a polite reply to a customer "
      f"whose order arrived late. Apologise and offer a small discount.")

# the budget is included so the AI suggests ideas the owner can actually afford

print("\n[3] Growth")
print(f"Suggest 3 low-cost AI tools a {business_type} in {city} can use "
      f"to attract {main_customers} with a budget of {monthly_budget} PKR per month.")


# a WhatsApp auto-reply saves the owner time

print("\n[4] WhatsApp Auto-Reply")
print(f"You are the assistant of {business_name}, a {business_type} in {city}. "
      f"Write a short, friendly WhatsApp auto-reply for {main_customers} "
      f"who ask about prices. Ask for their order details and keep it under 40 words.")
