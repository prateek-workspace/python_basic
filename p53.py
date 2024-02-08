name = input("Enter name : ")
sname = name.split(" ")

#print(sname)

print("Short name is : ",end = "")

for n in range (len(sname) - 1):
	print(sname[n][0] + ".", end = "")

print(sname[len(sname) - 1])