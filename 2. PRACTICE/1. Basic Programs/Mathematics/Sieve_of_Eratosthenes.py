"""
Given a number print all the prime numbers below or equal to that number.
Using the Sieve of eratosthenes method. The complexity of this method is O(n*log(log n)) 
The normal sieve of eratosthenees method can be used for numbers till 10^7 or 10^8.
"""

num = int(input("Enter the number: "))

# Creating an array/list for storing "num" number of elements and setting default value to be True
sieve = [True for i in range(num+1)]
p = 2
sieve[0] = False
sieve[1] = False


# Setting all the multiples of primes to be False
while p * p <= num:
    if sieve[p]:
        for i in range(p**2, num+1, p):
            sieve[i] = False
    p += 1

# Printing all the numbers whose values are not False
for p in range(num+1):
    if sieve[p] == True:
        print(p, end=' ')
