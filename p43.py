# Multilevel inheritance

class A:
	def m1(self):
		print("This is m1 function from class A ")

class B(A):
	def m2(self):
		print("This is m2 function from class B ")

class C(B):
	def m3(self):
		print("This is m3 function from class C ")

temp = C()

temp.m1()
temp.m2()
temp.m3()
