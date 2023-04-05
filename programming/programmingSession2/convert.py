# A program that converts celcius to farenheit
from decimal import ROUND_HALF_EVEN


def main():
    userName = input("Enter your name: ")
    print("Welcome", userName)
    celcius = eval(input('What is the celcius temperature? '))
    farenheit = (5/9) * celcius + 32
    print('The temperature in farenheit is', round(farenheit,3), 'degrees farenheit')

main()