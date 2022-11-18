import numpy as np
from Practico05.ej_8 import sol_gradopt
from Practico05.ej_09 import sol_Richardson
from Practico05.ej_10 import sol_gradcon


iterations = 1000


##--ejercicio A--
print("EJERCICIO A")

M1=np.array([
    [9, -2, 0],
    [-2, 4, -1],
    [0, -1, 1]
], dtype=float)
y1 = np.array([5, 1, -5/6], dtype=float)

print(sol_gradopt(M1,y1,iterations))
print(sol_Richardson(M1,y1,iterations))
print(sol_gradcon(M1,y1,iterations))




##--ejercicio B--
print("\n\n\n\n\n\nEJERCICIO B")

M2 = np.array([
    [4, -1, 0],
    [-1, 4, -1],
    [0, -1, 4]
], dtype=float)
y2 = np.array([2, 6, 2], dtype=float)

print(sol_gradopt(M2,y2,iterations))
print(sol_Richardson(M2,y2,iterations))
print(sol_gradcon(M2,y2,iterations))


#--ejercicio C--
print("\n\n\n\n\n\nEJERCICIO C,D,E")
diag = 4
"""
diag = 4 ejercicio C
diag = 10,100,1000 ejercicio D
"""
def tribanda(n,k):
    A= np.diag(k*np.ones(n)) #Crea la matriz diagonal con 2 en la diagonal
    A= A + np.diag((-1)*np.ones(n-1), -1) #El segundo parametro te hace la diagonal 1 lugar por debajo de la principal
    A= A + np.diag((-1)*np.ones(n-1), 1)  #El segundo parametro te hace la diagonal 1 lugar por encima de la principal
    return A

def soluciones():
    soluciones=[]
    for j in range(5,25,5):
        A=tribanda(j,diag)
        b=np.ones(j)
        soluciones.append(sol_gradopt(A,b,iterations))
        soluciones.append(sol_Richardson(A,b,iterations))
        soluciones.append(sol_gradcon(A,b,iterations))
    return soluciones

sols=soluciones()
for j in sols:
    print(j,end="\n\n")

#--ejercicio F--
print("\n\n\n\n\n\nEJERCICIO F")
def HilberSystem(n):
    H=np.zeros((n,n))
    b=np.ones(n)
    for i in range(1,n+1):
        for j in range(1,n+1):
            H[i-1,j-1]=1/(1+i+j)
        b[i-1]=np.sum(H[i-1])
    return H,b
H,b=HilberSystem(3)
print(sol_gradopt(H,b,10000))
print(sol_Richardson(H,b,10000))
print(sol_gradcon(H,b,10000))