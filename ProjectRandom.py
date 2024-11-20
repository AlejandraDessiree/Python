from ProjectModule import player_2

print("Lets play Rock, Paper and Siccors")
player_1 = input("Rock is \"1\", Paper is \"2\" and Siccors is \"3\"")

while player_1 not in ["1", "2", "3"]:
    print("Please use \"1\" for Rock, \"2\" for Paper and \"3\" for Siccors")
    player_1 = input("Rock is \"1\", Paper is \"2\" and Siccors is \"3\"")
    
player_1 = int(player_1)
player_2 = player_2()

if player_1 == 1:
    print('''  1
    _______
  /       
 /         
|   ROCK   |
 \         /
  \_______/''')
    if player_2 == 1:
        print('''   
    _______
  /       
 /         
|   ROCK   |
 \         /
  \_______/''') 
        print("Tie")
    elif player_2 == 2:
        print('''   
    _______
  /       
 /         
|   PAPER  |
 \         /
  \_______/''')
        print("Computer Wins")
    elif player_2 == 3:
        print('''   
    _______
  /       
 /         
| SCISSORS |
 \         /
  \_______/''')
        print("Player 1 Wins")
elif player_1 == 2:
    print('''   
    _______
  /       
 /         
|   PAPER  |
 \         /
  \_______/''')
    if player_2 == 1:
        print('''   
    _______
  /       
 /         
|   ROCK   |
 \         /
  \_______/''')
        print("Player 1 Wins")
    elif player_2 == 2:
        print('''   
    _______
  /       
 /         
|   PAPER  |
 \         /
  \_______/''')
        print("Tie")
    elif player_2 == 3:
        print('''   
    _______
  /       
 /         
| SCISSORS |
 \         /
  \_______/''')
        print("Computers Wins")
elif player_1 == 3:
    print('''   
    _______
  /       
 /         
| SCISSORS |
 \         /
  \_______/''')
    if player_2 == 1:
        print('''   
    _______
  /       
 /         
|   ROCK   |
 \         /
  \_______/''')
        print("Computers Wins")
    elif player_2 == 2:
        print('''   
    _______
  /       
 /         
|   PAPER  |
 \         /
  \_______/''')
        print("Player 1 Wins")
    elif player_2 == 3:
        print('''   
    _______
  /       
 /         
| SCISSORS |
 \         /
  \_______/''')
        print("TIe")