print("welcome to the ride!")
height = int(input("How tall are you? "))

if height >= 20:
    print("enjoy! ")
    age = int(input("what is your age? "))
    price = 0
    if age >= 18:
        price = 20
        print(f"ticket will be {price}$ ")
    elif age >= 12:
        price = 15
        print(f"ticket will be {price}$ ")
    else:
        print("go for free! ")
    
    wants_photo = input("Do you want a photo? Y or N: ")
    if wants_photo == "Y":
        print(f"Your price is {price + 2}$")
    else:
        print(f"Total is {price}$ ")
            

else: 
    print("cant ride! ")