# Program to take the average of a set of numbers 
# Illustrates interactive loop with 2 accumulators

def average1():
    sum = 0
    count = 0
    moreData = 'yes'

    while moreData[0] == 'y':
        x = float(input('Enter a number >> '))
        sum += x
        count += 1
        moreData = str(input('Will you input more numbers? (yes or no) >> '))
    print(f'\nThe average of the number is {sum/count}')
    print()

# average1()

# Illustrates sentinel loop using negative 
# input as sentinel

def average2():
    sum = 0
    count = 0
    x = float(input('Enter a number (negative to quit) >> ')) # This is a priming read
    # Priming read is something that we use in the sentence to
    # control how the program behaves over time
    while x >= 0:
        sum += x 
        count += 1
        x = float(input('Enter a number (negative to quit) >> ')) # priming read
    print(f'\nThe average of the numbers is {sum/count}')

# average2()

def average3():
    sum = 0
    count = 0
    answer = input('Enter a number (<Enter> to quit) >> ')
    while answer != "":
        number = float(answer)
        sum += number
        count += 1 
        answer = input('Enter a number (<Enter> to quit) >> ')
    if count == 0: print('There was no input you funny')
    else: print(f'\nThe average of the number is {sum/count}')
    
# average3()