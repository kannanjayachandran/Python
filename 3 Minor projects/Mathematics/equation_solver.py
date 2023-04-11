import math


def quadratic(a: int, b: int, c: int):
    x1 = (-b + math.sqrt(b * b - (4 * a * c))) / (2 * a)
    x2 = (-b - math.sqrt(b * b - (4 * a * c))) / (2 * a)

    return f"Two possible solutions are {x1: .1f} and {x2: .1f}"


print(quadratic(1, 7, -15))
