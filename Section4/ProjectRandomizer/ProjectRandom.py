from ProjectModule import player_2


img_rock = ('''
    _______
  /       
 /         
|   ROCK   |
 \         /
  \_______/''')

img_paper = ('''   
    _______
  /       
 /         
|   PAPER  |
 \         /
  \_______/''')

img_siccors = ('''   
    _______
  /       
 /         
| SCISSORS |
 \         /
  \_______/''')

print("Lets play Rock, Paper and Siccors")
global player_1


player_1 = input("Rock is \"1\", Paper is \"2\" and Siccors is \"3\"\n")

while player_1 not in ["1", "2", "3"]:
    print("Please use \"1\" for Rock, \"2\" for Paper and \"3\" for Siccors")
    player_1 = input("Rock is \"1\", Paper is \"2\" and Siccors is \"3\"\n")
    
player_1 = int(player_1)
player_2 = player_2()

def game():
 if player_1 == 1:
    print(img_rock)
    if player_2 == 1:
        print(img_rock) 
        print("Tie")
    elif player_2 == 2:
        print(img_paper)
        print("Computer Wins")
    elif player_2 == 3:
        print(img_siccors)
        print("Player 1 Wins")
 elif player_1 == 2:
    print(img_paper)
    if player_2 == 1:
        print(img_rock)
        print("Player 1 Wins")
    elif player_2 == 2:
        print(img_paper)
        print("Tie")
    elif player_2 == 3:
        print(img_siccors)
        print("Computers Wins")
 elif player_1 == 3:
    print(img_siccors)
    if player_2 == 1:
        print(img_rock)
        print("Computers Wins")
    elif player_2 == 2:
        print(img_paper)
        print("Player 1 Wins")
    elif player_2 == 3:
        print(img_siccors)
        print("Tie")

PlayAgain = "yes" 

while PlayAgain == "yes":
  game()
  PlayAgain = input("Play Again? Yes or No?\n")