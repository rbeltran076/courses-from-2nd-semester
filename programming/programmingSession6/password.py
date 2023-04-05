# Uses a while loop to ask for the password
# until the correct one is input

def password():
    password = ""
    while password != "programming":
        password = input("Enter the password >> ")
    print('OKY-DOWkY! c:')
    print()
# password()

# This program uses break for input validation

def password2():
    while True:
        password = input('Enter the password >>')
        if password == 'programming': break
    print("OKI DOKY! c:")
    print()
# password2()