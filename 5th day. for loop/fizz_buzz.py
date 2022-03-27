

for number in range(1, 101):
    num = 3 / number
    if number % 3 == 0 and number % 5 == 0:
        number = "fizzbuzz"
    elif number % 3 == 0:
        number = "fizz"
    elif number % 5 == 0:
        number = "buzz"
    print(number)