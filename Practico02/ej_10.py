import numpy as np
from ej_5 import egauss
from Practico01.ej_03 import sol_trsup_fil
from ej_9 import egaussp,pivotGauss
from ej_11 import inverse

def sol_egauss(A_,b_):
    A,p = pivotGauss(A_)
    b = b_.copy()
    n = len(p)

    print(A)
    #swaping del vector b
    for k in range(n-1):
        i = p[k]
        temp = b[k]
        b[k] = b[i]
        b[i] = temp

    for j in range(n):
        for i in range(j+1,n):
            b[i] += A[i,j]*b[j]
    for j in range(n-1,0,-1):
        for i in range(j):
            b[i] -= A[i,j]*b[j]

    return b

def sol_egauss2(A_,b_):
    """
    seguimos el algoritmo 11 pagina 33
    :param A_:
    :param b_:
    :return:
    """
    U,y = egaussp(A_,b_)

    x = sol_trsup_fil(U,y)

    return x

"""
A1 = np.array([[1,1,3],
               [0,100,3],
               [1091,0,1]],dtype="float")
b1 = np.array([-8,8,2],dtype="float")

"""
A1 = np.array([[2, 10, 8, 8, 6],
                   [1, 4, -2, 4, -1],
                   [0, 2, 3, 2, 1],
                   [3, 8, 3, 10, 9],
                   [1, 4, 1, 2, 1]],
                  dtype="float")

b1 = np.array([52,14,12,51,15],dtype="float")
b2 = np.array([50,4,12,48,12],dtype="float")
s = sol_egauss2(A1,b2)
print(s)

#print(b1*inverse(A1))