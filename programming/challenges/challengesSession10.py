# A function with attribute n that returns the sum of the
# First n natural numbers
def sumN(n):
    return sum(range(n + 1))
# sumN(3)

# Function that Sums the cubes of the first n natural numbers
def sumNCubes(n):
    sum = 0
    for number in range(n + 1):
        sum += number ** 3
    return sum
# sumNCubes(10)

def challenge1():
    n = int(input("Please enter a number for calulating sum and summing cubes >> "))
    print(f"The sum of the first {n} natural numbers is {sumN(n)}, and the sum of their cubes is {sumNCubes(n)}")
# challenge1()

# Write a program that implements Newton's method. The program should 
# prompt the user for thevalue to find the square root of (x) and the 
# number of times to improve the guess. Starting with aguess value of 
# x/2, your program should loop the specified number of times applying 
# Newton'smethod and report the final value of guess. 
# You should also subtract your estimate from the valueof math. 
# sqrt (x) to show how close it is.
import math
def challenge2():
    # Create the function nextGuess that returns the result of the Newton's method formula
    def nextGuess(guess, x): # The parameters are the previous guess and the number to sqrt().
        return (guess + (x / guess)) / 2

    x = eval(input("Enter the number you want to calculate the square root of >> "))
    numberOfImprovements = int(input("How many times you want to improve the answer? >> "))
    # Set the first guess as x / 2
    guess = x / 2
    # Start improving
    for i in range(numberOfImprovements):
        guess = nextGuess(guess, x)
    print(f"The approximation obtained is {guess}, which is {math.sqrt(x) - guess} close to the value using sqrt(x)")
challenge2()

