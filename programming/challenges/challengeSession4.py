# Write a program to determine the length of a ladder required 
# to reach a given height when leaned against a house. The height 
# and angle of the ladder are given as inputs. 

import math

def challenge1():
    height = float(input('Enter a height >> '))
    angle = (math.pi/180) * float(input('Enter the angle in degrees >> '))
    print(f"\nThe length of the ladder should be {height/math.sin(angle):.2f}\n")

# challenge1()

# A program that uses the Newton's method in a loop to approximate the square root of a number
# Provided a number of improving iterations.

def challenge2():
    x = eval(input("Will calculate the square root of >> "))
    improvingTimes = int(input('How many times should the approximation be improved? '))
    guess = x/2
    for i in range(improvingTimes - 1):
        guess = (guess + x/guess)/2
    print(f'The approximation obtained is {guess:.2f}, which is {math.sqrt(x) - guess:.2f} different from the actual sqrt: {math.sqrt(x):.2f}')

# challenge2()