# WAP for  printing numbers from 1 to 100 using recursion.

import time

def num(n):
    if(n >= 100):
        return
    print(n, end = " ")
    time.sleep(1)
    num(n+1)

a = int(input("Enter number : "))
num(a)