# Class

class demo():
    def temp(self):
        print("Hello World !!")

    def add(self,a,b):
        return a+b

d = demo()
d.temp()
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print(d.add(x,y))
