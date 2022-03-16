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
while player != "e":

    player = int(player) - 1

    print(game[player])
    computer = random.randint(0, len(game) - 1)
    computer_choice = game[computer]
    print(computer_choice)

    if player == computer:
        print("Tie game!")
    elif player == 0 and computer == 2:
        print("You win!!")
    elif player == 1 and computer == 0:
        print("You win!")
    elif player == 2 and computer == 1:
        print("You win!!!")
    else:
        print("You lose!")
    player = input("1 for rock, 2 for paper, 3 scissors. enter e to exit!\n")

