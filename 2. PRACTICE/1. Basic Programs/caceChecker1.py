# A python program to check if the given letter is in uppercase or in lower case.

letter = input("Enter the character to check: ")

if letter.isupper():
    print(letter, " is in Uppercase.")

elif letter.islower():
    print(" is in lowercase.")
else:
    print("Invalid input")

# isupper() and islower() are two built-in python functions which returns True or False if the string is in uppercase or lowecase.
