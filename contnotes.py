amount = int(input("Enter the amount: "))
note1 = amount //100
note2 = (amount%100)//50
note3 = (amount%100%50)//10
print("the amount of 100 rs notes is:", note1)
print("the amount of 50 rs notes is:", note2)
print("the amount of 10 rs notes i230s:", note3)