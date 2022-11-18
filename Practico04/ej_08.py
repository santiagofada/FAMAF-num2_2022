import numpy as np

from Practico01.ej_03 import sol_trsup_fil,sol_trinf_fil
from Practico04.ej_07 import sol_cuadmin
from Practico02.ej_6 import LU


def sol_tradicional(A_, b_):
    A = A_.copy()
    b = b_.copy()
    b = A.T @ b
    A = A.T @ A
    L, U = LU(A)
    y = sol_trsup_fil(L, b)
    x = sol_trinf_fil(U, y)
    return x


def sol_QR(F, s):
    return sol_cuadmin(F, s)

def mtrx(x):
    A=np.array([
        [1,1],
        [x, 0],
        [0, x]
    ],dtype=float)
    return A






if __name__=="__main__":
    b = np.array([1, 1, 1], dtype=float)
    for k in range(1,5):
        A = mtrx(k)

        print(sol_tradicional(A, b))
        print(sol_QR(A, b))