# Function that compares 3 numbers 
# and determines which one is the maximum

def maxOf3Comparison():
    n1, n2, n3 = eval(input('Please enter 3 numbers separated by a comma:'))
    print()
    if n1 >= n2 and n1 >= n3:
        maxval = n1
    elif n2 >= n1 and n2 >= n3:
        maxval = n2
    else:
        maxval = n3
    print(f'The maximum value is {maxval:.2f}')

maxOf3Comparison()


# Make the same function with the decision tree
# algorithm

def maxOf3DecisionTree():
    n1, n2, n3 = eval(input('Please enter 3 numbers separated by a comma:'))
    print()
    if n1 >= n2:
        if n1 >= n3:
            maxval = n1
        else:
            maxval = n3
    else:
        if n2 >= n3:
            maxval = n2
        else:
            maxval = n3
    print()
    print(f'The maximum value is {maxval:.2f}')

maxOf3DecisionTree()