import matplotlib.pyplot as plt
import numpy as np
from ej_10 import sol_egauss2
def graficar_circunferencia(u, v, w):
    # chequear no colinealidad? en teoria si fueran colineales no podríamos resolver el sistema...

    # Armar sistema
    #[a, b, c]

    A = np.array([
        [u[0],u[1],1],
        [v[0],v[1],1],
        [w[0],w[1],1],
    ],dtype=float)

    b = - np.array([u[0]**2 + u[1]**2, v[0]**2 + v[1]**2, w[0]**2 + w[1]**2],dtype=float)

    # x = [a, b, c]
    x = sol_egauss2(A, b)

    # graficar puntos iniciales
    p = [u,v,w]
    for i in range(3):
        plt.scatter(p[i][0], p[i][1],color="purple")

    # armar circunferencia a partir de muchos puntos entre 0 y 2pi
    circunferencia = np.linspace(0, 2 * np.pi, 100)

    radio = np.sqrt((x[0]**2 + x[1]**2) / 4 - x[2])
    # trasladar la circunferencia al punto central luego de multiplicar por el radio
    x_circunferencia = (np.cos(circunferencia)) * radio - x[0] / 2
    y_circunferencia = (np.sin(circunferencia)) * radio - x[1] / 2

    plt.plot(x_circunferencia, y_circunferencia, "orange")
    # ejes con misma escala
    plt.axis("equal")
    plt.grid()
    plt.show()

graficar_circunferencia((1,2), (3,4), (-7,9))