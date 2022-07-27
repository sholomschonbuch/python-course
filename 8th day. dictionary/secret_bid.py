import os
clear = lambda: os.system('cls')

contin = "yes"
biders = {}
highest_bid = 0
while contin == "yes":
        
    name = input("What's your name? ")
    bid = int(input("What's your bid? $"))
    biders[name] = bid
    contin = input("Are there more bidders? type yes or no")
    clear()

for bid in biders:
    if biders[bid] > highest_bid:
        highest_bid = biders[bid]
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
                       .-------------.
                      /_______________\\
'''

print(f"The highest bid was {highest_bid.keys()}")

