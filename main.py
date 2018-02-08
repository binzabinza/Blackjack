#!usr/bin/env python

from deck import *


deck = Deck()
deck.shuffle()
dhand = [deck.deal(), deck.deal()]

print "Dealer's hand: ??", dhand[1].display()
print "Your hand    :", deck.deal().display(), deck.deal().display()
