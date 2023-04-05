# Function that finds reversed words
def excercise1():
    # Create the list of words
    output = []
    list = ["I", "know", "you", "love", "me", "baby", "ooh", "yeah", "radar", "civic", "mom", "noon", "level", "refer", "rotator"]
    for word in list:
        if list(word).reverse() == list(word):
            output.append(word)
        return output
print(excercise1())

list = [1,2,3,4,5,6]

# Function that squares a list of numbers
def squareEach(nums):
    squaredNums = []
    for i in range(len(nums)):
        nums[i] = (nums[i] ** 2)
    return nums
# print(squareEach([1,2,3,4,5,6,7]))

# Function that sums all the numbers in a list
def sumList(nums):
    addedNums = sum(nums)
    return addedNums
# sumList([1,2,3,4,5,6,7])

# Function that transforms a list of strings into a list of numbers
def toNumbers(strList):
    numList = []
    for i in range(len(strList)):
        strList[i] = len(strList[i])
    return strList
toNumbers(["hi", "bye"])

# Function that computes the sum of squares of numbers read from a text file
def ex2():
    filename = str(input('Enter a file name >> '))
    with open(filename, "r") as infile:
        print(sumList(squareEach(toNumbers(list(infile.read()))))

# ex2()
    