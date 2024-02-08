# Multiple Inheritance.

class A:
	def m1(self):
		print("This is m1 from class A")

class B:
	def m2(self):
		print("This is m2 from class B")

class C(A,B):
	def m3(self):
		print("This is m3 from class C")

temp = C()

temp.m1()
temp.m2()
temp.m3()