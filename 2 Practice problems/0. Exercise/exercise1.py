
#  EXERCISE 1
#  1.  Ask the user for two numbers between 1 and 100. Then count from the lower number to the higher number.


num1 = int(input("Enter a number between 1 and 100: "))
num2 = int(input("Enter a number between 1 and 100: "))

if num1 > num2:
    for i in range(num2, num1+1):
        print(i)
elif num2 > num1:
    for i in range(num1, num2+1):
        print(i)


#  2.  Ask the user for a String input and reverse it.

name = input("Enter a string input")
word = ""

for char in name:
    word = char + word
print(word)
print(name[::-1])  # One line solution in pythonic way.


# 3. Ask the user for a number between 1 and 12 and print a times table for that.

num = input("Enter a number between 1 and 12: ")

while (not num.isdigit()) or int(num) < 1 or int(num) > 12:
    print("Input must be a number between 1 and 12 !!")
    num = input("Enter a number between 1 and 12: ")

num1 = int(num)
for i in range(1, 13):
    print(i, " * ", num1, " = ", i*num1)


# 4. Make a times table of all the numbers between 1 and 12.

for i in range(1, 13):
    print("----------------------------")
    print(f"This is the times table of {i}")
    for j in range(1, 13):
        print(j, " * ", i, " = ", i*j)


# 5. Ask the user for an input f of a sequence of numbers and calculate the mean of those numbers.

print("Type 'x' to stop.")
num = input("Enter the first number: ")
num1 = []
while num.lower() != "x":
    num1.append(int(num))
    num = input("Enter the next number: ")

add = 0
for i in num1:
    add += i
print(add / len(num1))
print(sum(num1) / len(num1))  # Built-in method sum


# 6. Write a program to calculate the factorial of 15.

num = 15
fact = 1
for i in range(1, num+1):
    fact *= i

print(fact)


# 7. Ask the user for an input and calculate the factorial of that number.

num = input()

while not num.isdigit():
    num = input("Enter a number: ")

fact = 1
for i in range(1, int(num) + 1):
    fact *= i
print(fact)


# 8. Write a program to find fibonacci sequence.

first = 0
second = 1
num = 5
lis = []

for i in range(num+1):
    lis.append(first)
    first, second = second, first+second   # Multi assignment and no need of temp variable.

print(lis)


# 9. Create a "F" pattern.

star = "*"

for i in range(1, 7):
    for j in range(1, 6):
        if i == 1 and j < 6:
            print(star, end='')
        elif i == 2 and j == 1:
            print()
            print(star)
        elif i == 3 and j < 5:
            print(star, end='')
        elif i == 4 and j == 1:
            print()
            print(star)
        elif i == 5 and j == 1:
            print(star)
        elif i == 6 and j == 1:
            print(star)


# 10. Write a program that determine all numbers from 1 to 100 as odd and even and put them in
# two lists with all the odd numbers in one and all the even numbers in one.

even = []
odd = []
for i in range(1, 101):
    if i % 2 == 0:
        even.append(i)
    elif i % 2 != 0:
        odd.append(i)

print(f'Even numbers are: {even}')
print("Odd list is : ", odd)

# End of exercise 1.
