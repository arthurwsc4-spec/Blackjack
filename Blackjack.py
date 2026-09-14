import random

class Blackjack():
    def __init__(self):
        self.player_points = 0
        self.computer_points = 0
        self.player_hand = []
        self.computer_hand = []
        self.deck_of_cards = self.Build_Deck()

    def Build_Deck(self):
        suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
        numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return [(s, n) for s in suits for n in numbers for _ in range(2)]

    def Hit(self, who="player"):
        card = random.choice(self.deck_of_cards)
        if who == "player":
            self.player_hand.append(card)
        else:
            self.computer_hand.append(card)
        self.deck_of_cards.remove(card)

    def Calculate_Hand_Points(self, who="player"):
        total_points = 0
        if who == "player":
            hand = self.player_hand
        else:
            hand = self.computer_hand

        for elem in hand:
            try:
                total_points += int(elem[1])
            except:
                if elem[1] == "A":
                    return (total_points + 1, total_points + 11)
                else:
                    return total_points + 10
        return total_points, who

    def Stay(self):
        while self.Calculate_Hand_Points(who="computer")[0] < 18:
            self.Hit(who="computer")
        if self.Calculate_Hand_Points(who="computer")[0] >= 18:
            self.Winner()
        else:
            self.Hit(who="computer")

    def Restart(self):
        self.player_hand = []
        self.computer_hand = []
        self.deck_of_cards = self.Build_Deck()

    def Show_Hand_Points(self):
        print(f"{self.Calculate_Hand_Points()[1]} points of your hand: {self.Calculate_Hand_Points()[0]}")

    def Blackjack(self, who="player"):
        if who == "player":
            if self.Calculate_Hand_Points(who)[0] == 21:
                self.player_points += 1
        else:
            if self.Calculate_Hand_Points(who)[0] == 21:
                self.computer_points += 1

    def Bust(self, who="player"):
        if who == "player":
            points, person = self.Calculate_Hand_Points(who)
        else:
            points, person = self.Calculate_Hand_Points(who)

        if points > 21:
            if person == "player":
                self.player_points += 1
            else:
                self.computer_points += 1
        
    def Winner(self):
        player, _ = self.Calculate_Hand_Points(who="player")
        computer, c = self.Calculate_Hand_Points(who="computer")
        winner_status = False

        if player > 21:
            self.Bust(who="player")
            winner_status = True
        if player == 21:
            self.Blackjack(who="player")
            winner_status = True

        if computer > 21:
            self.Bust(who="computer")
            winner_status = True
        if computer == 21:
            self.Blackjack(who="computer")
            winner_status = True

        if not winner_status:
            if player > computer:
                self.player_points += 1
            elif computer > player:
                self.computer_points += 1
            else:
                print("It seems to be a Tie!")
                self.Restart()
        else:
            print("We got a winner")
            print("The score is: player = {self.player_points} and computer = {self.computer_points}")
