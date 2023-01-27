# A python program to check if the given letter is in uppercase or in lower case.

letter = input("Enter the character to check: ")

if 'A' <= letter <= 'Z':
    print(letter, " is in uppercase")

elif 'a' <= letter <= 'z':
    print(letter, " is in lowercase.")
else:
    print("Invalid input.")
