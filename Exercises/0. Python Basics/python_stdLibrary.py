# Python standard library.

import math
import random
import webbrowser as wb
from random import randint

# print(dir(math))  # wil show all the functions available in math module.
# print(dir(random)) # will show all the functions available in random module.
# print(dir(webbrowser)) # will show all the functions available in webbrowser module.


print(math.pi)
print(math.cos(90))

print(random.randint(1, 10))

print(randint(1, 10))

for i in range(10):
    print(random.randint(1, 10), end=' ')

wb.open("http://pages.di.unipi.it/marino/pythonads/index.html")
wb.open("https://docs.python.org/3/library/")

"""
 The python Standard Library is a  collection of files that contains additional built-in
 functionalities. we have to import them as modules in order to access their functionalities.
 Python’s standard library is very extensive; that contains built-in modules (written in C) that
 provide access to system functionality such as file I/O that would otherwise be inaccessible to
 Python programmers, as well as modules written in Python that provide standardized solutions for
 many problems that occur in everyday programming...
"""