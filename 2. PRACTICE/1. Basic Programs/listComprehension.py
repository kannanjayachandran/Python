# List comprehension

lis = [x for x in range(10)]
print(lis)

name = [letter for letter in 'kannan j']
print(name)
noSpace = [letter for letter in name if letter != ' ']
print(noSpace)

# Even number's squares in one line using list comprehension.
square = [x**2 for x in range(10) if x % 2 == 0]
print(square)

# Multiplying two sets using list comprehension
multi = [x * y for x in [10, 20, 30] for y in [1, 2, 3]]
print(multi)
# This is the equivalent of a for loop iterating through [10, 20, 30] and an inside for loop,
# iterating through [1, 2, 3] for each value of the outside for loop.
