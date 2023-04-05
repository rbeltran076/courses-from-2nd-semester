# Write a program that inputs a year, verifies that it is in proper range, 
# and then prints out the date of Easter that year

def challenge1():
    print()
    year = int(input("""Enter the year you want to see the date of the easter of 
(The year must be between the years 1982 and 2048) >> """))
    print()
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19*a + 24) % 30
    e = (2*b + 4*c + 6*d + 5) % 7
    if 2048 >= year >= 1982:
        if (d + e) > (31 - 22):
            print(f"The date of easter is April {(d + e) - 9}")
        else:
            print(f"The date of the easter is March {22 + d + e}")
    else:
        print('This year is not between 1982 and 2048')
    print()

# challenge1()

# Write a program that determines whether a year is a leap year.

def challenge2():
    year = int(input("""Enter the year you want to see the date of the easter of >> """))    
    if year % 4 == 0 and year % 400 == 0:
        print("yup")
    else:
        print("nope")

# challenge2()