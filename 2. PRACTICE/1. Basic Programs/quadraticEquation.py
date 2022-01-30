# A program to solve quadratic equation.

from math import sqrt


a = int(input('Enter the coefficient of a'))
b = int(input('Enter the coefficient of b'))
c = int(input('Enter the coefficient of c'))

discriminant = (b**2) - (4 * a * c)

soln1 = (-b + sqrt((b**2) - (4*a*c))) / (2*a)
soln2 = (-b - sqrt((b**2) - (4*a*c))) / (2*a)

print(soln1, " ", soln2)
