# A program that returns the number of the n most repeated words.

def byFreq(pair):
    return pair[1]

def main():
    print("""This program analyzes word frequency in a file
and prints a report on the n most frequent words.""")

    # get the sequence of words from the file
    filename = input("File to analyze: ")
    text = open(filename, "r").read()
    text = text.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
        text = text.replace(ch, " ")
    words = text.split()

    # construct a dictionary of word count
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    
    # output analysis of n most frequent words
    n = int(input("How many words should this program output? "))
    items = list(counts.items())
    items.sort()    # orders pairs alphabetically
    items.sort(key = byFreq, reverse = True)    # Orders by frequency
    for i in range(n):
        word, count = items [i]
        print("{0:15}{1:5}".format(word, count))

if __name__ == "__main__": main()