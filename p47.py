# WAP for exception handling.


try:
	a = int(input("Enter first number : "))
	b = int(input("Enter second number : "))

	c = a + b

	print("Sum is : ",c)

except ValueError:
	print("Pagal ho kya...integer kahe nhi input kar rhe ho...")