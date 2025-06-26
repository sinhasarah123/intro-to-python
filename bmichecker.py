height=float(input("Enter your height in cm: "))
weight=float(input("Enter your weight in kg: "))
bmi = weight / ((height / 100) ** 2)
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 24.9:
    print("Normal weight")
elif 25 <= bmi < 29.9:
    print("Overweight")
elif bmi >= 30:
    print("Obesity")
else:
    print("Invalid input")
print("Your BMI is:", bmi)