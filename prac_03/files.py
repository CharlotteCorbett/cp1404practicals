# 1. Write code that asks the user for their name, then opens a file called "name.txt"
# and writes that name to it. Remember to close your file.
with open("name.txt", 'w') as infile:
    infile.write(input("What is your name? "))

# #2.(In the same file, but as if it were a separate program) Write code that opens "name.txt" and reads
# # the name (as above) then prints, "Your name is Bob" (or whatever the name is in the file).
infile = open("name.txt", 'r')
name = infile.read()
print(f"Your name is {name}")
infile.close()
#
#3.Write code that opens "numbers.txt", reads only the first two numbers and adds them together then prints the result, which should be... 59.
infile = open("numbers.txt", 'r')
total = 0
for line in range(2):
    number = int(infile.readline().strip('\n'))
    total += number
print(total)
infile.close()

#4.Now write a fourth block of code that prints the total for all lines in
# numbers.txt or a file with any number of numbers.
infile = open("numbers.txt", 'r')
total = 0
for line in range(3):
    number = int(infile.readline().strip('\n'))
    total += number
print(total)
infile.close()
