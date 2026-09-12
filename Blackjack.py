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
        self.player_hand.append(int(card[1]))
        self.deck_of_cards.remove(card)

    def Stay(self):
        pass

    def Restart(self):
        self.hand = 0
        self.build_deck()

    def Show_Points(self):
        pass

    def blackjack(self):
        pass #if hand == 21

if __name__ == '__main__':
    player = Blackjack()
    game = input('Wanna play Blackjack? ')
    if game == 'y':
        if len(player.player_hand) > 1:
            total = 0
            for num in player.player_hand:
                total += num
            if num > 21:
                player.player_hand == total
                player.Stay()
            else:
                player.player_hand == total
                option = input(f'Hand: {player.player_hand}. Want to hit or want to stay?')
    else:
        print('Oh, so sad, bye then!')
