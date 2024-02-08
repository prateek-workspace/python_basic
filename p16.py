# WAP to calculate electricity bill.

print("----------------------------------------")
n = eval(input("Enter Number of units consumed : "))

print()

if (n > 0 and n <=150):
	bill = n * 2.40
elif (n >= 151 and n <= 300):
	bill = (150*2.40) + (n - 150)*3.00
else:
	bill = (150*2.40) + 150*3.00 + (n - 300)*3.20

print("Total Billed Amount is : ", bill)

print("----------------------------------------")

