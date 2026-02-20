
# Student Name: [Your Name]
# Grocery Store Billing System

# Get the prices from the user
item1 = float(input("Enter price for item 1: "))
item2 = float(input("Enter price for item 2: "))
item3 = float(input("Enter price for item 3: "))

# Calculate the total
total = item1 + item2 + item3

# Check for discount
if total > 50:
    discount = total * 0.10
    final_price = total - discount
else:
    discount = 0
    final_price = total

# Show the results
print("Original Total:", total)
print("Discount:", discount)
print("Final Amount to Pay:", final_price)