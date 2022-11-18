import numpy as np


def cholesky(A):
    """
    Implementación del algoritmo de descomposición de Cholesky, versión producto exterior.
    Dado un arreglo bidimensional A, devuelve G triangular superior tal que np.dot(G.T, G) = A
    Esta función actúa sobre el arreglo A, por lo que al terminar la función el mismo se va a
    modificar. Para poder mantener A, es posible definir G como una copia de A, pero hay que
    realizar otras operaciones para terminar de tener una matriz triangular superior.
    """


    n = A.shape[0]
    G = np.zeros((n, n))

    for i in range(n):
        if A[i, i] <= 0:
            print("A no es definida positiva")
            break
        G[i, i] = np.sqrt(A[i, i])  # = A[i, i] ** 0.5
        # J = {i + 1, n} -> J Python i+1:n
        G[i, i + 1:n] = A[i, i + 1:n] / G[i, i]
        A[i + 1:n, i + 1:n] = A[i + 1:n, i + 1:n] - np.outer(G[i, i + 1:n], G[i, i + 1:n])

    return G
if __name__ == "__main__":
    A = np.array([
        [4, 2, 6],
        [2, 2, 5],
        [6, 5, 29],], dtype=float)
    G = cholesky(A)
    print(G)
    print(G.T @ G)