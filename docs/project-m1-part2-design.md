# Module 1 Project Part 2: AI Front Desk (Design)

## Intents

| Intent | Keywords | Reply |
|---|---|---|
| Complaint | refund, complaint, late | A manager will call you within 1 hour |
| Hours | hour, open, timing, time | Open 9 am to 10 pm, every day |
| Delivery | delivery | 200 PKR, free from 3,000 PKR |
| Prices | price, cost, how much | Item prices and a hint to use /quote |
| Location | where, location | Main Boulevard, Lahore |
| Greeting | hi, hello (exact), salam (starts with) | Hello and an offer to help |
| Human handover | agent, human | Connecting you to a human... |

## Business rules

| Rule | Value |
|---|---|
| Item prices | cupcake 250 PKR, brownie 300 PKR, chocolate cake 1,500 PKR |
| Bulk discount | 10% off for 10 or more items |
| Delivery | 200 PKR, free when the order after discount is 3,000 PKR or more |
| Private words | phone, cnic, my address |

## Rule tests

| You type | Expected | Pass? |
|---|---|---|
| `  WHAT are your hours  ` | Hours | Yes |
| `which cake is best?` | Fallback, not a greeting | Yes |
| `my order is late` | Manager reply | Yes |
| `/quote`, 1 chocolate cake | Delivery fee charged (total 1,700) | Yes |
| `/quote`, 3 chocolate cakes | Delivery free (total 4,500) | Yes |
| `/quote`, 12 cupcakes | Discount applied (total 2,900) | Yes |
| `/quote`, pizza | Not on our menu, no crash | Yes |
| `can I change my phone number on the order?` | Local model, cost 0 | Yes |
| Press Enter with no text | Asks again | Yes |
| `BYE` | Goodbye + session report | Yes |
| `/quote`, cupcake, `abc` (bonus) | Polite message, no crash | Yes |