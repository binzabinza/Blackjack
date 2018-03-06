#!usr/bin/env python

#This is class for the Card object. A card is completely represented by its suit and ranks
#Seeing as this class is being used for a blackjack simulator, there is also a value associated with a card

class Card:
    suits = [u"\u2661", u"\u2664", u"\u2662", u"\u2667"] #HSDC
    ranks = [None, "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self, suit, rank):
        self.suit = self.suits[suit]
        self.rank = self.ranks[rank]

    def __str__(self):
        return self.rank + self.suit.encode('utf-8')

    def value(self):
        #Card value is the same as the rank, with the exception of face cards. These are valued as 10.
        #Aces (in Blackjack) are valued as 1 or 11 - this is handled by the blackjack class
        val = self.ranks.index(self.rank)
        if (val > 10):
            val = 10
        return val
