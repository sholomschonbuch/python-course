import random as random

#def function
def hit(cards):
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

while hits:
    player_count = 0
    dealer_count = 0
    print(f"dealers cards{dealers_cards}")
    print(f"your cards {player_cards}")
    stay = input("H for hit, S for stay ").lower()
    while stay != "s":

        hit(player_cards)
        for card in player_cards:
            player_count += card
        if player_count > 21:
            print(f"dealers cards{dealers_cards}")
            print(f"your cards {player_cards}")
            
                   
        print(f"dealers cards{dealers_cards}")
        print(f"your cards {player_cards}")
        
        
        stay = input("H for hit, S for stay ").lower()
        
    # if stay == "s":
    #     hits = False
    #     dealer_hits = True
    # elif stay == "h":
    #     hit(player_cards)
    #Add up players cards
    for card in player_cards:
        player_count += card

    
    if player_count > 21:
        print(f"{player_count} You went bust")
        hits = False
    
    #dealer gets dealt
    while dealer_hits:
        for card in dealers_cards:
            dealer_count += card
        if dealer_count <= player_count and dealer_count <= 21:
            hit(dealers_cards)
        elif dealer_count == player_count:
            print(f"Your cards {player_cards} \nDealers cards{dealers_cards}\nDraw!")
            dealer_hits = False
        elif dealer_count > 21:
            print(f"Dealers bust {dealers_cards}")
            dealer_hits = False


    