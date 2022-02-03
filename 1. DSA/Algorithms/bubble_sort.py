# Bubble sort in python

from random import randint as r

# making a list with 20 random numbers
lis = []
for i in range(20):
    lis.append(r(1, 100))

print("The list before sorting is: ", lis)

# Bubble sort
for i in range(len(lis)):
    for j in range(len(lis) - i - 1):
        if lis[j] > lis[j + 1]:
            lis[j], lis[j + 1] = lis[j + 1], lis[j]

print('After sorting the list is: ', lis)

"""
Bubble sort also referred to as sinking sort is a simple sorting algorithm that 
repeatedly steps through the list, compares adjacent elements and swaps them if 
they are in the wrong order. The pass through the list is repeated until the list is sorted.
"""