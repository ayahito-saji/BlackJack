#!/usr/bin/env python3

import sys
from PlayingCard import *
from Hand import *
from Player import *
from Dealer import *


def output(player, score=False):
    if score:
        print("{0}:\t{1} = {2}".format(
            player.name, player.hand, player.score()))
    else:
        print("{0}:\t{1}".format(player.name, player.hand))


def game(deck, player, dealer):
    dealer.hand.clear()
    player.hand.clear()
    bet = 10
    print("Bet {0} coin(s)".format(bet))
    player.draw(deck)
    dealer.draw(deck)
    player.draw(deck)
    dealer.draw(deck)
    output(dealer)
    output(player, True)

    lose = False
    win = False
    tie = False
    yn = input("Hit or Stay? (h or s)")
    while yn in "hHyY":
        player.draw(deck)
        output(player, True)
        if player.score() > 21:
            lose = True
        yn = input("Hit or Stay? (h or s)")

    if not lose:
        print("Turn of the Dealer")
        output(dealer)
        while dealer.score() < 17:
            dealer.draw(deck)
            output(dealer)
            if dealer.score() > 21:
                win = True

        print("No more hit")
        output(dealer, True)
        output(player, True)

        if player.score() > dealer.score():
            win = True
        elif player.score() == dealer.score():
            tie = True
        else:
            lose = True

    if win:
        print("You Win")
        player.coin += bet
    elif tie:
        print("Tie")
    elif lose:
        print("You Lose")
        player.coin -= bet
    else:
        print("You Win or Lose?")
    print("You have {0} coins".format(player.coin))

deck = Deck()
deck.shuffle()

player = Player("You", 100)
dealer = Dealer()

yn = input("Do you play the game?(y/n)")
while yn == "y" or yn == "Y":
    game(deck, player, dealer)
    yn = input("Next Game? (y/n)")

print("Game End")