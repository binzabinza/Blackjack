#!usr/bin/env python

#This is the class for the Blackjack object. The methods contained are everything needed to create a game of Blackjack
#It is currently configured for only one player

import os
from deck import *

class Blackjack:
    def __init__(self, deck_num, bankroll = 1000):
        self.shoe = Deck(deck_num)
        self.shoe.shuffle()
        self.deck_num = deck_num
        self.bankroll = bankroll
        self.end = 0
        self.count = 0

    def __str__(self):
        disp =  "\nDealer's hand: "
        if (self.end):
            for card in self.dealer_hand:
                disp += str(card) + " "
        else:
            disp += "?? " + str(self.dealer_hand[1])
        disp += "\n    Your hand: "
        for card in self.player_hand:
            disp += str(card) + " "
        disp += "  " + str(self.value(self.player_hand))
        return disp

    def deal(self):
        #deals out two cards to the dealer and to the player
        self.dealer_hand = [self.shoe.deal(), self.shoe.deal()]
        self.player_hand = [self.shoe.deal(), self.shoe.deal()]

        #adjusting the count
        self.running_count(self.player_hand[0])
        self.running_count(self.player_hand[1])
        self.running_count(self.dealer_hand[1])

    def hit(self, hand):
        #will add one card from the shoe to the passed hand
        card = self.shoe.deal()
        hand.append(card)
        self.running_count(card)

    def value(self, hand):
        #calculates the numerical value of the hand
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

    def running_count(self, card):
        #alters the class variable count to reflect the running count of the shoe
        if (card.value == 1 or card.value == 10):
            self.count -= 1
        elif (card.value < 7):
            self.count += 1

    def true_count(self):
        #calculates the true_count of the game. To be used for practicing card counting
        return self.count/deck_num

    def place_bet(self):
        #lets the player place a bet from their bankroll
        print "Bankroll: ${}".format(self.bankroll)

        bet = int(raw_input("Enter a bet: "))
        if (bet > self.bankroll):
            self.bet = self.bankroll
        else:
            self.bet = bet

        self.bankroll -= self.bet
        self.end = 0


    def player_action(self):
        while(self.value(self.player_hand) < 21):
            os.system('clear')
            print "Bankroll: ${}\nCurrent bet: {}".format(self.bankroll, self.bet)
            print self
            action = raw_input()

            if (action == 'h'):
                self.hit(self.player_hand)
            elif (action == 'd'):
                self.hit(self.player_hand)
                self.bet += self.bet
                self.bankroll -= self.bet
                break
            elif (action == 'p'):
                pass
            elif (action == 's'):
                break
        self.end = 1

    def dealer_action(self):
        #dealer draws to 17, stands on all 17s
        while (self.value(self.dealer_hand) <= 16):
            self.hit(self.dealer_hand)

    def payout(self):
        #rectifies all bets
        os.system('clear')
        print "Bankroll: ${}\nCurrent bet: {}".format(self.bankroll, self.bet)
        print self
        if (len(self.player_hand) == 2 and self.value(self.player_hand) == 21):
            self.bankroll += self.bet * 2.5
            self.bet = 0
        elif ((self.value(self.player_hand) <= 21 and self.value(self.player_hand) > self.value(self.dealer_hand)) or (self.value(self.player_hand) <= 21 and self.value(self.dealer_hand) > 21)):
            self.bankroll += self.bet * 2
            self.bet = 0
        else:
            self.bet = 0

        _ = raw_input("Press any key to continue...")
