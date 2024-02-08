# WAP for string palindrome.

str = input("Enter string : ")
rstr = "".join(reversed(str))

print(rstr)

if ( str == rstr ):
	print("Palindrome")
else:
	print("Not a Palindrome")