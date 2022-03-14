import random

name_string = input("put in everyones name with ',' seperateting them\n")
name = name_string.split(",")

number = random.randint(0, len(name) - 1)
print(f"name[number], is paying for tonight!")
