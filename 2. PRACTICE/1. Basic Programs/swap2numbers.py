# Swap two numbers (Using multi assignment operation)

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("The first number is: ", a)
print("The second number is: ", b)

a, b = b, a

print("The first number is: ", a)
print("The second number is: ", b)