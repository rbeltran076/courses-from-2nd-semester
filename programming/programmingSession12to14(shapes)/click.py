
from graphics import *

def main():
    win = GraphWin()
    while True:
        p = win.getMouse()
        print(f"You clicked at {p.getX(), p.getY()}")
main()