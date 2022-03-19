# split() method in python.

# 1. Taking two numbers as inputs and finding their product.
a, b = [int(x) for x in input("Enter the numbers: ").split()]
print("product is: ", a*b)

# 2. Taking two floating numbers separated by , and finding their product.
c, d, e = [float(x) for x in input("Enter the numbers: ").split(",")]
print("Product of ", c, d, e, " is ", c*d*e)
