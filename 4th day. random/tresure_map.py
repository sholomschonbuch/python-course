#from function__0.append_list_in_a_list import list_in_list
row1 = ["1", "2", "3"]
row2 = ["6", "5", "4"]
row3 = ["7", "8", "0"]
rows = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
treasure = input("Where do you want your treasure to be? \n")

hori = int(treasure[0])
verti = int(treasure[1])

selected_row = rows[verti - 1]
selected_row[hori - 1] = "X"

print()
#list_in_list(a, b, rows)

print(f"{row1}\n{row2}\n{row3}")
