#WAP to check if number is a Palindrome Number or Not.(Without Loop upto 4 digits)

n = eval(input("Enter Number :  "))

number = n

a = n % 10
n = n // 10

b = n % 10
n = n // 10

c = n % 10
n = n // 10

d = n % 10
n = n // 10

num = a * 1000 + b * 100 + c * 10 + d * 1
#Palindrome means if number and its reverse or equal'

if number == num :
    print("Number is a Palindrome Number")
else : 
    print("Number is not a Palindrome Number")
    