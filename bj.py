
from deck import *

class Blackjack:
    def __init__(self, num_decks = 1):
        self.shoe = []
        for d in range(num_decks):
            tempdeck = Deck()
            tempdeck.display()
            self.shoe.append(tempdeck.shuffle())
