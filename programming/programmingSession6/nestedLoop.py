# nestedLoop() Creates a blank test for a student
# This demonstrates how a nested loop can work
# Uses both for and while loops

def nestedLoop1():
    print("Name:\nDate:\n\nSelect the correct answer.\n")
    qNumber = 1
    while qNumber <= 10:
        print(f"Question {qNumber}")
        for qletter in ["a", "b", "c", "d", "e"]:
            print(qletter)
        print()
        qNumber += 1

# nestedLoop1()

def nestedLoop2():
    print("Name:\nDate:\n\nSelect the correct answer.\n")
    for qNumber in range(1, 11):
        print(f"Question {qNumber}")
        for qletter in ["a", "b", "c", "d", "e"]:
            print(qletter)
        print()

nestedLoop2()