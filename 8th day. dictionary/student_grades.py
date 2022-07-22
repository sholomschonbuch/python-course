student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
print(student_scores.keys())

for k in student_scores:
    if student_scores[k] > 90:
        score = "outstanding"
    elif student_scores[k] > 80:
        score = "exceeds expectations"
    elif student_scores[k] > 70:
        score = "Acceptable"
    else:
        score = "Fail"
    student_grades[k] = score

# 🚨 Don't change the code below 👇
print(student_grades)
