string = input("please enter a string: ")
char= input("please enter a character: ")
i= 0
count = 0
while i < len(string):
    if string[i] == char:
        count += 1
    i += 1
print("The character", char, "occurs", count, "times in the string.")