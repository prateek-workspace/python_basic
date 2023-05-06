#WAP to find average of 5 subjects and their sum.

sci = eval(input("Enter marks obtained in science : "))
sst = eval(input("Enter marks obtained in sst : "))
hin = eval(input("Enter marks obtained in hindi : "))
eng = eval(input("Enter marks obtained in english : "))
maths = eval(input("Enter marks obtained in maths : "))


total = sci + sst + hin + eng + maths

average = total / 5


print("Total of 5 fubjects is : " ,total)

print("Average of 5 subjects is : " ,average)
