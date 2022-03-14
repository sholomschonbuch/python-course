from dis import code_info
import random
game = ["heads", "tails"]
coin = random.randint(0, 1)
user = int(input("Pick 1 for heads, 2 for tails\n")) - 1
comp = game[coin]
if user == coin:
    print(f"{comp}, you win!")
else:
    print(f"{comp}, you lose!")

