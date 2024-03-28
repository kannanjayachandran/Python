# Find the area of a triangle using the given formula.
# Area of a triangle = (s*(s-a)*(s-b)*(s-c))-1/2

from math import sqrt
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

s = float(a + b + c) / 2
area = sqrt((s*((s-a)*(s-b)*(s-c))))

print("The area of the triangle is: ", area)
