numbers = [3, 1, 4, 1, 5, 9, 2]

print(numbers[0])
# 3
print(numbers[-1])
# 9 (wrong. correct output: 2)
print(numbers[3])
# 1
print(numbers[:-1])
# [3,1,4,1,5] (wrong. correct output: [3,1,4,1,5,9]
print(numbers[3:4])
# [1]
print(5 in numbers)
# True
print(7 in numbers)
# False
print("3" in numbers)
# False
print(numbers + [6, 5, 3])
# [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# 1.
del numbers[1]
numbers.insert(1, 'ten')

# 2.
del numbers[6]
numbers.insert(6, 1)

# 3.
print(numbers[:-2])

# 4.
print(9 in numbers)
