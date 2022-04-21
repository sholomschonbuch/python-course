from itertools import count


def prime_check(number):
    for n in range(number, 0):
        number = number % n
        if (number - int(number) == 0):
            print("Not prime")
        else:
            print("Prime")







n = int(input("Check this number: "))
prime_check(number=n)