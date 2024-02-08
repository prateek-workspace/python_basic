# WAP to find sum of even numbeers in a given range.

sum = 0
i = 0

n = int(input("Enter number upto which you want sum of : "))

while(i <= n):
    even = n % 2
    if (even == 0):
        sum = sum + even
    else:
        pass
        i = i + 1

print(sum)