# Find the n-th Fibonacci number.

num = int(input("Enter the number: "))
if num == 1 or num == 0:
    print(num)

else:
    first, second, count = 0, 1, 2
    while count <= num:
        first, second = second, first+second
        count += 1

print(num, "th fibonacci number is", second)

'''
    This is not the efficient way for finding fibonacci numbers.
'''
