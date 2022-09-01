import random as random

#draw function
def hit(cards):
    """Deals a random number to passed list"""
    #card deck
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    cards.append(random.choice(deck))

#begin game
dealers_cards = []
player_cards = []
hit(dealers_cards)
hit(player_cards)
hit(player_cards)


#hit or stay?
hits = True

#Print the game
player_count = 0
dealer_count = 0
print(f"dealers cards{dealers_cards}")
print(f"your cards {player_cards}")

#Ask and deal card to player
stay = input("H for hit, S for stay ").lower()
if stay == "h":
    deal_player = True
else:
    deal_player = False

while deal_player:
    hit(player_cards)
    #Counts the cards
    for card in player_cards:
        player_count += card
    if player_count > 21:
        #End game
        print(f"Dealers cards {dealers_cards}")
        print(f"You busted {player_cards}")
        hits = False
        deal_player = False
    else:
        #Ask if he wants another card         
        print(f"Dealers cards {dealers_cards}")
        print(f"Your cards {player_cards}")
        stay = input("H for hit, S for stay ").lower()
        if stay == "s":
            deal_player = False

#Dealer gets dealt
if hits:
    hit(dealers_cards)
    dealer_hits = True
    while dealer_hits:
        player_count = 0
        dealer_count = 0
        for card in player_cards:
            player_count += card
        for card in dealers_cards:
            dealer_count += card
        if dealer_count < player_count and dealer_count < 21:
            hit(dealers_cards)
        elif dealer_count == player_count:
            print(f"Your cards {player_cards} \nDealers cards{dealers_cards}\nDraw!")
            dealer_hits = False
        elif dealer_count > 21:
            print(f"Dealers bust {dealers_cards}")
            dealer_hits = False
        else:
            print(f"Dealer wins {dealers_cards}\nYour cards{player_cards}")
            dealer_hits = False


    