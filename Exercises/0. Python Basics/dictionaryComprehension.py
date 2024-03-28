# dictionary comprehension

'''
Dictionary comprehension is a way to create a dictionary in a single line of code.
'''

# Creating a dictionary with keys as numbers and values as their squares
dic1 = {x: x**2 for x in range(11)}
print(f'Dictionary 1: {dic1}\n')


# Creating a dictionary with keys as index as values as the values in the list
dic2 = {index: value for index, value in enumerate("Kannan J")}
print(f'Dictionary 2: {dic2}\n')

dic3 = {index: value for index, value in enumerate("Kannan J") if value != ' '}
print(f'Dictionary 3: {dic3}\n')

# Dictionary comprehension along with zip function
a = [1, 2, 3]
b = ["apple", "Orange", "Grape"]
dic4 = {key: value for key, value in zip(a, b)}
print(dic4)
