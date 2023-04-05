# Defining a class for an n sided dice

from random import randrange

class MSDice():

    def __init__(self, sides):
        self.sides = sides
        self.value = 1

    def roll(self):
        self.value = randrange(1, self.sides + 1)

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

dice1 = MSDice(6)
print(dice1.getValue())
print()
dice1.roll()
print(dice1.getValue())
print()
dice1.setValue(3)
print(dice1.getValue())
