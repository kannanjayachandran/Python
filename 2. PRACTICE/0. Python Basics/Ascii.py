# ascii value in python
letter = input("Enter the character: ")
number = int(input("Enter the number: "))

print(f'The ascii value of {letter} is', ord(letter))
print(f'The number {number} represents', chr(number))

"""
    Python chr() function is used to get a string representing of a character which points to a Unicode code integer.
    Python ord() function returns the Unicode code from a given character. 
"""
