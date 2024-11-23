
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
direcction = input("Type 'encode' to encrypt, or 'decode' to decrypt:\n").lower()
text = input("Type your message:\n")
text = text.lower()
shift = input("Type the shift number:\n")
game_over = False

def encrypt(original_text, shift_amount):
    shifted_text = ""
    shift_amount = int(shift_amount)
    
    for letter in original_text:
        if letter == " ":
            shifted_text += " "
        else:
         shifted_position = alphabet.index(letter) + shift_amount
         shifted_position = shifted_position % len(alphabet)
         shifted_text += alphabet[shifted_position]
    
    print(f"This is your finished text: {shifted_text}")
    
def decypt(original_text, shift_amount):
    shifted_text = ""
    shift_amount = int(shift_amount)
    
    for letter in original_text:
        if letter == " ":
            shifted_text += " "
        else:
         shifted_position = alphabet.index(letter) - shift_amount
         shifted_position = shifted_position % len(alphabet)
         shifted_text += alphabet[shifted_position]
    
    print(f"This is your finished text: {shifted_text}")

def game():    
 if direcction == "encode":
    encrypt(original_text=text, shift_amount=shift)
 elif direcction == "decode":
    decypt(original_text=text, shift_amount=shift)
 else:
    print("no")
    
while not game_over:
    game()
    continu = input("Have another message?:\n").lower()
    
    if continu == "no":
        game_over = True
        break
    elif continu == "yes":
        print(logo)
        direcction = input("Type 'encode' to encrypt, or 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n")
        text = text.lower()
        shift = input("Type the shift number:\n")
        game()
    else:
        print("Invalid input. Please type 'yes' or 'no'.") 
