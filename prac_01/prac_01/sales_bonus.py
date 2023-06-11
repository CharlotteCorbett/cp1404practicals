"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.

Pseudocode:
Get user sales
If user sales <1000:
    user bonus = user sales * 0.1
If user sales >= 1000:
    user bonus = user sales * 0.15
Display user bonus
"""

# Easier to change % bonus via constants, no magic numbers.
LOWER_BONUS = 0.1
HIGHER_BONUS = 0.15
SALES_THRESHOLD = 1000


sales = float(input("Sales:$"))

user_bonus = 0

if sales < SALES_THRESHOLD:
    user_bonus = sales * LOWER_BONUS
else:
    user_bonus = sales * HIGHER_BONUS

print(f"Bonus:${user_bonus:.2f}")
