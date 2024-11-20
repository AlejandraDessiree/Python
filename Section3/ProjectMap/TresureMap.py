print("Welcome to Treasure Island \nYour mission is to find the treasure. \nYou're at a cross road where do you want to go?")

choice = input("Type \"left\",\"Right\" or \"Straight\"\n")
if choice.lower() == "left":
    print("You start walking left and found a box do you want to open it?")
    choice_2 = input("Type \"Yes\" or \"No\"\n")
    if choice_2.lower() == "yes":
        print("You open the box and found a silver coin, knowing it does not worth money.")
    elif choice_2.lower() == "no":
        print("You decided to left the box behind and started walking home knowing there was something valuable there.")
    else:
        print("I do not recognized that action, try again!")
elif choice.lower() == "right":
    print("You started going right and found a little lake with something in the middle, what your move?")
    choice_3 = input("Type \"Wait\" or \"Swim\"\n")
    if choice_3.lower() == "wait":
        print("You decided to wait for a boat to appear. \n \n \nNothing happened then you decided to go home tired of waiting.")
    elif choice_3.lower() == "swim":
        print("You decided to swim, and visualized a little island, with something sparkling. \nIn your way you where eating by a shark!. \nGood Luck next time!")
    else:
        print("I do not recognized that action, try again!")
elif choice.lower() == "straight":
    print("You decided to go in the middle path, seeing a little fairy that want to show you something. \nWant to follow her?")
    choice_4 = input("Type \"Yes\" or \"No\"\n")
    if choice_4.lower() == "yes":
        print("You decided to follow the fairy and found something sarkling... \nIt can be a treasure, want to get it?")
        choice_5 = input("Type \"Yes\" or \"No\"\n")
        if choice_5.lower() == "yes":
            print("\"You have come a long way just to find this treasure, have it\" said the fairy")
            print('''
                  YOU HAVE GOTTEN THE TREASURE
                  ___________________________________________________________
                    /                                                          /|
                   /                                                          / |
                  /                                                          /  |
                 /                                                          /   |
                /__________________________________________________________/    |
               |                                                           |    |
               |                                                           |    |
               |                                                           |    |
               |                                                           |    |
               |              ____________________________               |    |
               |             |                            |              |    |
               |             |                            |              |    |
               |             |                            |              |    |
               |             |                            |              |    |
               |             |____________________________|              |    |
               |                                                           |    |
               |                                                           |    |
               |                                                           |    |
               |                                                           |    |
               |                                                           |    |
               |                                                           |    |
               |                                                           |    |
               |                                                           |    |
               |                                                           |    |
               |                                                           |    |
               |                                                           |    |
               |___________________________________________________________|    |
               |___________________________________________________________|    |
               /__________________________________________________________/    /
              /____________________________________________________________/   /
             (______________________________________________________________)  /
              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')
        elif choice_5.lower() == "no":
            print("\"You dont deserve to know our secrets, go home.\" said the fairy, you just left, feeling like you leave something.")
    elif choice_4.lower() == "no":
        print("You dont want to follow a fairy they dont exist, so you decided to go home.")
    else:
        print("I do not recognized that action, try again!")
else:
    print("I do not recognized that action, try again!")