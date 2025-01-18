#Section 12
import random
computer_number = random.randint(1,101)
print("Guees a number between 0 to 100")
choice= input("Choose your dificulty:'easy' or 'hard': ").lower()

def game(chances):
    print (f"You have {chances} attemps remaining")
    while chances >= 1:
        guess = int(input("Guess: "))
        chances -= 1
        
        if guess <= 0:
            print("Number Between 0 to 100")
        elif guess >= 101:
            print("Number Between 0 to 100")
        else:
            pass
        
        if guess > computer_number:
            print("lower")
            print(f"You have {chances} attemps remaining")
        elif guess < computer_number:
            print("Higher")
            print(f"You have {chances} attemps remaining")
        
        if guess == computer_number:
            chances = 0
            print("Won")
            
        

while choice not in ["easy", "hard"]:
    choice= input("'easy' or 'hard'").lower()

if choice == "easy":
    game(10)
elif choice == "hard":
    game(5)
