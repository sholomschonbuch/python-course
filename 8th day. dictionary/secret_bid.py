import os
from art1 import logo
clear = lambda: os.system('cls')

#variables
contin = False

#dictionary of all bidders
biders = {}

#functions
def find_highest_bidder(**dictionary1):
    highest_bid = 0
    for k,bid in dictionary1.items():
        if bid > highest_bid:
            highest_bid = bid
            top = f"{k} at {bid}"
    print(logo)
    print(f"The highest bid was {top}")


#While loop that will run the program
while contin == False:
        
    name = input("What's your name? ")
    bid = int(input("What's your bid? $"))
    biders[name] = bid
    quest = input("Are there more bidders? type yes or no. ")
    if quest == "no":
        contin = True
    clear()

#Result
find_highest_bidder(**biders)