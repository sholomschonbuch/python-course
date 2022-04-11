student_height = input("Input a list of student heights ").split()
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
print(student_height)
total= 0
amount_students = 0
for height in student_height:
    amount_students += 1
    total += height
    print(height)

print(total // amount_students)