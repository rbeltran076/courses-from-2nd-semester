# The  wrote that this is a wrong solution
from graphics import *
def eyes1():
    win = GraphWin()
    leftEye = Circle(Point(80, 50), 5)
    leftEye.setFill("red")
    leftEye.setOutline("yellow")
    leftEye.draw(win)
            
    Circle(Point(80, 50), 5)
    rightEye = leftEye
    rightEye.move(20, 0)

def eyes2():
    win = GraphWin()
    leftEye = Circle(Point(80, 50), 5)
    leftEye.setFill("red")
    leftEye.setOutline("yellow")

    rightEye = leftEye.clone()
    rightEye.move(20, 0)
    rightEye.draw(win)
    win.getMouse()

eyes2()