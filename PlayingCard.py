#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class PlayingCard :
    """definitio of Playing Card"""
#    SUIT_LIST = ('♣︎', '♢', '♡', '♠︎')
    SUIT_LIST = ('C', 'D', 'H', 'S')
    NUMBER_LIST = ('A','2','3','4','5','6','7','8','9','10','J','Q','K')

    def __init__(self, suit, number):
        """deconstructor of Playing Card"""
        self.suit = suit
        self.number = number

    def __str__(self):
        return self.suit + self.NUMBER_LIST[self.number - 1]

if __name__=='__main__':
    card = PlayingCard('C', 1)
    print(card)