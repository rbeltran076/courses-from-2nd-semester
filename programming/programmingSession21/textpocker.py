from pockerapp import PockerApp

class TextInterface:

    def __init__(self):
        print("Welcome to video pocker")

    def setMoney(self, amt):
        print(f"You currently have ${amt:0}")

    def setDice(self, values):
        print("Dice: ", values)

    def wantToPlay(self):
        ans = input("You wanna try your luck?")
        return ans[0] in "yY"

    def close(self):
        print("\nThanks for playing!")

    def showResult(self, msg, score):
        print(f"{msg:0}, You win ${score:1}")

    def chooseDice(self):
        return eval(input("Enter list of which to change ([] to stop)"))

inter = TextInterface()
app = PockerApp(inter)
app.run()

