"""
Program that converts between Celsius and Fahrenheit temperatures.
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    """Main program"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = calculate_fahrenheit(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit:"))
            celsius = calculate_celsius(fahrenheit)
            print(f"Result: {celsius:2f}C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def calculate_fahrenheit(celsius):
    """Function calculates Fahrenheit"""
    return celsius * 9.0 / 5 + 32


def calculate_celsius(fahrenheit):
    """Function calculates Celsius"""
    return 5 / 9 * (fahrenheit - 32)


main()
