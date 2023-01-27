# Find the fibonacci series till a given number.

num = int(input("Enter the number: "))

if num == 1 or num == 0:
    print(num)

else:
    print("The series is : ", end='')
    first, second, count = 0, 1, 2
    while count <= num+1:
        print(first, end=',')
        first, second = second, first+second
        count += 1
print(first)
