from math import *



def fibonacci4(n):
    a=b=c=1
    for i in range(2,n):
        c=a+b
        a=b
        b=c
    return b

n=int(input("Inserisci n: "))
print("Fibonacci 4:", fibonacci4(n))
