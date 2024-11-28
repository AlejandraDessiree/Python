from ProjectModule import player_2


global img_rock 
img_rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

global img_paper 
img_paper= ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

global img_siccors 
img_siccors= ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

title = """
██████╗  ██████╗  ██████╗██╗  ██╗    ██████╗  █████╗ ██████╗ ███████╗██████╗     ███████╗ ██████╗██╗███████╗███████╗ ██████╗ ██████╗ ███████╗
██╔══██╗██╔═══██╗██╔════╝██║ ██╔╝    ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗    ██╔════╝██╔════╝██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝
██████╔╝██║   ██║██║     █████╔╝     ██████╔╝███████║██████╔╝█████╗  ██████╔╝    ███████╗██║     ██║███████╗███████╗██║   ██║██████╔╝███████╗
██╔══██╗██║   ██║██║     ██╔═██╗     ██╔═══╝ ██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗    ╚════██║██║     ██║╚════██║╚════██║██║   ██║██╔══██╗╚════██║
██║  ██║╚██████╔╝╚██████╗██║  ██╗    ██║     ██║  ██║██║     ███████╗██║  ██║    ███████║╚██████╗██║███████║███████║╚██████╔╝██║  ██║███████║
╚═╝  ╚═╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝    ╚═╝     ╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝╚═╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝
 """              

global player_1

def game():
  print(title)
  print("Lets play Rock, Paper and Siccors")
  player_1 = input("Rock is \"1\", Paper is \"2\" and Siccors is \"3\"\n")

  while player_1 not in ["1", "2", "3"]:
    print("Please use \"1\" for Rock, \"2\" for Paper and \"3\" for Siccors")
    player_1 = input("Rock is \"1\", Paper is \"2\" and Siccors is \"3\"\n")
    
  player_1 = int(player_1)
  player2 = player_2()
 
  if player_1 == 1:
    print(img_rock)
    if player2 == 1:
        print(img_rock) 
        print("Tie")
    elif player2 == 2:
        print(img_paper)
        print("Computer Wins")
    elif player2 == 3:
        print(img_siccors)
        print("Player 1 Wins")
  elif player_1 == 2:
    print(img_paper)
    if player2 == 1:
        print(img_rock)
        print("Player 1 Wins")
    elif player2 == 2:
        print(img_paper)
        print("Tie")
    elif player2 == 3:
        print(img_siccors)
        print("Computers Wins")
  elif player_1 == 3:
    print(img_siccors)
    if player2 == 1:
        print(img_rock)
        print("Computers Wins")
    elif player2 == 2:
        print(img_paper)
        print("Player 1 Wins")
    elif player2 == 3:
        print(img_siccors)
        print("Tie")
  PlayAgain = input("Play Again? Yes or No?\n")
  
  if PlayAgain == "yes":
    game()
  else:
      print("Game Ended")

game()
