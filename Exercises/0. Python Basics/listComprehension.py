# List comprehension

'''
List comprehension is a way to create a list in a single line of code. 
'''

lis = [x for x in range(10)]
print(f'Original list: {lis}\n')

name = [l for l in 'kannan j']
print(f'Name List: {name}')

noSpace = [l for l in name if l != ' ']
print(f'Name list with no space: {noSpace}\n')

# Even number's squares in one line using list comprehension.
square = [x**2 for x in range(10) if x % 2 == 0]
print(f'Square of even numbers under 10: {square}\n')

# Multiplying two sets using list comprehension
'''
This is the equivalent of a for loop iterating through [10, 20, 30] and an inside for loop,
iterating through [1, 2, 3] for each value of the outside for loop.
'''

lis1 = [1, 2, 3]
lis2 = [10, 20]

multi = [x * y for x in lis1 for y in lis2]
print(f'Product of two lists are: {multi}\n')


# String manipulation using comprehension
l = 'elephant'
print([char.upper() for char in l])

friends = ['ron', 'paul', 'zimba']
print([friend[0].upper() for friend in friends])

# # Boolean values with list comprehension
bool_lis = [0, '', 1, []]
print([bool(val) for val in bool_lis])

# # Converting a int list to string
numbers = [1, 3, 4, 54, 4, 46]
number_str = [str(number) for number in numbers]
print(number_str)
