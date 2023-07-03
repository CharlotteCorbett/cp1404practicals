"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

 # Original code using  Look Before You Leap (LBYL) approach
STATE_CODE_TO_STATE_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
            "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(STATE_CODE_TO_STATE_NAME)

state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code in STATE_CODE_TO_STATE_NAME:
        print(state_code, "is", STATE_CODE_TO_STATE_NAME[state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

 # For loop that prints each state
for state in STATE_CODE_TO_STATE_NAME:
    print(f"{state} is {STATE_CODE_TO_STATE_NAME[state]}")


# Easier to Ask Forgiveness than Permission (EAFP) approach.

print(STATE_CODE_TO_STATE_NAME)

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(state_code, "is", STATE_CODE_TO_STATE_NAME[state_code])
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()