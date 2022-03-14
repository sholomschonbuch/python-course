import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game = [rock, paper, scissors]

player = input("1 for rock, 2 for paper, 3 scissors\n")
player = int(player) - 1
player = game[player]
print(player)
computer = random.choice(game)
print(computer)
#print(game[computer])


#if player == 0 and computer == 3:
#    print("yeah you win!!")
#if player == 0 and computer == 3:
#if player == 0 and computer == 3:

