# A program that computes the real roots of a quadratic equation
# illustrates use of a math library
# This program crashes if the equation has no real roots

import math # Makes the math library available
def main():
    print("This program finds the real solutions to a quadratic: ")
    print()

    a,b,c = eval(input("Please, enter the coefficients (a,b,c)"))

    discriminantRoot = math.sqrt(b * b - 4 * a * c) # The discriminant is the polynomial inside the root
    root1 = (-b + discriminantRoot)/(4 * a * c)
    root2 = -(-b + discriminantRoot)/(4 * a * c)


