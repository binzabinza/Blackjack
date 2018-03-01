#!usr/bin/env python

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
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)
