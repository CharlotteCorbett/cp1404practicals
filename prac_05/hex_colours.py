"""
Prac 5
Pseudocode:
display colour dictionary
get colour from user
while user input is not blank:
    try:
        display colour code
    except KeyError:
        display invalid colour message
    get colour from user

"""

colour_to_code = {"Absolute Zero": "#0048ba", "Acid Green":"#b0bf1a", "Amethyst": "#9966cc",
                  "Ash Grey": "#b2beb5", "Baby Blue": "#89cff0", "Baby Pink": "#f4c2c2",
                  "Battleship Gray": "#848482", "Bistre": "#3d2b1f", "Bleu de France": "#318ce7",
                  "Brandeis Blue": "#0070ff"}

print(colour_to_code)
colour = input("Colour: ").title()
while colour != "":
    try:
        print(f"{colour} is coded as {colour_to_code[colour]}")
    except KeyError:
        print("Invalid colour. Please try again")
    colour = input("Colour: ").title()
