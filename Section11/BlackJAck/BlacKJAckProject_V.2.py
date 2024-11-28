import random
cards_player = ['A', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 10, 10, 10]
cards_dealer = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

logo = '''
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
                       _/ |                
                      |__/                 '''

def dealer():
    dealer = random.choice(cards_dealer)
    return dealer

def player():
    player = random.choice(cards_player)
    return player

def game(money):
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
We are giving out initials cards
Your first card is {player_initial_card}
Computer has got his initial card
Ypur starting money is {money}""")
    print("The initial bet is $25")
    bets_player = str(input("Would you like to 'Raise' the bet or 'Stay' the same?\n")).lower()
        
    if bets_player == "raise":
        player_money = int(input("Enter the amount you want to raise the bet for\n$"))
        while player_money > 25:
            player_money = int(input("Enter the amount you want to raise the bet for\n$"))
        money = money - player_money
        pot = player_money * 2
        print(f"Your current money is {money}, and the money on the pot is {pot}")
    elif bets_player == "stay":
        pot = 50
        print(f"No raises by player, actual money on the pot is {pot}")

    player_second_card = player()
    player_second_card = str(player_second_card)
    dealer_second_card = dealer()
    dealer_second_card = str(dealer_second_card)
    player_cards.append(player_second_card)
    dealer_cards.append(dealer_second_card)
    print(f"""
Your second card is {player_second_card}
Your total now is {", ".join(player_cards)}
Computer second card is {dealer_second_card}
Computer cards are __ and {dealer_second_card}""")
    
    second_pot = pot * 1.5
    print(f"Seconds bets are going out, the money in the pot is {pot}, the current bet is {second_pot}")
    bets_player = str(input("Would you like to 'Raise' the bet or 'Stay' the same?\n")).lower()
        
    if bets_player == "raise":
        player_money = int(input("Enter the amount you want to raise the bet for\n$"))
        while player_money > second_pot:
            player_money = int(input("Enter the amount you want to raise the bet for\n$"))
        money = money - player_money
        pot = player_money * 2
        print(f"Your current money is {money}, and the money on the pot is {pot}")
    elif bets_player == "stay":
        pot = second_pot
        print(f"No raises by player, actual money on the pot is {pot}")
    
    choice = str(input("Would you like to get another card?\n"))
    while choice in ["yes", "no"]:
        if choice == "yes":
            extra_card = player()
            extra_card = str(extra_card)
            dealer_extra_card = dealer()
            dealer_extra_card = str(dealer_extra_card)
            player_cards.append(extra_card)
            dealer_cards.append(dealer_extra_card)
            print(f"""
You decided to get another card that is {extra_card}, your cards are {', '.join(player_cards)}
and computer gets another card that is {dealer_extra_card}""")
            choice = str(input("Would you like to get another card?\n"))
        if choice == "no":
            print(f"""No more cards your total is ({', '.join(player_cards)}), computer total is ({','.join(dealer_cards)})""")
            break
        
    for i in range(len(player_cards)):
        if player_cards[i] in ['A']:
            new_card = str(input(f"You got a {player_cards[i]} in your cards, what value would you like to assign, it can be 11 or 1:\n"))
            player_cards[i] = new_card
            
    player_updated_list = [int(num) for num in player_cards]
    total_player = sum(player_updated_list)
    dealer_updated_list = [int(num) for num in dealer_cards]
    total_dealer = sum(dealer_updated_list)
    
    if total_dealer < 17:
        extra_card = dealer()
        total_dealer += extra_card
        print(f"The total value of the dealer is least than 17, dealer got another card that is {extra_card}, new total is {total_dealer}")
        
    if total_player == total_dealer:  
        print("Draw")
    elif total_player > 21:
        print("You overpassed 21 and lost the game")
        money = money - pot
    elif total_dealer > 21:
        print("computer over passed 21 and you Win")
        money = money + pot
    elif total_player > total_dealer:
        print(f"You win the game with {total_player}, the computer lost with {total_dealer}")
        money = money + pot
    elif total_player < total_dealer:
        print(f"You lose the game with {total_player}, the computer win with {total_dealer}")
        money = money - pot
    
        
    repeat_game = str(input("Would you like to play again?\n")).lower()
    while repeat_game in ["yes", "no"]:
        if repeat_game == "yes":
            return game(money)
        elif repeat_game == "no":
            return " "
            
game(1000)