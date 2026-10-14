""" AI Prompt Kit for a Local Business"""
 
#code
business_name = input("Business name: ")
business_type = input("Business type: ")
city = input("City: ")
main_customers = input("Main customers: ")
monthly_budget_in_PKR = input("Monthly budget in PKR: ")
monthly_budget = int(monthly_budget_in_PKR)




print(f"Business Name: {business_name}")
print(f"Business Type: {business_type}")
print(f"City: {city}")
print(f"Main Customers: {main_customers}")
print(f"Monthly Budget: {monthly_budget} PKR")

# header
print("=========================================")
print("   AI Prompt Kit for {business_name}   ")
print("=========================================")

# Prompt
print("[1] Marketing")
print(f"Write a short Instagram post for {business_name}, a {business_type} in {city}."
      f"Target {main_customers}. Friendly tone, 1 call to action.")

print("[2] Customer Service")
print(f"You are the manager of {business_name}. Write a polite reply to a customer "
      f"whose order arrived late. Apologise and offer a small discount.")



print("[3] Growth")
print(f"Suggest 3 low-cost AI tools a {business_type} in {city} can use"
      f"to attract {main_customers} with a budget of {monthly_budget} PKR per month.")



