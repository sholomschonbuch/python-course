
#calculator functions

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
#calculator
def calcultor(): 
    num1 = int(input("Enter your first number: "))
    for symbol in oporations:
        print(symbol)
    continues = True
    
    while continues:
        oporation_symbol = input("Pick a oporation: ")
        calculation_function = oporations[oporation_symbol]
        num2 = int(input("Enter your next number: "))
        answer = calculation_function(num1, num2)
        print(f"{num1} {oporation_symbol} {num2} = {answer}")
        num1 = answer
        q = input("type yes to continue or no to stop: ")
        if q == "no":
            continues = False
        elif q == "clear":
            calcultor()
calcultor()