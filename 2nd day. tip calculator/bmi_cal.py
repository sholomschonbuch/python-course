height = float(input("Please enter your height: "))
weight = float(input("please enter your weight: "))


bmi = weight / (height ** 2) * 703

if bmi <= 18.5:
        print(f"your bmi is {bmi}, you are underweight")
elif bmi < 25:
        print(f"your bmi is {bmi}, you are normal weight")
elif bmi < 30:
        print(f"your bmi is {bmi}, you are overweight")
elif bmi < 35:
        print(f"your bmi is {bmi}, you are obese")
#elif bmi > 35:
else:
    print(f"your bmi is {bmi}, you are clinically obese")

