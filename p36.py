def add(a,b):
    c = a + b 
    print("Sum : ",c)

def sub(a,b):
    c = a - b 
    print("Substraction : ",c)
    
def div(a,b):
    c = a / b 
    print("Division : ",c)
    
def multi(a,b):
    c = a * b 
    print("Multiplication : ",c)

def clrscr():
    print("\n" * 50)  # Print 100 empty lines


print("--------------------------------------")
    
x = eval(input("Enter first number : "))
y = eval(input("Enter second number : "))

print("Enter 1 for Addition :---")
print("Enter 2 for Substraction :---")
print("Enter 3 for Division :---")
print("Enter 4 for Multiplication :---")

n = int(input())

clrscr()

if n == 1:
    clrscr()
    add(x,y)


elif n == 2:
    clrscr()
    sub(x,y)

elif n == 3:
    clrscr()
    div(x,y)

elif n == 4:
    clrscr()
    multi(x,y)

else:
    print("Enter a valid choice !!")