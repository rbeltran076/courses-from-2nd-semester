# A program that computes the real roots of a quadratic eq.
# Simple version using if to avoid crash

import math # Makes the math library available
def main():
    print("This program finds the real solutions to a quadratic: ")
    print()

    a, b, c = eval(input("Please, enter the coefficients (a,b,c)"))
    discriminant = b * b - 4 * a * c
    if discriminant >= 0:
        discriminantRoot = math.sqrt(b * b - 4 * a * c) # The discriminant is the polynomial inside the root
        solution1 = (-b + discriminantRoot) / (2 * a)
        solution2 = (-b - discriminantRoot) / (2 * a)
        print()
        print("The solutions are", solution1, solution2)


