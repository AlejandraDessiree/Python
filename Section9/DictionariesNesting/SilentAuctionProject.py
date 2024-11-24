import os
auction_list = {}
question = "yes"
max_value = 0
max_item = ""

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                         `'-------'`
                       .-------------.
                      /_______________\\
                       
                       '''

while question == "yes":
    print(logo)
    names = input("Whats Your name?\n")
    bids = int(input("What's your bid?\n$"))
    auction_list[names] = bids
    question = input("continue? (yes/no): ").lower()
    os.system("cls")
    
    if question == "no":
        break
    
for key in auction_list:
    if auction_list[key] > max_value:
        max_value = auction_list[key]
        max_item = key
    
print(logo)
print(f"{max_item} won the auction with ${auction_list[max_item]}")
