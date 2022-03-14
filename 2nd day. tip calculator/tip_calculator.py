print("Welcome to tip calculator!")
totalBill = int(input("What is your total bill? $"))
amountPpl = int(input("How many people are splitting the bill? :"))
percentTip = int(input("What percent would you like to give? 10, 20, or 15? %"))
tipAmount = (totalBill / 100) * percentTip
#tipAmount = (percentTip / totalBill) * 100
print(tipAmount)

totalBill = totalBill + tipAmount
total = totalBill / amountPpl
print(total)
