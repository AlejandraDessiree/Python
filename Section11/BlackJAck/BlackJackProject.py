# Dealer takes an extra card if value under 17
import random
cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
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
    dealer = random.choice(cards)
    cards_dealer = dealer
    return cards_dealer

def player():
    player = random.choice(cards)
    player_cards = player
    return player_cards

def game():
    card_not_shown = dealer()
    print(card_not_shown)
    initial_card = player()
    print(logo)
    print(f"""
        Welcome to Black Jack
        We are giving out initials cards
        Your initial card is {initial_card}
        Computer has got his initial card
        Initial bet of $5""")
    bet = str(input("Do you want to raise your bet?\n"))
    
    if bet == "yes":
        while bet == "yes":
            money = int(input("How much money you want in your bet?\n$"))
            if money <= 5:
                print("Bet have to be over $5")
            elif money >= 6:
                print(f"Bet have been raised to ${money} by you")
                break
    elif bet == "no":
        money = 5
    
    computer_bet = ["yes", "no"]
    computer_money = ["raise", "not raise"]
    computer_choice = random.choice(computer_bet)
    total_bet = money * 2
    
    if computer_choice == "yes":
        computer_choice = random.choice(computer_money)
        if computer_choice == "raise":
            computer_raise = money * 3
            player_money = computer_raise - money
            total_bet = computer_raise * 2
            print(f"""
        Computer decided to raise the bet.
        The money computer raised to is ${computer_raise}
        You need to pay an extra of ${player_money}
        After pay, The money in the pot is ${total_bet}""")
        elif computer_choice == "not raise":
            total_bet = money * 2
            print(f"""
        Computer decided to not raise the bet.
        The money in the pot is now ${total_bet}""")
    elif computer_choice == "no":
        print(f"""
        Computer decided to not raise the bet.
        The money in the pot is now ${total_bet}""")
    
    extra_dealer_card = dealer()
    player_card = player()
    print(f"""
        We are giving out the second card
        Your second card is {player_card}
        Computer has got his second card
        his card is {extra_dealer_card}""")
    
    sum_dealer_cards = card_not_shown + extra_dealer_card
    sum_player_cards = initial_card + player_card
  
    if sum_dealer_cards < 17:
        extra_dealer_card = dealer()
        sum_dealer_cards = sum_dealer_cards + extra_dealer_card

    choice = str(input("Do you want to get another card?\n")).lower
    
    if choice() == "yes":
        third_card = player()
        print(f"""
        You choose to get another card,
        your new card is {third_card}""")
        sum_player_cards = sum_player_cards + third_card
        if sum_player_cards > 21:
            print("You lose, computer wins")
        elif sum_dealer_cards > 21:
            print("Computer Lose, you Win")
        elif sum_dealer_cards > sum_dealer_cards:
            print(f"You wim")
        elif sum_dealer_cards > sum_player_cards:
            print(f"You lose")
        elif sum_player_cards == sum_dealer_cards:
            print("Draw")
            
    if choice() == "no":
        if sum_player_cards > 21:
            print(f"You lose with {sum_player_cards}, computer wins with {sum_dealer_cards}")
        elif sum_dealer_cards > 21:
            print(f"Computer Lose with {sum_dealer_cards}, you Win with {sum_player_cards}")
        elif sum_dealer_cards > sum_dealer_cards:
            print(f"You wim with {sum_player_cards}")
        elif sum_dealer_cards > sum_player_cards:
            print(f"You lose with {sum_player_cards}")
        elif sum_player_cards == sum_dealer_cards:
            print(f"Draw")
            
    game_over = str(input("Want to play again?\n"))
    while game_over in ["yes", "no"]:
        if game_over == "yes":
            return game()
        elif game_over == "no":
            return "Thanks for playing"
    
game()

# if player() > 21:
#     print("Over 21 player")
# elif dealer() > 21:
#     print("Over 21 dealer")
    
# if player() > dealer():
#     print("Win")
# elif player() < dealer():
#     print("Lose")
# elif player() == dealer():
#     print("Draw")