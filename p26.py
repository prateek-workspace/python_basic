# WAP to create a blank list then insert elements in it using append() also print the list.

mylist = []

print("Enter ten numbers to the list : ")

for i in range (0,10):
	m = int(input())
	mylist.append(m)
print(mylist)
print("Maxiumum number = ", max(mylist))
print("Minimum number = ", min(mylist))
