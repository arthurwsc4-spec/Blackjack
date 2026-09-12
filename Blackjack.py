import random

class Blackjack():
    def __init__(self):
        self.player_points = 0
        self.machine_points = 0
        self.player_hand = []
        self.machine_hand = []
        self.deck_of_cards = self.build_deck()

    def build_deck(self):
        suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
        numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return [(s, n) for s in suits for n in numbers]

    def Hit(self):
        card = random.choice(self.cards)
        self.player_hand.append(card)
        self.deck_of_cards.remove(card)

    def Stay(self):
        pass

    def Restart(self):
        self.hand = 0

    def Show_Points(self):
        pass
