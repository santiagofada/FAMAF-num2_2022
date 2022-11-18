import numpy as np
from Practico01.ej_03 import sol_trinf_fil,sol_trsup_fil
from ej_9 import pivotLU
def inverse(A):
    n = len(A[0])
    p,L,U = pivotLU(A)
    I = np.zeros([n,n])

    for i in range(n):
        v = np.zeros(n)
        v[i] = 1
        y = sol_trinf_fil(L,v)

        x = sol_trsup_fil(U,y)

        I[i] = x

    return I[p,:].T



if __name__=="__main__":
    A = np.array([[3, 2, 4],
                  [1, 1, 2],
                  [4, 3, 2.]], dtype="float")

    print(inverse(A))
