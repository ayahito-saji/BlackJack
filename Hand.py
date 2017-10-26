from Deck import *
from PlayingCard import *

class Hand(Deck):
    def __init__(self):
        super().__init__()
        self.clear()
    def score(self):
        a_number = 0
        score = 0

        for card in self:
            if card.number == 1:
                a_number += 1
            elif 2 <= card.number <= 10:
                score += card.number
            elif 11 <= card.number <= 13:
                score += 10

        if score + 10 + a_number <= 21: return score + 10 + a_number
        else: return score + a_number

if __name__=='__main__':
    hand = Hand()
    hand.insert(PlayingCard("S", 1))
    hand.insert(PlayingCard("S", 10))
    hand.insert(PlayingCard("S", 1))
    hand.insert(PlayingCard("S", 1))
    print(hand)
    print(hand.score())