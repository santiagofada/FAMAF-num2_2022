import numpy as np
import numpy.linalg as l
#Esta linea es para que no me aparezcan numeros en notacion cientifica
np.set_printoptions(precision = 2, suppress = True)

def soltrsupfil(Z,c):
    b = c.copy()
    k = np.max(np.nonzero(b))
    for i in reversed(range(k + 1)):
        b[i] = (b[i] - Z[i, i + 1:] @ b[i + 1:] ) / Z[i,i]
    return b


#Funcion que utilizare en qrgivens
def givens(a, b):
    c = a / np.sqrt(a**2 + b**2)
    s = b / np.sqrt(a**2 + b**2)

    return c, s
def qrgivens(F):
    # Estas lineas es para que el algoritmo funcione con marices rectangulares
    m, n = F.shape
    Q = np.eye(m)
    A = F.copy()
    r = min(m - 1, n)
    # Estos for recorren todos los elementos debajo de la diagonal de la matriz
    for j in range(r):
        for i in range(j + 1, m):
            # calculo givens (Se sirua en el elemento diagonal y de ahi va recorriendo para abajo)
            c, s = givens(A[j, j], A[i, j])

            rot = np.array([[c, s],
                            [-s, c]])

            indices = [j, i]

            # Como la multiplicacion por izquierda(derecha) por la matriz de rotacion plana solo modifica
            # las filas(columnas), no multiplico toda la matriz, solo estas filas(columnas)
            A[indices, :] = rot @ A[indices, :]
            Q[:, indices] = Q[:, indices] @ rot.T

    return Q, A  # A es R


def hh_vector(x):
    # u, rho = hh_vector(x)
    # Calcula u y rho tal que Q = I - rho u u^T
    # cumple Qx = \|x\|_2 e^1

    n = len(x)
    rho = 0
    u = x.copy()
    u[0] = 1.

    if n == 1:
        sigma = 0
    else:
        sigma = np.sum(x[1:] ** 2)

    if sigma > 0 or x[0] < 0:
        mu = np.sqrt(x[0] ** 2 + sigma)
        if x[0] <= 0:
            gamma = x[0] - mu
        else:
            gamma = -sigma / (x[0] + mu)

        rho = 2 * gamma ** 2 / (gamma ** 2 + sigma)
        u = u / gamma
        u[0] = 1

    return u, rho
def qrhholder(A):
    m, n = A.shape
    Q = np.eye(m)
    R = A.copy()
    p = min(m, n)

    for j in range(p):
        # I = j:, J = j:
        u, rho = hh_vector(R[j:, j])
        w = rho * u
        R[j:, j:] = R[j:, j:] - np.outer(w, u.T @ R[j:, j:])
        Q[:, j:] = Q[:, j:] - Q[:, j:] @ np.outer(w, u)

    return Q, R

if __name__=="__main__":
    A = np.array([
        [2, 3, 5, 5],
        [5, 7, 6, 7],
        [2, 4, 6, 0],
        [2, 5, 9, 8]], dtype=float)

    S = np.array([[2, 3],
                  [5, 7]], dtype=float)

    b = np.array([12, 29, 4, 9], dtype=float)


    print(qrhholder(A)[0]@qrhholder(A)[1],end="\n\n")
