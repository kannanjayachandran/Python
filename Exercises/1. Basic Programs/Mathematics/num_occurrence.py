# Write a program to find the occurrence of a particular digit in any given number.

num = int(input("Enter the number: "))
num_digit = int(input("Enter the digit to check: "))
num_copy = num
count = 0
while num > 0:
    remainder = num % 10
    if remainder == num_digit:
        count += 1
    num //= 10

print(f"In {num_copy} {num_digit} exists {count} times.")
