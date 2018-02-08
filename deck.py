#!usr/bin/env python

import random
from card import *

class Deck:
    def __init__(self):
        self.cards = []
        
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))

    def display(self):
        print '[',
        for card in self.cards:
            print card.display(), ',',
        print ']'

    def deal(self):
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)
