# Ronald Beltran BCSAI B
# Version of convert function that welcomes the user
def challenge1():
    userName = input("Enter your name: ")
    print("Welcome", userName)
    celcius = eval(input('What is the celcius temperature? '))
    farenheit = (5/9) * celcius + 32
    print('The temperature in farenheit is', round(farenheit, 3), 'degrees farenheit')

# Call function challenge1
challenge1()

# Function that inputs 5 numbers from the user, prints their addition and their average, using simultaneous assignment.
def challenge2and3():
    a, b, c, d, e = eval(input('Enter 5 numbers separated by commas: '))
    print('The addition of the numbers is', a + b + c + d + e)
    print('The average of the numbers is', (a + b + c + d + e)/5)

# Call challenge2 function
# challenge2()

# Function that converts degrees Farenheit to Celsius.
def challenge4():
    celsius = eval(input('Enter value in degrees Celsius: '))
    farenheit = celsius * 1.8 + 32
    print('The equivalent in degrees Farenheit is', farenheit)

# Call challenge4 funtion
# challenge4()

# Funtion that converts miles from kilometers
def challenge5():
    kilometers = eval(input('Enter value in kilometers: '))
    print('The equivalent in miles is', round(kilometers * 0.62, 2))

# Call challenge5 funtion 
# challenge5()

# Funtion that converts calories to joules
def challenge6():
    calories = eval(input('Enter the number of calories: '))
    print('The equivalent in joules is:', calories * 4.184)

# Call challenge6 function
# challenge6()

# Funtion chaos() edited so that it asks the user how many numbers should it print and doing that.
def challenge7():
    n = eval(input('Enter how many numbers should the program print: '))
    print()
    print('This program illustrates a chaotic function')
    x = eval(input('Enter a number between 0 and 1: '))
    for i in range(n):
        x = 3.9 * x * (1-x)
        print(x)

# Call the challenge7 function
# challenge7()

# Another version of chaos() funtion where instead of just one value of x, there are 2, x and y.
def challenge8():
    n = eval(input('Enter how many numbers should the program print: '))
    print()
    print('This program illustrates a chaotic function')
    x = eval(input('Enter the first number between 0 and 1: '))
    y = eval(input('Enter the second number between 0 and 1: '))
    for i in range(n):
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)
        print(round(x, 4), round(y, 4))

# Call the challenge8 funtion
# challenge8()    