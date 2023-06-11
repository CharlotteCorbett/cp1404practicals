"""
Shop  Calculator

Pseudocode:
Get number of items
while number of items <0:
    Get valid number of items
For each item:
    Get item price
    Calculate total price
If total price > 100:
     Deduct 10% of the total price
Display total price
"""

total_price = 0
number_of_items = int(input("Number of items:  "))

while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items:  "))

for item in range(number_of_items):
    item_price = float(input("Item price: "))
    total_price += item_price

if total_price > 100:
    total_price -= total_price * 0.1

print(f"Total price for {number_of_items} items is ${total_price:.2f}")
