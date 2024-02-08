# WAP to find area and perimeter of rectangle using class and constructor.

class rect:
	def __init__(self,l,b):
		self.l = l
		self.b = b

	def area(self):
		return self.l*self.b

	def peri(self):
		return 2*(self.l + self.b)

x = eval(input("Enter length : "))
y = eval(input("Enter breadth : "))

r = rect(x,y)

print("Area is : ", r.area())
print("Perimeter is : ", r.peri())