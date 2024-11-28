import random

cards_player = ['A', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 'J', 'Q', 'K']
cards_dealer = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

logo = '''
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
                       _/ |                
                      |__/                 
'''

def dealer():
    return random.choice(cards_dealer)

def player():
    return random.choice(cards_player)

def game(money):
    while money > 0:  # Keep playing as long as the player has money
        player_cards = []
        dealer_cards = []
        player_initial_card = player()
        player_initial_card = str(player_initial_card)
        dealer_initial_card = dealer()
        dealer_initial_card = str(dealer_initial_card)
        player_cards.append(player_initial_card)
        dealer_cards.append(dealer_initial_card)
        pot = 0
        
        print(logo)
        print(f"""
        Welcome to Black Jack
        We are giving out initial cards
        Your first card is {player_initial_card}
        Computer has got their initial card
        Your starting money is ${money}""")
        print("The initial bet is $25")
        
        bets_player = input("Would you like to 'Raise' the bet or 'Stay' the same?\n").lower()
        
        if bets_player == "raise":
            try:
                player_money = int(input("Enter the amount you want to raise the bet for\n$"))
                while player_money > money or player_money < 25:
                    print("Please enter a valid bet amount.")
                    player_money = int(input("Enter the amount you want to raise the bet for\n$"))
                money -= player_money
                pot = player_money * 2
                print(f"Your current money is ${money}, and the money on the pot is ${pot}")
            except ValueError:
                print("Please enter a valid number.")
                continue  # Go to the next loop iteration if invalid input
        
        elif bets_player == "stay":
            pot = 50
            print(f"No raises by player, actual money on the pot is ${pot}")
        
        player_second_card = player()
        player_second_card = str(player_second_card)
        dealer_second_card = dealer()
        dealer_second_card = str(dealer_second_card)
        player_cards.append(player_second_card)
        dealer_cards.append(dealer_second_card)
        
        print(f"""
        Your second card is {player_second_card}
        Your total now is {", ".join(player_cards)}
        Computer's second card is {dealer_second_card}
        Computer's cards are __ and {dealer_second_card}""")
        
        second_pot = pot * 1.5
        print(f"Second bets are going out, the money in the pot is ${pot}, the current bet is ${second_pot}")
        
        bets_player = input("Would you like to 'Raise' the bet or 'Stay' the same?\n").lower()
        
        if bets_player == "raise":
            try:
                player_money = int(input("Enter the amount you want to raise the bet for\n$"))
                while player_money > second_pot:
                    print(f"Please enter a bet less than or equal to ${second_pot}")
                    player_money = int(input("Enter the amount you want to raise the bet for\n$"))
                money -= player_money
                pot = player_money * 2
                print(f"Your current money is ${money}, and the money on the pot is ${pot}")
            except ValueError:
                print("Please enter a valid number.")
                continue

        elif bets_player == "stay":
            pot = second_pot
            print(f"No raises by player, actual money on the pot is ${pot}")
        
        choice = input("Would you like to get another card?\n").lower()
        while choice == "yes":
            extra_card = player()
            extra_card = str(extra_card)
            player_cards.append(extra_card)
            print(f"You decided to get another card that is {extra_card}, your cards are {', '.join(player_cards)}")
            choice = input("Would you like to get another card?\n").lower()

        print(f"Your final hand: {', '.join(player_cards)}")
        
        # Handling Aces and face cards values
        total_player = 0
        for card in player_cards:
            if card in ['J', 'Q', 'K']:
                total_player += 10
            elif card == 'A':
                if total_player + 11 <= 21:
                    total_player += 11
                else:
                    total_player += 1
            else:
                total_player += int(card)
        
        total_dealer = 0
        for card in dealer_cards:
            if card in ['J', 'Q', 'K']:
                total_dealer += 10
            elif card == 'A':
                if total_dealer + 11 <= 21:
                    total_dealer += 11
                else:
                    total_dealer += 1
            else:
                total_dealer += int(card)
        
        print(f"Dealer's cards: {', '.join(dealer_cards)}")

        if total_dealer < 17:
            extra_card = dealer()
            total_dealer += extra_card
            print(f"The dealer's total is less than 17, so they draw a card: {extra_card}, new total is {total_dealer}")
        
        if total_player > 21:
            print(f"You went over 21! You lost.")
            money -= pot
        elif total_dealer > 21:
            print(f"The dealer went over 21! You win!")
            money += pot
        elif total_player > total_dealer:
            print(f"You win with {total_player}! The dealer had {total_dealer}.")
            money += pot
        elif total_player < total_dealer:
            print(f"You lose with {total_player}! The dealer had {total_dealer}.")
            money -= pot
        else:
            print("It's a draw")
            
        if money <= 0:
            print("You're out of money! Game over.")
            break
        repeat_game = input("Would you like to play again? (yes/no)\n").lower()
        if repeat_game != "yes":
            print("Thanks for playing!")
            break

game(1000)
