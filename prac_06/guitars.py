"""
This program will get and show guitars using Guitar class

Pseudocode:
display "My guitars!"
while name != '':
    get guitar name
    get guitar year
    get guitar cost
    add guitar
    display guitar added
 for guitar in guitars:
    display neatly formatted guitar
"""
from prac_06.guitar import Guitar

guitars = []

print("My guitars!")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost:$"))
    new_guitar = Guitar(name, year, cost)
    guitars.append(new_guitar)
    print(f"{new_guitar} added.")
    name = input("Name: ")


print("These are my guitars:")
for guitar_number, guitar in enumerate(guitars, 1):
    guitar.get_age()
    vintage_string = " (vintage)" if guitar.is_vintage() else ""
    print(f"Guitar {guitar_number}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")



print()
