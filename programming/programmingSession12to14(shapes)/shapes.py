# Before coding this, I believe that we are going to call a window that displays shapes
from graphics import *

def shapes():
    # open a graphics window
    window = GraphWin("Shapes")     # Constructor

    # draw a red circle centered at point (100,100) with radius 30
    center = Point(100, 100)    # Constructor
    circle = Circle(center, 30)     # Constructor
    circle.setFill("red")

    # Put the circle in the window
    circle.draw(window)

    # Put a textual label in the center of the circle
    label = Text(center, "WENAMAGCHIAINSAMA")
    label.draw(window)

    # Draw a square using a rectangle object and indicate 2 points (30,30) (70,70)
    rectangle = Rectangle(Point(30, 30), Point(70, 70))
    rectangle.draw(window)

    window.getMouse()

shapes()