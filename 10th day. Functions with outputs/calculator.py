
#calculator

#Add
def add(n1, n2):
    return n1 + n2
#Multiply
def multiply(n1, n2):
    return n1 * n2
#Subtract
def subtract(n1, n2):
    return n1 - n2
#Devide
def devide(n1, n2):
    return n1 / n2
oporations = {
    "+": add,
    "*": multiply,
    "-": subtract,
    "/": devide
}

num1 = int(input("Enter your first number: "))
for symbol in oporations:
    print(symbol)
oporation_symbol = input("Pick a simbol from the list above: ")
num2 = int(input("Enter your second number: "))
calculation_function = oporations[oporation_symbol]
answer = calculation_function(num1, num2)
print(f"{num1} {oporation_symbol} {num2} = {answer}")
q = input("type yes to continue or no to stop: ")
while q != "no":
    for symbol in oporations:
        print(symbol)
    oporation_symbol = input("Pick a simbol from the list above: ")
    calculation_function = oporations[oporation_symbol]
    num3 = int(input("Enter your second number: "))
    answer2 = calculation_function(answer, num3)
    print(f"{answer} {oporation_symbol} {num3} = {answer2}")
    answer = answer2
    q = input("type yes to continue or no to stop: ")
