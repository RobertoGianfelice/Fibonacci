from math import *


def fibonacci3(n):
    fib=[]
    fib.append(1)
    fib.append(1)
    for i in range(2,n):
        fib.append(fib[i-1]+fib[i-2])
    return fib[n-1]

n=int(input("Inserisci n: "))
print("Fibonacci 3:", fibonacci3(n))
