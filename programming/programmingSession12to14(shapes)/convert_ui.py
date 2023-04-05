# the convert function applied in the window

from graphics import *
def main():
    win = GraphWin("Celcius converter", 400, 300)
    win.setCoords(0.0, 0.0, 3.0, 4.0)

# draw the interface
    Text(Point(1, 3), "  Celcius Temperature:").draw(win)  
    Text(Point(1, 3), "Farenheit Temperature:").draw(win)
    inputText = Entry(Point(2.25, 3), 5)
    inputText.setText("0.0")
    inputText.draw(win)
    outputText = Text(Point(2.25, 1))
    outputText.draw(win)
    button = Text(Point(2.25, 1), "")
    button.draw(win)
    Rectangle(Point(1, 1.5), Point(2, 2.5)).draw(win)
    win.getMouse()  # Wait for a mouse click

    # convert input
    celcius = float(inputText.getText())
    farenheit = 9.0/5.0 * celcius + 32

    # display output and change button
    outputText.setText(round(farenheit, 2))
    button.setText("")

    win.getMouse()

main()