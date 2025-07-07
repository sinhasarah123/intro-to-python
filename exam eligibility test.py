medical_cause = input("do you have a medicalcause yes/no:")
attendence = input("enter your attendence")
if medical_cause=="yes":
    print("you are eligible for the exam")
else: 
    if attendence >= "75":
        print("you are eligible for the exam")
    else:
        print("you are not eligible for the exam")