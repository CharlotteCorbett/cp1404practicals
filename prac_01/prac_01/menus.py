"""
Menus

Pseudocode:
(Supplied from Prac 1 @ GitHub)
Get name
Display menu
Get choice from user
While choice != Q
   If choice == H
       display "hello" name
   Else if choice == G
       Display "goodbye" name
   Else
       display invalid message
   Display menu
   Get choice
Display finished message
"""

name = input("Enter name: ")

# Constant
MENU = "(H)ello \n" "(G)oodbye\n" "(Q)uit\n"

print(MENU)

choice = input(">>>").upper()

while choice != 'Q':
    if choice == 'H':
        print("Hello {}".format(name))
    elif choice == 'G':
        print("Goodbye {}".format(name))
    else:
        print("Invalid choice")
    print(MENU)
    choice = input(">>>").upper()

print("Finished.")
