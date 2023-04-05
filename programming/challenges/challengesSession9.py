#  Write a program that counts the number of words in a sentence entered by the user.

def challenge1():
    sentence = str(input("Please enter a string >> ")).split()
    print(f"The number of words in the sentence was {len(sentence)}")
# challenge1()

# Write a program that allows the user to type in a phrase and then outputs
# the acronym for that phrase. Note: The acronym should be all uppercase, even if the
# words in the phrase are not capitalized

def challenge2():
    sentence = str(input("Please enter a string >> ")).split()
    acronymCharacters = []
    for word in sentence:
        acronymCharacters.append(word[0])
    print(f"An acronym for the sentence could be {''.join(acronymCharacters).upper()}")
# challenge2()


# Write a program that calculates the average word length in a sentence entered by
# the user.

def challenge3():
    sentence = str(input("Please enter a string >> ")).split()
    totalWordLength = 0
    for word in sentence:
        totalWordLength += len(word)
    print(f"The average word length for the sentence is {totalWordLength / len(sentence)}")
# challenge3()