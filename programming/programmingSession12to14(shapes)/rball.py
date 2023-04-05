# simulation of a racquetball game
from random import random

def printIntro():
    print("""
This program simulates a racquetball game between two 
players (A and B) in a number of times (n).
The abilities for each player are indicated with a probabily (number between 0 and 1 inclusive)
that the player wins the point when serving. Player A always has the first move.
""")
    
def getInputs():
    # Returns the three simulation paramters
    a = float(input("What is the probability that the player A wins a point when serving? "))
    b = float(input("What is the probability that the player B wins a point when serving? "))
    n = int(input("How many serves are in the game? "))
    return a, b, n

def simNGames(n, probA, probB):
    # Simulates n games of raquetball between players whose
    # abilities are represented by the probability of winning a serve
    # Returns number of wins for A and B
    winsA = winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
        return winsA, winsB

def simOneGame(probA, probB):
    # Simulates a single game or raquetball between players whose
    # abilities are represented by the probability of winning a serve
    # Returns scores of A and B after one game
    serving = "A"
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA: # A wins the serve
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random() < probB: # B wins the serve
                scoreB = scoreB + 1
            else:
                serving = "A"
    return scoreA, scoreB

def gameOver(a, b):
    # a and b are the scores of each player
    # Returns true if the game is over, False otherwise
    return a == 15 or b == 15

def printSummary(winsA, winsB):
    # Prints a summary of wins for each player
    n = winsA + winsB
    print(f"""
Games simulated: {n}
Wins for A {winsA:.2f}
Wins for B {winsB:.2f}
""")
    
def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)
main()
