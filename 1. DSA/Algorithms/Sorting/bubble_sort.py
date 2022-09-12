# Bubble sort in python

from random import randint

lis = []
for i in range(10):
    lis.append(randint(1, 100))

print("The list before sorting is: ", lis)

# Bubble sort Algorithm
for i in range(len(lis)):
    for j in range(len(lis) - i - 1):
        if lis[j] > lis[j + 1]:
            lis[j], lis[j + 1] = lis[j + 1], lis[j]

print('\nAfter sorting the list is: ', lis)

"""
Bubble sort also referred to as sinking sort is a simple sorting 
algorithm that repeatedly steps through the list, compares adjacent 
elements and swaps them if they are in the wrong order. The pass 
through the list is repeated until the list is sorted.

If the array is already sorted bubble sort would take O(n) time.
O(N^2) is the worst time complexity.
"""
