# A program to convert a textual message into a sequence of numbers,
# using the underlying unicode enconding.

def text2numbers():
    print("""This program converts a textual message into a sequence of numbers representing
the Unicode encoding of the message.""")

    # Get the message to encode
    message = input("Please enter the message to encode >> ")
    print(f"\nHere are the Unicode codes")

    # 
    for ch in message:
        print(ord(ch), end = " ")
    print()

# text2numbers()

def numbers2text():
    print("""This program converts a sequence of numbers representing
the Unicode encoding of the message, into the message.""")
    string = input("\nEnter the Unicode - encoded message >> ")
    
    # Loop though each substring and build the Unicode message
    message = ""
    for substring in string.split():
        # Convert the substring to a number
        codeNum = int(substring)

        # Append character to message
        message += chr(codeNum)

    print(f"\nThe encoded message is {message}")

# numbers2text()

def numbers2text2():
    print("""This program converts a sequence of numbers representing
the Unicode encoding of the message, into the message.""")
    string = input("\nEnter the Unicode - encoded message >> ")

    # Loop through each substring and build unicode message
    characters = []
    for substring in string.split():
        codeNumber = int(substring)             # Convert digits into numbers
        characters.append(chr(codeNumber))      # Add new character
        message = "".join(characters)           # Joins chars with "" as a separator
        print(f"The decoded message is {message}")

