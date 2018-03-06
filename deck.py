#!usr/bin/env python

#This is the class for the Deck object. A deck is described as a collection of cards. By default this is assumed to be the standard 52 cards
#The optional parameter deck_num can be used to create a "shoe" consisting of multiple decks

import random
from card import *

class Deck:
    def __init__(self, deck_num = 1):
        self.cards = []
        for _ in range(deck_num):
            for suit in range(4):
                for rank in range(1, 14):
                    self.cards.append(Card(suit, rank))

    def __str__(self):
        disp = '['
        for card in self.cards:
            disp = disp + card.rank + card.suit.encode('utf-8') + ','
        disp += ']'
        return disp

    def deal(self):
        #This will remove the top card of the deck and return it to the caller
        return self.cards.pop()

    def shuffle(self):
        #This will shuffle and randomize the order of the cards
        random.shuffle(self.cards)
