# A program to check whether a given number is prime or not.

from math import sqrt

num = int(input("Enter the number: "))

if num == 0 or num == 1:
    print("Neither prime nor composite.")
else:
    flag = 1
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            print(num, " is Not prime")
            flag = 0
            break
    if flag:
        print(num, " is prime")
