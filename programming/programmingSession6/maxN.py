# determine the maximum of a series of numbers

def maxN():
    n = int(input('How many numbers are there? '))

    # Set max to be the first value
    max = float(input('Enter a number >> '))

    # Now compare the n-1 successive values
    for i in range(n-1):
        x = float(input('Enter a number >> '))
        if x > max:
            max = x

    print(f'The largest number is {max}')

maxN()

