# WAP for inheritance

class bulldog:
	def grawl(self):
		print("Brutus")
		print("Grawls...")

class rundog(bulldog):
	def bark(self):
		print("Moti")
		print("Barks...")

dog = rundog()

dog.bark()
dog.grawl()