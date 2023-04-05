# A program that prints the abbreviation of a month, given its number

def month():
    # months is used as a lookup variable
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"

    n = int(input('Enter a month number (1 - 12) >> '))

    # Compute compute the starting position of month n in months
    pos = (n - 1) * 3
    monthAbbreviation = months[pos:pos + 3]
    print(f"The month abbreviation is {monthAbbreviation}")

# month()

# A version of month() usin list data type
def month2():
    # Month is a list used as a lookup table
    months = ["Jan", "Feb", "May", "Apr", "May", "Jun", 
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    n = int(input("Enter a month number (1 - 12) >> "))
    print(f"The month abbreviation is {months[n -1]}")

month2()