from collections import Counter

def main():
    print("""This program analyzes word frequency in a file
and prints a report on the n most frequent words.""")

    # get the sequence of words from the file
    filename = input("File to analyze: ")
    text = open(filename, "r").read()
    text = text.lower()
    words = text.split()

    # construct a dictionary of word count
    counts = Counter(words)
    
    # output analysis of n most frequent words
    n = int(input("How many words should this program output? "))
    items = counts.most_common(n)
    for word, count in items:
        print("{0:15}{1:5}".format(word, count))

if __name__ == "__main__": main()