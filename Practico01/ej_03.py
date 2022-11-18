import numpy as np
from numpy import linalg



Ainf = np.array([[1, 0, 0, 0],[-1, 1, 0, 0],[0, -1, 1, 0],[0, 0, -2, 2]],    dtype="float")
b1 = np.array([0, 0, 1, 1],  dtype="float")
Binf = np.array([[2, 0, 0, 0],[-1, 2, 0, 0],[3, 1, -1, 0],[4, 1, -3, 3]], dtype="float")
b2 = np.array([2, 3, 2, 9], dtype="float")
Csup = np.array([[9, 2, 4],[0, -6, 3],[0, 0, 5]], dtype="float")
b3 = np.array([18, -2, 7], dtype="float")
Dsup = np.array([[1, 2, -1, 1],[0, 1, 0, -1],[0, 0, -1, 4],[0, 0, 0, 1]], dtype="float")
b4 = np.array([2, -1, 0, 0], dtype="float")


def sol_trinf_fil(A, b):
    assert np.prod(np.diag(A)) != 0, "Error: la matriz es singular"

    n = len(b)
    x = b.copy()

    if n == 1:
        x[0] = x[0] / A[0, 0]
    else:
        k = 0
        while x[k] == 0 and k < n - 1:  # Si b_i = 0 => x_i = 0
            k += 1

        for i in range(k, n):  # Ya calculé los x hasta k
            x[i] = (x[i] - A[i, 0:i] @ x[0:i]) / A[i, i]

    return x
def sol_trin_col(A, b):
    assert np.prod(np.diag(A)) != 0,"Error: la matriz es singular"
    n = len(b)
    x = b.copy()

    if n==1:
        x[0]=x[0]/A[0, 0]
    else:
        k=0
        while x[k]==0 and k<n-1: #Si b_i = 0 => x_i = 0
            k+=1
        for i in range(k,n): #Ya calculé los x hasta k
            x[i] = x[i]/A[i,i]
            x[i+1:n] = (x[i+1:n] - A[i+1:n,i]*x[i])
    return x
def sol_trsup_fil(A, b):
    assert np.prod(np.diag(A)) != 0,"Error: la matriz es singular"
    n = len(b)-1
    x = b.copy()
    k=n
    while x[k]==0 and k>0: #Si b_i = 0 => x_i = 0
        k-=1

    for i in reversed(range(0,k+1)): #Ya calculé los x desde k hasta n.
        x[i] = (x[i]-(A[i,i+1:n+1]@x[i+1:n+1])) / A[i,i]
    return x
def sol_trsup_col(A, b):
    assert np.prod(np.diag(A)) != 0, "Error: la matriz es singular"
    n = len(b) - 1
    x = b.copy()
    k = n
    while x[k] == 0 and k > 0:  # Si b_i = 0 => x_i = 0
        k -= 1

    for i in reversed(range(k + 1)):  # Ya calculé los x desde k hasta n.
        x[i] = x[i] / A[i, i]
        x[0:i] = x[0:i] - (A[0:i, i] * x[i])
    return x