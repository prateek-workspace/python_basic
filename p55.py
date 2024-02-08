n = int(input("Enter Number : "))

hexa = hex(n).replace("0x","")

print("Binary is : ",bin(n).replace("0b",""))
print("Octal is : ",oct(n).replace("0o",""))
print("Hexadecimal is : ",hexa.upper())