string = input("Enter a string: ")
string2 = ('')
for i in string:
    string2 = i + string2
print("original string:", string)
print("Reversed string is:", string2)