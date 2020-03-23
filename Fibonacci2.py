from math import *


def fibonacci2(n):
    if (n<=2):
        return 1
    else:
        return (fibonacci2(n-1)+fibonacci2(n-2))


n=int(input("Inserisci n: "))
print("Fibonacci 2:", fibonacci2(n))
