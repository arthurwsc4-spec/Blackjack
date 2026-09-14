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
        self.player_hand.append(card)
        self.deck_of_cards.remove(card)

    def calculate_hand_points(self, who="player"):
        total_points = 0
        if who == "player":
            hand = self.player_hand
        else:
            hand = self.machine_hand

        for elem in hand:
            try:
                total_points += int(elem[1])
            except:
                if elem[1] == "A":
                    return (total_points + 1, total_points + 11)
                else:
                    return total_points + 10
        return total_points, who

    def Stay(self): #turns to machine play
        pass

    def Restart(self):
        self.player_hand = []
        self.machine_hand = []
        self.deck_of_cards = self.build_deck()

    def Show_Hand_Points(self):
        print(f"{self.calculate_hand_points()[1]} points of your hand: {self.calculate_hand_points()[0]}")

    def blackjack(self, who="player"):
        if who == "player":
            if self.calculate_hand_points(who)[0] == 21:
                self.player_points += 1
        else:
            if self.calculate_hand_points(who)[0] == 21:
                self.machine_points += 1

    def bust(self, who="player"):
        if who == "player":
            points, person = self.calculate_hand_points(who)
        else:
            points, person = self.calculate_hand_points(who)

        if points > 21:
            if person == "player":
                self.player_points += 1
            else:
                self.machine_points += 1
        
    def winner(self):
        pass #decide who is the winner
