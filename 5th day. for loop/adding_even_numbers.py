

from tkinter import N


total = 0
for number in range(1, 101):
    n = number % 2
    if n == 0:
        total += number
print(total)


