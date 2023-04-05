# Write a program that computes the fuel efficiency of a multi-leg journey. The
# program will first prompt for the starting odometer reading and then get information
# about a series of legs. For each leg, the user enters the current odometer reading and
# the amount of gas used (separated by a space). The user signals the end of the trip
# with a blank line. The program should print out the miles per gallon achieved on each
# leg and the total MPG for the trip.

def mpg(odometer_start, odometer_end, gas_used):
    return (odometer_end - odometer_start) / gas_used

def challenge1():
    odometer_reading = float(input("Enter the starting odometer reading: "))
    total_gas_used = 0.0
    total_distance = 0.0

    while True:
        leg = input("Enter the odometer reading and gas used (separated by a space), or press Enter to finish: ")
        if leg == "":
            break
        odometer_end, gas_used = map(float, leg.split())
        distance = odometer_end - odometer_reading
        leg_mpg = mpg(odometer_reading, odometer_end, gas_used)
        print("Leg MPG: {:.2f}".format(leg_mpg))
        total_distance += distance
        total_gas_used += gas_used
        odometer_reading = odometer_end

    total_mpg = mpg(0, total_distance, total_gas_used)
    print("Total MPG: {:.2f}".format(total_mpg))

# challenge1()

# The Goldbach conjecture asserts that every even number is the sum of two prime
# numbers. Write a program that gets a number from the user, checks to make sure that
# it is even, and then finds two prime numbers that add up to the number.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(n):
    for i in range(2, n):
        if is_prime(i) and is_prime(n - i):
            return (i, n - i)
    return None
def challenge2():
    num = int(input("Enter an even number: "))
    if num % 2 != 0:
        print("The number should be even.")
    else:
        primes = find_primes(num)
        if primes:
            print("{} = {} + {}".format(num, *primes))
        else:
            print("No such primes found.")

challenge2()