class parent(object):
	def altered(self):
		print("Parent Altered")
class child(parent):
	def altered(self):
		print("Child before parent altered")
		super(child,self).altered()
		print("child after parent altered")


dad = parent()		
dad.altered()

son = child()
son.altered()