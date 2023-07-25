


def main():
    email_to_name = {}
    email = input("Email: ")

    # get user email until they enter blank
    while email != '':
        # extract name from email function
        name_segment, is_name = extract_name_from_email(email)

        # selection for user input
        if is_name == 'y' or is_name == '':
            name = f"{name_segment}"
            email_to_name[email] = name
        else:
            name = input("Name: ")
            correct_name = name.title()
            email_to_name[email] = correct_name
        email = input("Email: ")

    # loop through name to emails
    email_to_names = email_to_name.items()
    for name_email in email_to_names:
        print(f"{name_email[1].title()} ({name_email[0]})")

def extract_name_from_email(email):
    name_email_segment = email.split("@")
    if '.' in name_email_segment[0]:
        name_segments = name_email_segment[0].split('.')
        name_segment = f"{name_segments[0].title()} {name_segments[1].title()}"
        is_name = input(f"Is your name {name_segment}? (Y/n) ").lower()
    else:
        name_segment = name_email_segment[0]
        is_name = input(f"Is your name {name_segment.title()}? (Y/n) ").lower()

    return name_segment, is_name




main()
