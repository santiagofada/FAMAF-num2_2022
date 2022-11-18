import numpy as np
import scipy.linalg


def LU(A_):
    A = A_.copy()
    n = len(A[0])
    if n == 1:
        return A
    else:
        for k in range(n-1):

            A[k+1:n,k] = A[k+1:n,k]/A[k,k]
            A[k+1:n,k+1:n] -= np.outer(A[k+1:n,k],A[k,k+1:n])

    # Parte triangular superior
    U = np.triu(A)
    # Parte triangular inferior sin diagonal + identidad
    L = np.tril(A, -1) + np.eye(n)
    return L,U


if __name__=="__main__":
    A = np.array([[3,2,4],
                  [1,1,2],
                  [4,3,2.]],dtype="float")

    L,U = LU(A)
    print(L @ U)
