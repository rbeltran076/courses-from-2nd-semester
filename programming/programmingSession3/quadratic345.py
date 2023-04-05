# A program that computes the real roots of a quadratic equation
# Illustrates the use of a two-way decision in main3() and multiple way decision in main4().

import math # Makes the math library available

def main3():
    print("This program finds the real solutions to a quadratic: ")
    print()

    a, b, c = eval(input("Please, enter the coefficients (a,b,c) "))
    discriminant = b * b - 4 * a * c
    if discriminant < 0:
        print("\nThe equation has no real roots!.")
    else:
        discriminantRoot = math.sqrt(b * b - 4 * a * c) # The discriminant is the polynomial inside the root
        solution1 = (-b + discriminantRoot) / (2 * a)
        solution2 = (-b - discriminantRoot) / (2 * a)
        print()
        print("The solutions are", solution1, solution2)

def main4():
    print("This program finds the real solutions to a quadratic: ")
    print()

    a, b, c = eval(input("Please, enter the coefficients (a,b,c) "))
    discriminant = b * b - 4 * a * c
    if discriminant < 0:
        print("\nThe equation has no real roots!.")
    elif discriminant == 0:
        print("The solution when discriminant 0 is", -b/2*a)
    else:
        discriminantRoot = math.sqrt(b * b - 4 * a * c)  # The discriminant is the polynomial inside the root
        solution1 = (-b + discriminantRoot) / (2 * a)
        solution2 = (-b - discriminantRoot) / (2 * a)
        print()
        print("The solutions are", solution1, solution2)

def main5():


    try:
        print("This program finds the real solutions to a quadratic: ")
        print()

        a, b, c = eval(input("Please, enter the coefficients (a,b,c)"))
        discriminant = b * b - 4 * a * c
        if discriminant >= 0:
            discriminantRoot = math.sqrt(b * b - 4 * a * c)  # The discriminant is the polynomial inside the root
            solution1 = (-b + discriminantRoot) / (2 * a)
            solution2 = (-b - discriminantRoot) / (2 * a)
            print()
            print("The solutions are", solution1, solution2)
    except:
        print("")   

# Function that sums up 2 numbers
