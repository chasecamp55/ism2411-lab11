# ISM2411 Lab 11 - Customer Dictionary & Lookup
# Name: Chase Campbell

# Reflection 1:
# I would use .get() when a field might be missing because it
# lets me provide a default value instead of causing an error.
# I would use bracket notation when I know the key exists and
# want an error if it is missing.

# Reflection 2:
# This reminds me of using a PivotTable in Excel to group
# and summarize data. Python can be more useful for large
# datasets because it can automate the process and handle
# repeated calculations without manually updating a table.

# Exercise 1 - One Customer

customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1500
}

print("Exercise 1")
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

# Exercise 2 - Update and Add

print("\nExercise 2")

customer["phone"] = "555-123-4567"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)

# Exercise 3 - Safe Lookup

print("\nExercise 3")

email = customer.get("email", "no email on file")
print(email)

try:
    print(customer["email"])
except KeyError:
    print("KeyError: email does not exist")
   
# Exercise 4 - Iterate

print("\nExercise 4")

for key, value in customer.items():
    print(f"{key}: {value}")

# Without .items(), the loop only gives us the keys.
for key in customer:
    print(key)

# Exercise 5 - Lookup Table

print("\nExercise 5")

tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

tier = customer["tier"]
discount = tier_discounts.get(tier, 0)

price = 200
final_price = price * (1 - discount)

print(f"Tier: {tier}")
print(f"Discount: {discount:.0%}")
print(f"Final Price: ${final_price:.2f}")

# Exercise 6 - List of Dictionaries

print("\nExercise 6")

customers = [
    {"name": "Alice", "tier": "platinum"},
    {"name": "Bob", "tier": "gold"},
    {"name": "Charlie", "tier": "silver"}
]

for person in customers:
    name = person["name"]
    tier = person["tier"]
    discount_rate = tier_discounts.get(tier, 0)
    discount_amount = 300 * discount_rate

    print(
        f"{name} | Tier: {tier} | "
        f"Discount: ${discount_amount:.2f}"
    )

# Exercise 7 - Nested Catalog

print("\nExercise 7")

catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product} - {details['stock']} remaining")

# Exercise 8 - Sales by Region

print("\nExercise 8")

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

sales_summary = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]

    sales_summary[region] = sales_summary.get(region, 0) + amount

for region in sorted(sales_summary):
    print(f"{region}: ${sales_summary[region]}")


