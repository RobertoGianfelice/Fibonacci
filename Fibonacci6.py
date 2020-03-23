from math import *
m=[[1,1],[1,0]]
invProd=0
invPot=0

def prodotto(m1,m2):
   global invProd
   invProd+=1
   n=len(m1)
   mm=[[0,0],[0,0]]
   for r in range(n):
       for c in range(n):
           somma=0
           for k in range(n):
               somma+=m1[r][k]*m2[k][c]
           mm[r][c]=somma
   return mm

def potenzaDiMatrice(A,n):
    global invPot
    invPot+=1
    if (n<=1):
        M=[[1,0],[0,1]]
    else:
        M=potenzaDiMatrice(A,(int(n/2)))
        M=prodotto(M,M)
    if (n%2==1):
        M=prodotto(M,A)
    return M

n=int(input("Inserisci n: "))
R=potenzaDiMatrice(m,n-1)
print("Fibonacci 6:", R[0][0])
print("Invocazioni prodotto={}, invocazioni Potenza= {}".format(invPot, invProd))
