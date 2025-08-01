def decimal_to_binary(decimal_number):
    return bin(decimal_number).replace("0b", "")
decimal_number = int(input("Enter a decimal number: "))
binary_number = decimal_to_binary(decimal_number)
print("Binary representation:", binary_number)