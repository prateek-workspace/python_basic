#WAP to Calculate an employees gross salary.

basic = eval(input("Enter basic salary :  "))

print("Basic Salary is :  " ,basic)

ta = basic * 0.1

da = basic * 0.3

hra = basic * 0.2

gross = basic + ta + da + hra

print("Gross Salary is :  " ,gross)