# Find the largest number among three given numbers.

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))

num1, num2, num3 = [int(x) for x in input(
    "Enter the three numbers (separated by coma): ").split(",")]

# Method 1 : Using logical operators.
if num1 > num2 and num1 > num3:
    print(num1, "is the largest number.")
elif num2 > num1 and num2 > num3:
    print(num2, "is the largest number.")
elif num3 > num2 and num3 > num1:
    print(num3, "is the largest number.")

# Method 2
large = num1
if num2 > num1:
    large = num2
if num3 > num1:
    large = num3
print(large, "is the largest number.")

# Method 3 : Built in function.
print(max(num1, num2, num3), "is the largest number.")

'''
    max() function returns the largest item in an iterable. 
    It can also be used to find the largest item between two or more parameters.
'''
