from re import S


print("Pizza order! ")
size = input("what size pizza do you want? S, M or L? ")
add_cheese = input("Do you want more cheese? Y or N? ")
olives = input("Do yu want olives? Y or N? Y or N? ")
price = 0
if size == "S":
    price = 10
    print(f"Pizza is {price}$ ")
elif size == "M":
    price = 15
    print(f"Pizza is {price}$ ")
else:
    price = 20
    print(f"Pizza is {price}$ ")

if add_cheese == "Y":
    if size == "S":
        price += 3
    else:
        price += 6
if olives == "Y":
    if size == "S":
        price += 3
    else:
        price += 6
print(f"Your total is {price}$ ")
