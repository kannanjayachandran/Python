# Given a number find all the prime numbers below that number

from math import sqrt

num = int(input("Enter the number: "))


if num == 1 or num == 0:
    print(num)
else:
    for i in range(2, num+1):
        flag = True
        for j in range(2, int(sqrt(i))+1):
            if i % j == 0:
                flag = False
                break
        if flag:
            print(i, end=' ')
