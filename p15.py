# WAP to find greatest among 3 numbers using and keyword.

print("----------------------------------------")

a = eval(input("Enter first no : "))

b = eval(input("Enter second no : "))

c = eval(input("Enter third no : "))

print()

if (a > b and a > c):
	print("Greater number is : ", a)

elif (b > a and b > c):

	print("Greater number is : ", b)

else:
	print("Greater number is : ", c)


print("----------------------------------------")

