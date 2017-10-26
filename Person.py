from Hand import *
from Deck import *

class Person:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def score(self):
        return self.hand.score()

    def draw(self, deck):
        c = deck.draw()
        self.hand.insert(c)