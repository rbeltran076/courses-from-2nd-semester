# Challenge 1. Create a class to represent spheres.
# with methods to: get radius, compute surface area, and compute volume
import math
class Sphere:

    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius
    
    def surfaceArea(self):
        return 4 * math.pi * (self.radius ** 2)
    
    def volume(self):
        return (4 / 3) * math.pi * self.radius ** 3
    
# Challenge 2. Create a class to represent cubes with the same 
# Sphere class methods.
class Cube:

    def __init__(self, side):
        self.side = side
    
    def getSide(self):
        return self.side
    
    def surfaceArea(self):
        return (self.side ** 2) * 6
    
    def volume(self):
        return self.side ** 3

# Write a program to play "Three Button Monte." 
# Your program should draw three buttons labeled "Door 1' " 
# " Door 2' " and "Door 3" in a window and randomly select one of 
# the buttons (without telling the user which one is selected). 
# The program then prompts the user to click on one of the buttons. 
# A click on the special button is a win, and a click on one of the 
# other two is a loss. You should tell the user whether they won or 
# lost, and in the case of a loss, which was the correct button. Your
# program should be entirely graphical; that is, all prompts and 
# messages should be displayed in the graphics window.
#three-button-monte game, original simple version
#draws three buttons labeled "door 1," "door 2," "door 3"
#user is prompted and selects one of the buttons
#user clicks one of the buttons and is advised whether he/she won or lost.

from random import randrange 
# I imported the graphics and button files to use them in this program
# I also edited the appearances of the button to 
# give the game an aesthetic design.
from graphics import *
from Button import Button

def Three_Button_Monte():
    #create the application window
    win = GraphWin("Three Button Monte", 250, 250)
    win.setCoords(0, 0, 6, 7)
    win.setBackground("black")

    # Create the buttons, the center location, wid, and height, 
    # and label are specified in the params.
    width, height = (1.3, 1)
    yCoord = 3.3
    door1 = Button(win, Point(1.5, yCoord), width, height, "1")
    door2 = Button(win, Point(3, yCoord), width, height, "2")
    door3 = Button(win, Point(4.5, yCoord), width, height, "3")
    quit = Button(win, Point(3, 0.7), width, height, "Quit Game")
    buttons = [door1, door2, door3, quit]
    for button in buttons: button.activate()

    # Setting the display
    label = Text(Point(3,5.5), 'Three Button Monte\n\nClick any door twice\nto start playing.')
    
    numberOfWins = 0
    numberOfLosses = 0
    displayOfWins = Text(Point(2, 1.7), f"Wins: {numberOfWins}")
    displayOfLosses = Text(Point(4, 1.7), f"Losses: {numberOfLosses}")

    # set uniform text style for the displays 
    displays = [displayOfLosses, displayOfWins, label]
    for d in displays:
        d.setFace("courier")
        d.setStyle("bold")
        d.setSize(10)
        d.setTextColor("white")
        d.draw(win)

    # Generating a random correct answer and
    # displaying it in the console for knowing it
    # doorprize = "Door " + str(randrange(1,4))
    doorprize = randrange(1, 4)
    x = win.getMouse()
    print(f"The point clicked was {x}")             # Print in terminal the coordinates clicked.  
    
    while quit.clicked(x) == False:
        doorprize = randrange(1, 4)
        print(f"\nthe correct door is {doorprize}")     # Print in terminal the correct door.
        x = win.getMouse()
        print(f"The point clicked was {x}")             # Print in terminal the coordinates clicked.

        # Display the messages according to the results.
        # If the door clicked is the same door as doorprize, the player wins.
        if (door1.clicked(x) == True and doorprize == 1) or (door2.clicked(x) == True and doorprize == 2) or (door3.clicked(x) == True and doorprize ==3):
            numberOfWins += 1
            label.setTextColor("light green") # Set green sext
            label.setText('Correct!\nThat was the right door.')
            displayOfWins.setText(f"Wins: {numberOfWins}")
        # If the door clicked and the doorprize do not match, the player loses.
        elif (door1.clicked(x) == True and doorprize !=1) or (door2.clicked(x) == True and doorprize !=2) or (door3.clicked(x) == True and doorprize !=3):
            numberOfLosses += 1 
            label.setTextColor("red") # set red text
            label.setText('Incorrect!\nThe correct door was ' + str(doorprize))
            displayOfLosses.setText(f"Losses: {numberOfLosses}")
        # If the player doesn't click a door, it misses and it's stoopid.
        else:
            label.setTextColor("white")
            label.setText('You missed.')

        # This is for testing which button the program
        # acknowledges to be pressed. Printed in terminal.
        print(f""""
    1 {door1.clicked(x)}
    2 {door2.clicked(x)}
    3 {door3.clicked(x)}""")
    
    
# Run the game
Three_Button_Monte()
