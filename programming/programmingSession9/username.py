# Using best practices
# String processing program that generates usernames

def username():
    print("This program generates computer usernames\n")

    # Get user first and last names
    first = str(input("Please enter the first name (all lowercase) >> "))
    last = str(input("Please enter the last name (all lowercase) >> "))

    # concatenate the first initial letter of the first name 
    # and 7 first characters of the last name.
    username = first[0] + last[:7]
    print(f"The username is {username}")

username()