rows=int(input("Enter the number of rows: "))
print("diamond pattern")

if rows % 2 == 0:
 halfdiamond = rows // 2
else:
    halfdiamond = (rows // 2) + 1

for i in range(halfdiamond):
    for j in range(halfdiamond - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print()

for i in range(halfdiamond - 1):
    for j in range(i + 2):
        print(" ", end="")
    for j in range(2 * (halfdiamond - i - 1) - 1):
        print("*", end="")
    print() 