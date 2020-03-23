from math import *

def prodotto(m1,m2):
   n=len(m1)
   mm=[[0,0],[0,0]]
   for r in range(n):
       for c in range(n):
           somma=0
           for k in range(n):
               somma+=m1[r][k]*m2[k][c]
           mm[r][c]=somma
   return mm

def fibonacci5(n):
    M=[[1,0],[0,1]]
    R=[[1,1],[1,0]]

    for i in range(1,n):
        M=prodotto(M,R)
    return M[0][0]

n=int(input("Inserisci n: "))
print("Fibonacci 5:", fibonacci5(n))
