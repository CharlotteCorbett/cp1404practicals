"""Do this now from video 2 in Lecture 3-Files and Exceptions
Written after practicing read(n), readline, and readlines methods in Python
console.
"""

infile = open("secret_stuff.txt")
for line in infile:
    line.strip("\n")
    if line.startswith("#"):    #Found this method in textbook
        print(line.strip("#"))
infile.close()
