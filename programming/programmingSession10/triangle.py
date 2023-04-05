# Program that calculates the distance between 2 points

import math
def square(x):
    return x * x

def distance(x1, y1, x2, y2):
    distance = math.sqrt(square(x2 - x1) + square(y2 - y1))
    return distance

def perimeter(side1, side2, side3):
    perimeter = side1 + side2 + side3
    return perimeter

def main():
    x1, y1, x2, y2, x3, y3 = eval(input("Enter the coordinates of 3 points to measure the distance >> "))
    print(f"The perimeter of the triangle is {perimeter(distance(x1, y1, x2, y2), distance(x2, y2, x3, y3), distance(x1, y1, x3, y3))}")

main()