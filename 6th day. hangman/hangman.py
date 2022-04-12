import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)

#asq art
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
answer_list = []
for letter in chosen_word:
    answer_list.append("_")
game_counter = 6
game = False
while game_counter > 0 and game == False:

    guess = input("guess a letter: \n").lower()
    print(f"answer is {chosen_word}")

    #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    
    second = answer_list
    counts = 0
    for letter in chosen_word:
        if guess == letter:
            answer_list[counts] = guess
        counts += 1
    if second == answer_list:
        game_counter -= 1

    if not "_" in answer_list:
        game = True
    print(stages[game_counter])
    
            
            
    print(answer_list)
if game == True:
    print("you won!")
else:
    print(stages[0])
    print("you lost!")

