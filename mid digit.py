# Find the middle digit of a number
num = int(input("Enter a number: "))
str_num = str(num)
if len(str_num) % 2 == 1:
    mid_index = len(str_num) // 2
    print("The middle digit is:", str_num[mid_index])
else:
    print("There is no middle digit.")
