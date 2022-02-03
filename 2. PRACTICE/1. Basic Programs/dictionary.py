# Dictionary in python

colors = {'banana': 'yellow', 'apple': 'red', 'strawberry': 'red', 'grapes': 'purple', 'orange': 'orange'}

print("\n The dictionary is: ", colors, "\n")

# Accessing elements in the dictionary
print('The color of apple is:', colors['apple'])
print('The color of grapes is:', colors['grapes'], "\n")

print("---------------------------------------\n")

# Conditional operations in dictionary.
if 'banana' in colors:
    print("I know the color of banana")
if 'potato' not in colors:
    print("Potato is not a fruit.\n")

# Adding a new item to dictionary.
print("---------------------------------------\n")
colors['apricot'] = 'orange'
colors.update({'date': 'black', 'cherry': 'red'})
print("Modified dictionary is: ", colors)

# Looping through the dictionary
print("\n---------------------------------------\n")
print("The fruits are: ", end='')

for fruits in colors:
    print(fruits, end=' ')
print("\n")
for fruit, color in colors.items():
    print("The color of", fruit, "is", color)

# Some methods in dictionary
print(colors.get('apple'))  # Returns the value of the key provided.
print(colors.items())  # Returns a view object.
"""
The view object contains the key-value pairs of the dictionary, as tuples in a list.
The view object will reflect any changes done to the dictionary, see example below.
"""
p = colors.copy()  # copy the dictionary.
p.pop('apple')  # removes the element with the specified key.
p.keys()  # returns a list containing the keys.
p.popitem()  # removes the last inserted key-value pair.
p.clear()  # clear the entire dictionary.


""""
Dictionaries are very fast. They consist of key value pair.
 The key must be immutable ie; Strings, numbers.
 The value can be anything.
 They are not ordered. From 3.6 they are considered as ordered.
 They are iterable.
"""