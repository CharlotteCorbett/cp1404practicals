numbers = []
for number in range(5):
    given_number = int(input("Number: "))
    numbers.append(given_number)

print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[4]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
total_numbers = 0
for number in numbers:
    total_numbers += number
average = float(total_numbers) / float(len(numbers))
print(f"The average of the numbers is {average:.1f}")

# Woefully inadequate security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("Username: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")