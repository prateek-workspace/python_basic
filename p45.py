# WAP for polymorphism

class parent:
    def myMethod(self):
            print("calling paarent class")

class child:
    def myMethod(self):
            print("calling child class")
  
c = child()
c.myMethod()

p = parent()
p.myMethod()