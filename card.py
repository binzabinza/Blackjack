#!usr/bin/env python

class Card:
    suits = [u"\u2661", u"\u2664", u"\u2662", u"\u2667"] #HSDC
    ranks = [None, "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self, suit, rank):
        self.suit = self.suits[suit]
        self.rank = self.ranks[rank]

    def display(self):
        return self.rank + self.suit
