from msilib import type_string
import string


print("Welcome to love cal!")
name1 = input("whats your name? \n")
name2 = input("whats there name? \n")


name1 = name1.lower()
name2 = name2.lower()

def go(x, i):
    love = 0
    tru = 0
    for y in x:
        
        love += y.count("l")
        love += y.count("o")
        love += y.count("v")
        love += y.count("e")
    for y in i:
        tru += y.count("t")
        tru += y.count("r")
        tru += y.count("u")
        tru += y.count("e")
    str(tru)
    str(love)
    
    
    num = f"{tru}{love}"
    int_num = int(num)

    if int_num <= 10 or int_num >=90:
        print(f"your number is {int_num}% you guys are toxic!")
    elif int_num >= 40 and int_num <= 50:
        print(f"your number is {int_num}% you guys are perfect!")
    else:
        print(f"Your number is {int_num}%!")

#    love += x.count("o")
#    love += x.count("v")
#    love += x.count("e")
    
go(name1, name2)