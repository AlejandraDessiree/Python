import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to My Password Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers you want in your password?\n"))
nr_symbols = int(input(f"How manu symbols you want in your password?\n"))

password = []

for char in range(1, nr_letters + 1):
    random_character = random.choice(letters)
    password += random_character
    
for num in range(1, nr_numbers + 1):
    random_number = random.choice(numbers)
    password += random_number
     
for sym in range(1, nr_symbols + 1):
    random_symbol = random.choice(symbols)
    password +=  random_symbol
    
random.shuffle(password)
print("".join(password))


print('Te amo mucho alejandra dessire arauz fonsecaaaaa')
