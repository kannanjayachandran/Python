# String methods.
para = """
This string will show some simple string manipulations available in python. There are many builtin 
functionalities in pyton, which simplifies the overall development. The current version of python is python 3.
Python is an interpreted language. It's dynamically typed.
"""
new_words = para.split(' ')
# print("Split method: ", new_words)

for i in range(len(new_words)):
    new_words[i] = new_words[i].strip('\n')

print("\n Strip method: ", new_words)

print('current' in new_words)


"""
Strings are immutable in python.
split() splits the string whenever it encounters the specified parameter; space/new line here; and returns a
list with all the words.

strip() removes all the occurrence of specified parameter and returns a list of the words in the list.
"""