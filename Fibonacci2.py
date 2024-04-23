from math import *
invocazioni=0

def fibonacci2(n):
    global invocazioni
    invocazioni+=1
    if (n<=2):
        return 1
    else:
        return (fibonacci2(n-1)+fibonacci2(n-2))


n=int(input("Inserisci n: "))
print("Fibonacci 2:", fibonacci2(n))
print(f"Invocazioni {invocazioni}")
