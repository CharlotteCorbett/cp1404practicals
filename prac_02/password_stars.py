"""
Pseudocode:
Get user password

If user password length < 7:
    While user password length < 7:
        Display invalid password message
        Get user password

For character in user password length:
    Display '*'
"""


def main():
    """Main program"""
    password = get_valid_password()
    print_password(password)


def print_password(password):
    """Function that prints password as stars"""
    for character in password:
        print('*', end='')


def get_valid_password():
    """Function that gets password with error checking"""
    password = input("Enter password:")
    while len(password) < 7:
        print("Password too short. Try again.")
        password = input("Enter password:")
    return password


main()
