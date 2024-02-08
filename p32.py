# WAP to find greatest number among 2.

def great(a,b):
	if(a>b):
		return(a)
	else:
		return(b)

x = int(input())
y = int(input())
print("Greater number is : ", end = " ")
print(great(x,y))
