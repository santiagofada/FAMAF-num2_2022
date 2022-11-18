import numpy as np

def egauss(A_, b_):
    # lleva una matriz a una triangular superior
    A = A_.copy()
    b = b_.copy()
    v = np.zeros(len(b))
    n = A.shape[0]

    for k in range(n - 1):
        # I={k+1,...,n} ---> k+1:n
        # J={k,...,n}   ---> k:n
        v[k+1:n] = A[k+1:n,k]/A[k,k]
        A[k+1:n,k:n] = A[k+1:n,k:n] - np.outer(v[k+1:n],A[k,k:n])
        b[k+1:n]  = b[k+1:n] - v[k+1:n]*b[k]
    return A, b





