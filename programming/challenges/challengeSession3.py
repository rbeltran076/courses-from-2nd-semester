# Ronald Beltran BCSAI B

# 1.- Modify the convert.py program so that it computes and 
# prints a table of Celsius temperatures and the Fahrenheit 
# equivalents every 10 degrees from 0°C to 100°C.

from decimal import ROUND_HALF_EVEN

def challenge1():
    userName = input("Enter your name: ")
    print("Welcome", userName)
    for number in range(11):
      celcius = number * 10
      farenheit = (5/9) * (10 * celcius) + 32
      print(f'{celcius:.2f} celcius is {farenheit:.2f} in farenheit')

# challenge1()

# 2.- The program should prompt the user for the 
# yearly rate (rate) and the number of times that the interest is 
# compounded each year (periods). To compute the value in ten 
# years, the program will loop 10 * periods times and accure
# rate/period interest on each iteration.

def challenge2():
  rate = float(input("Enter the yearly rate: "))
  periods = int(input("Enter the number of times the interest is compounded per year: "))

  principal = 1
  for i in range(10 * periods):
      principal *= 1 + rate / periods
      # principal = principal + principal * (rate / periods)
      # principal = principal + (1 + rate/periods)

  print("The value after 10 years is", principal)

# challenge2()

