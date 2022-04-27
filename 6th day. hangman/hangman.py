import random
from word_list import word_list
from hangman_art import stages, logo
import os
clear = lambda: os.system('cls')

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
all_answers = []

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
answer_list = []
for letter in chosen_word:
    answer_list.append("_")
lives = 6
game = False
while lives > 0 and game == False:

    guess = input("guess a letter: \n").lower()
    print(f"answer is {chosen_word}")
    clear()

    #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    if guess in answer_list:
        print("You already guessed it")
    correct = False
    for letter in enumerate(chosen_word):
        if guess == letter[1]:
            answer_list[letter[0]] = guess
            correct = True

    if correct == False:
        lives -= 1
        all_answers.append(guess)
    print(f"History: {all_answers}")
    print(stages[lives])
    print(f"you guessed {guess}")
    print(answer_list)
    if not "_" in answer_list:
        print("congrats you won!")
        game = True
    
    if lives == 0:
        print(stages[0])
        print("you lost!")
        print(chosen_word)
                
print(logo)            




