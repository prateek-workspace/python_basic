try:
	a = int(input("Enter first number : "))
	b = int(input("Enter second number : "))

	c = a / b

	print("Divide is : ",c)

except ValueError:
    print("Invalid input. Please enter valid numbers.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally:
    print("Finally block: This will always be executed.")