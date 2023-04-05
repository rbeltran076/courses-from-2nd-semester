# This is a function to describe multiple
def spameggs():
    spam, eggs = eval(input('Enter number of spam and of eggs: '))
    print("You ordered", eggs, "eggs, and", spam, "spam.")

# A function that has nothing to do with spamEggs but calculates the value of an investment carried 10 years in the future
def main():
    print("This program calculates the final value of a 10 year investment")
    value = eval(input('Enter the initial value of investment'))
    annualInterestRate = eval(input('Enter the annual interest rate'))

    for i in range(10):
        value = value + (1 + annualInterestRate)
        print(value)

    print('The final value of the investment is this one')

main()
