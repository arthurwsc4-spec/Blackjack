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
        deck = [(s, n) for s in suits for n in numbers for _ in range(2)]
        random.shuffle(deck)
        return deck

    def Hit(self, who="player"):
        card = random.choice(self.deck_of_cards)
        if who == "player":
            self.player_hand.append(card)
        else:
            self.computer_hand.append(card)
        self.deck_of_cards.remove(card)

    def Calculate_Hand_Points(self, who="player"):
        total_points = 0
        aces = 0

        if who == "player":
            hand = self.player_hand
        else:
            hand = self.computer_hand

        for elem in hand:
            if elem[1] in ['J', 'Q', 'K']:
                total_points += 10
            elif elem[1] == 'A':
                total_points += 11
                aces += 1
            else:
                total_points += int(elem[1])

        while total_points > 21 and aces > 0:
            total_points -= 10
            aces -= 1
            
        return total_points, who

    def Stay(self):
        while self.Calculate_Hand_Points(who="computer")[0] < 18:
            self.Hit(who="computer")
        self.Winner()

    def Restart(self):
        self.player_hand = []
        self.computer_hand = []
        self.deck_of_cards = self.Build_Deck()

    def Show_Hand_Points(self):
        points, person = self.Calculate_Hand_Points()
        print(f"\nHand points of {person}: {points}")

    def blackjack(self, who="player"): #this is the only one in lower case so it makes harder to make confusions with the name of the class
        if who == "player":
            if self.Calculate_Hand_Points(who)[0] == 21:
                self.player_points += 1
        else:
            if self.Calculate_Hand_Points(who)[0] == 21:
                self.computer_points += 1
        
    def Winner(self):
        player, _ = self.Calculate_Hand_Points(who="player")
        computer, c = self.Calculate_Hand_Points(who="computer")
        winner_status = False

        if player > 21 and computer > 21:
            print('Both players busted, no winners!')
            winner_status = True

        if player > 21:
            winner_status = True
            print(f'{red}Player has busted, Computer won!{reset}')
        if player == 21:
            self.blackjack(who="player")
            winner_status = True

        if computer > 21:
            winner_status = True
            print(f'{green}Computer has busted, Player has won!{reset}')
        if computer == 21:
            self.blackjack(who="computer")
            winner_status = True

        if not winner_status:
            if player > computer:
                self.player_points += 1
            elif computer > player:
                self.computer_points += 1
            else:
                print(f"{yellow}It seems to be a Tie!{reset}")
                self.Restart()
        else:
            print(f"\n\n{green}We got a winner!!{reset}")
            print(f"\nThe score now is: player = {self.player_points} and computer = {self.computer_points}")
        self.Restart()

#colors for the code
red = '\033[91m'
green = '\033[92m'
yellow = '\033[33m'
reset = '\033[0m'

if __name__ == "__main__":
    player = Blackjack()
    play = input("Would you like to play Blackjack? (y or n) ")
    if play == "y":
        while True:
            player.Show_Hand_Points()
            move = input(f"What would you like to do? {green}Hit{reset} or {red}Stay{reset}? ").capitalize()
            if "Hit" in move:
                player.Hit()
            elif "Stay" in move:
                player.Stay()
                again = input("Wanna play another round?")
                if again == "y":
                    continue
                else:
                    break
            else:
                print(f"{red}Move Unavailable, choose again.{reset}")
