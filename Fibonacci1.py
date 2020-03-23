from math import *

def fibonacci1(n):
    nAureo=(1+sqrt(5))/2
    nAureoPrimo=(1-sqrt(5))/2

    return ((nAureo**n-nAureoPrimo**n)/sqrt(5))




n=int(input("Inserisci n: "))
print("Fibonacci 1:", fibonacci1(n))
