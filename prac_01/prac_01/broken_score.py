"""
CP1404- Practical
Broken program to determine score status

Pseudocode:
Get score
If score < 0 or score > 100:
     Display invalid score message
Else if score >= 90:
     Display excellent message
Else if score >= 50:
     Display passable message
Else:
     display bad message

"""

# Fixed code

score = float(input("Enter score: "))

if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")
