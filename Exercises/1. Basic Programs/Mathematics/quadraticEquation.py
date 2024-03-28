# A program to solve quadratic equation.

from math import sqrt as s


a = int(input('Enter the coefficient of a '))
b = int(input('Enter the coefficient of b '))
c = int(input('Enter the coefficient of c '))

discriminant = (b**2) - (4 * a * c)

soln1 = (-b + s((b**2) - (4*a*c))) / (2*a)
soln2 = (-b - s((b**2) - (4*a*c))) / (2*a)

print("The roots are ", soln1, ",", soln2)
