print("enter marks of student ")
marks1 = int(input("enter marks of subject 1:"))
marks2 = int(input("enter marks of subject 2:"))
marks3 = int(input("enter marks of subject 3:"))
marks4 = int(input("enter marks of subject 4:"))
marks5 = int(input("enter marks of subject 5:"))

total_marks = marks1 + marks2 + marks3 + marks4 + marks5
average_marks = total_marks / 5

if average_marks >= 90:
    print("Grade: A")
elif average_marks >= 80:
    print("Grade: B")
elif average_marks >= 70:
    print("Grade: C")
elif average_marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")