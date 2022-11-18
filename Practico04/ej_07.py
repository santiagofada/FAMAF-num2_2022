import numpy as np
from Practico01.ej_03 import sol_trsup_col
from Practico04.ej_03 import qrhholder


#En vez de usar givens usar householder
def sol_cuadmin(A, b):
    m, n = A.shape

    #Asumimos que A tiene rango completo
    p = np.min([m,n])
    y_sol = np.zeros(n)
    # I = {1, ... , p} -> :p
    # J = {1, ... , p} \ I = {p+1, ... , n} -> p:

    Q, R = qrhholder(A)

    q = Q.T @ b

    y_sol[:p] = sol_trsup_col(R[ :p, :p], q[:p])

    residuo = np.linalg.norm(q[p:])

    return y_sol, residuo

if __name__=="__main__":
    A = np.array([[1,1],
                  [0.5,0],
                  [0,0.5]], dtype=float)

    b = np.array([1,1,1], dtype=float)

    #x_sombrero = np.linalg.lstsq(A, b)
    y_sombrero = sol_cuadmin(A, b)
    #print(x_sombrero)
    print(y_sombrero)