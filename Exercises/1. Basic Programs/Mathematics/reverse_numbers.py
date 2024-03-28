# Reverse a given number.

num = int(input("Enter the number: "))

# Method 1 : string slicing.
print(str(num)[::-1])

# Method 2
num_rev = 0
while(num != 0):
    last = num % 10
    num_rev = (num_rev * 10) + last
    num //= 10

print(num_rev)
