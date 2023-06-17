"""Do this now from video 3 in Lecture 3-Files and Exceptions
"""

with open("cool_guitars.txt") as in_file:
    for line in in_file:
        segments = line.strip().split(',')
        name = segments[0]
        year = segments[1]
        price = segments[2].strip('\\n')
        print(f"{name} {year} ${price}")
