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
        card = random.choice(self.deck_of_cards)
        self.player_hand.append(card[1])
        self.deck_of_cards.remove(card)

    def calcule_points(self):
        total_points = 0
        for elem in self.player_hand:
            try:
                total_points += int(elem[1])
            except:
                if elem[1] == "A":
                    return (total_points + 1, total_points + 11)
                else:
                    return total_points + 10

    def Stay(self):
        pass

    def Restart(self):
        self.hand = 0
        self.deck_of_cards = self.build_deck

    def Show_Points(self):
        pass

    def blackjack(self):
        pass #if hand == 21
