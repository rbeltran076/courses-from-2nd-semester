# Program that calculates the distance between 2 points

import math
def square(x):
    return x * x

def distance(x1, y1, x2, y2):
    distance = math.sqrt(square(x2 - x1) + square(y2 - y1))
    return distance

def main():
    x1, y1, x2, y2 = eval(input("Enter the coordinates of the points to measure the distance >> "))
    print(f"The distance between the two points is {distance(x1, y1, x2, y2):.3}")

main()