# Find the factorial of a number.


num = int(input("Enter the number: "))

fact = 1
for i in range(1, num+1):
    fact *= i

print(fact, "is the factorial of", num)
