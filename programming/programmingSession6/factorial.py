# Program that computes the factorial of a number
# Illustrates the loop with an accumulator

def factorial():
    n = eval(input('Please enter a whole number >> '))
    factorial = 1
    for factor in range(n, 1, -1):
        factorial *= factor
        print(f"The factorial of {n} is {factorial}")

factorial()
