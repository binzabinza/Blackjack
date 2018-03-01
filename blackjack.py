#!usr/bin/env python

from deck import *

class Blackjack:
    def __init__(self, deck_num):
        self.shoe = Deck(deck_num)
        self.shoe.shuffle()

    def __str__(self):
        disp = "Dealer's hand: ?? " + str(self.dealer_hand[1]) + str(self.value(self.dealer_hand)) + "\n    Your hand: "
        for card in self.player_hand:
            disp += str(card) + " "
        disp += "  " + str(self.value(self.player_hand))
        return disp

    def deal(self):
        self.dealer_hand = [self.shoe.deal(), self.shoe.deal()]
        self.player_hand = [self.shoe.deal(), self.shoe.deal()]

    def hit(self, hand):
        hand.append(self.shoe.deal())

    def value(self, hand):
        val = 0
        ace = 0 #boolean
        for card in hand:
            if (card.value() == 1):
                ace = 1
                val += 11
            else:
                val += card.value()
            if (val > 21 and ace):
                ace = 0
                val -= 10
        return val

game = Blackjack(2)
game.deal()

while(game.value(game.player_hand) < 21):
    print game
    action = raw_input()
    
    if (action == 'h'):
        game.hit(game.player_hand)
    elif (action == 's'):
        break

while (game.value(game.dealer_hand) <= 16):
    game.hit(game.dealer_hand)

print game
if (game.value(game.player_hand) <= 21 and game.value(game.player_hand) > game.value(game.dealer_hand)):
    print "VICTORY"
elif (game.value(game.player_hand) == game.value(game.dealer_hand)):
    print "PUSH"
else:
    print "SAD!"
