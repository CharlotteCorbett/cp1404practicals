"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    When the user enters either a string of float (eg: seven / 6.6)
2. When will a ZeroDivisionError occur?
    When the user enters 0 into the denominator prompt.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Yes. See below.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        while denominator == 0:
            print("Cannot be zero! Mathematics can't define it :(")
            denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")