def div(x,y):
	try:
		result = x / y
	except ValueError:  
		print("Pagal ho kya...")
	except ZeroDivisionError:
		print("Infinite value can not be fetched")
	finally:
		print("This is finally block")

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
div(a,b)