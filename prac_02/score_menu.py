"""
Program not entirely finished.
Any feedback gladly welcomed.

This program will show scores and or print stars based on the score number.
"""

MENU = "(S)how result\n" "(P)rint stars\n"  "(Q)uit\n" "\n"


def main():
    """Main program"""
    print(MENU)

    choice = input("Enter choice:").upper()

    while choice != 'Q':
        if choice == 'S':
            score = int(input("Enter score:"))
            status = determine_score_status(score)
            print(status)
        elif choice == 'P':
            score = int(input("Enter score:"))
            for star in range(score):
                print('*', end='')
        else:
            print("Invalid choice")
        print()
        print(MENU)
        choice = input("Enter choice:").upper()

    print("Thank you")


def determine_score_status(score):
    """Function decides score status from score"""
    if score < 0 or score > 100:
        score = "Invalid score"
    elif score >= 90:
        score = "Excellent"
    elif score >= 50:
        score = "Passable"
    else:
        score = "Bad"
    return score


main()
