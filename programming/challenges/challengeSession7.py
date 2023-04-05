# Write a program that computes and outputs the nth 
# Fibonacci number, where n is a value entered 
# by the user.

# I will search for the formula of the nth element on
# Internet, and import math library to compute it in the 
# print() function.  

import math

def challenge1():
    n = int(input("Please enter a number >> "))

    # The formula of nth Fibonacci num. integerized.
    y = int(((1 + math.sqrt(5))**n - (1 - math.sqrt(5))**n) / (2**n * math.sqrt(5)))    
    print(f"The {n}th number of the Fibonacci sequence is {y}")

# challenge1()

#  Write a program that uses a while loop to determine how long it takes 
#  for an investment to double at a given interest rate. The input will be an 
#  annualised interest rate, and the output is the number of years it takes
#  an investment to double.

def challenge2():
    annualInterestRate = eval(input("Enter the annual interest rate to consider (currency%/year) >> "))
    initialMoney = eval(input("Enter the initial amount of money invested (currency) >> "))
    accumulatedMoney = initialMoney
    yearsCounted = 0
    while accumulatedMoney < (2 * initialMoney):
        yearsCounted += 1
        accumulatedMoney *= 1 + (annualInterestRate/100)
    print(f"""It would take {yearsCounted} years for an investment of 
${initialMoney} principal and an annual interest rate of {annualInterestRate}% to double.""")

# challenge2()