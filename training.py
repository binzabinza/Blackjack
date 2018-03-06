from blackjack import *

game = Blackjack()

while(len(game.shoe.cards) > 10):
    game.place_bet()
    game.deal()
    game.player_action()
    game.dealer_action()
    game.payout()
