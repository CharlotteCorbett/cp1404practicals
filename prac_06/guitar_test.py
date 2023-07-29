"""This program will test guitars.py"""

from prac_06.guitar import Guitar

guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
another_guitar = Guitar("Another Guitar", 2013)

guitar.get_age()
print(f"{guitar.name} get_age() - Expected 100. Got {guitar.age}")
another_guitar.get_age()
print(f"{another_guitar.name} get_age() - Expected 100. Got {another_guitar.age}")
print(f"{guitar.name} is_vintage() - Expected True. Got {guitar.is_vintage()}")
print(f"{guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")

