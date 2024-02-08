#  WAP to convert celcius to fahrenheit.

print("Enter 1 for celcius to fahrenheit : ")
print("Enter 2 for fahrenheit to celcius : ")

a = int(input())

if a == 1:
	c = float(input("Enter temperature in celcius : "))
	f = (9*c)/5 + 32
	print("Temperature in fahrenheit is : ",f)
elif a == 2:
	f = float(input("Enter temperature in celcius : "))
	c = (f-32)*5/9
	print("Temperature in celcius is : ",c)
else:
	print("Please select a valid choice !! ")
