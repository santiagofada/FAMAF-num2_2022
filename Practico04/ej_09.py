import numpy as np
from Practico04.ej_07 import sol_cuadmin
from Practico01.ej_12 import cholesky
from Practico01.ej_03 import sol_trsup_fil,sol_trinf_fil


def tribanda(n):
    A= np.diag((-1)*np.ones(n))
    A= A + np.diag((2)*np.ones(n-1), -1)
    A= A + np.diag((-1)*np.ones(n-2), -2)
    B = A[:,:-2]
    return B

def sol_QR(A,b):
    x= sol_cuadmin(A, b)[0]
    return x

def sol_ch(A,b): #Resuelvo el sistema (A.T@A)x = A.T@b
    #Creo el sistema de ec normales

    b = A.T@b
    A = A.T@A
    #Resuelvo el sistema
    G = cholesky(A)
    y = sol_trinf_fil(G.T, b)
    x = sol_trsup_fil(G, y)
    return x

if __name__=="__main__":
    n = 100
    A = tribanda(n)
    b = np.zeros(n)
    b[0] = b[-1] = 1

    print(sol_ch(A,b))
    print(end="\n\n\n")
    print(sol_QR(A,b))
