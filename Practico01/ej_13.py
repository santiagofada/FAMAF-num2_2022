import numpy as np
from ej_12 import cholesky

def matrix_generator(n):
    A = np.identity(n)*2
    B = np.diag(-np.ones(n-1),1)
    C = np.diag(-np.ones(n-1),-1)

    return A+B+C


if __name__ == "__main__":
    A = matrix_generator(100)
    G = cholesky(A)
    print(G)