age=int(input("Enter your age: "))

if age < 10:
    print("you are too young for class")
elif age >= 10 and age <= 20:
    print("you are allowed in class")
elif age > 20:
    print("you are not allowed in class")
else:
    print("you are too young for class")