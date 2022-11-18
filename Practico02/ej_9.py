import numpy as np

def pivotLU(A):
    n = A.shape[0]
    p = np.arange(n)

    for k in range(n-1):
        # Ubicar maximo desde la columna hacia abajo
        kmax = np.argmax(np.abs(A[k:n, k])) + k
        if kmax != k:
            # Pivoteo p y A
            par_index = [kmax, k]
            p[[k, kmax]] = p[par_index]
            A[[k, kmax], :] = A[par_index, :]

        # Vector de multiplicadores
        A[k+1:n, k] = A[k+1:n, k] / A[k, k]
        # Para aplicar el vector de multiplicadores en vez de usar un for, podemos hacer un producto exterior
        A[k+1:n, k+1:n] -= np.outer(A[k+1:n, k], A[k, k+1:n])

    # Parte triangular superior
    U = np.triu(A)
    # Parte triangular inferior sin diagonal + identidad
    L = np.tril(A, -1) + np.eye(n)

    return p, L, U

def pivotGauss(A_):
    # PREGUNTAR PORQUE ESTA ES LA QUE ANDA ANDANDO MAL
    A = A_.copy()
    n = len(A[0])
    v = np.zeros(n)
    p = np.arange(n)#vector que nos indica el orden de las filas

    for k in range(n-1):
        # Obtener el indice del maximo elemento(en valor abs)
        # Preguntar porque le sumamos k de la columna k
        kmax = np.argmax(np.abs(A[k:n,k])) + k
        if kmax != k:
            #pivoteamos las filas
            p[[k,kmax]] = p[[kmax,k]]
            A[[k,kmax],:] = A[[kmax,k],:]
        # I={k+1,...,n} ---> k+1:n
        # J={k,...,n}   ---> k:n
        v[k + 1:n] = A[k + 1:n, k] / A[k, k]
        A[k + 1:n, k:n] = A[k + 1:n, k:n] - np.outer(v[k + 1:n], A[k, k:n])
    return A,p
def egaussp(A, b):
    n = A.shape[0]
    U = A.copy()
    y = b.copy()

    for k in range(n):
        if np.max(np.abs(U[k:n, k])) != 0:
            # Elegimos el pivot
            pivot = k + np.argmax(np.abs(U[k:n, k]))
            # Pivoteamos (sin multiplicar por matriz elemental)
            U[[k, pivot], :] = U[[pivot, k], :]
            y[[k, pivot]] = y[[pivot, k]]
            # Reducir
            v = U[k + 1:, k] / U[k, k]
            U[k + 1:, k] = 0
            U[k + 1:, k + 1:] = U[k + 1:, k + 1:] - np.outer(v, U[k, k + 1:])
            y[k + 1:] = y[k + 1:] - v * y[k]

    return U, y

if __name__ == "__main__":
    A = np.array([[2, 10, 8, 8, 6],
                  [1, 4, -2, 4, -1],
                  [0, 2, 3, 2, 1],
                  [3, 8, 3, 10, 9],
                  [1, 4, 1, 2, 1]],
                 dtype=float)
    B = A.copy()
    p,L,U = pivotLU(A)
    print((L@U))
    print(B[p,:])

    #LU = B[p,:]