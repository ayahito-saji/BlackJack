import random
from PlayingCard import *

class Deck(list):
    def __init__(self):
        super().__init__()
        self.extend([PlayingCard(x, y) for x in PlayingCard.SUIT_LIST for y in range(1, 13+1)])
        self.shuffle()

    def draw(self):
        return self.pop()

    def shuffle(self):
        random.shuffle(self)

    def insert(self, card):
        i = random.randint(0, len(self))
        super().insert(i, card)
    def __str__(self):
        return " ".join(str(c) for c in self)

if __name__=='__main__':
    deck = Deck()
    print(deck)