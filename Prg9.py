#WAP to take input from user max 4 digits and calculate the sum of each individual digits.

num = eval(input("Enter Number :  "))

a = num % 10
num = num // 10

b = num % 10
num = num // 10

c = num % 10
num = num // 10

d = num % 10
num = num // 10

sum = a + b + c + d

print("sum of digits is :  " ,sum) 

