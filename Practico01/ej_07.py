import matplotlib.pyplot as plt
import numpy as np



def transformacion_bola_unidad():
    """
    Esta función nos permite generar una matriz SDP aleatoria y
    visualizar cómo afecta a la bola unidad.
    """
    # definir mi matriz aleatoria SDP
    A = np.random.randn(2, 2)
    A = A @ A.T

    # Genero bola unidad
    r = np.linspace(0, 2 * np.pi, 100)
    cosenos = np.cos(r)
    senos = np.sin(r)

    # Genero transformación de la bola unidad
    y_0 = np.zeros(100)
    y_1 = np.zeros(100)
    for i in range(100):
        res = A @ np.array([cosenos[i], senos[i]])
        y_0[i] = res[0]
        y_1[i] = res[1]

    # Grafico ambas
    plt.plot(cosenos, senos, label="bola unidad")
    plt.plot(y_0, y_1, label="transformacion")
    plt.legend()
    plt.axis("equal")
    plt.show()

def nivel(N, niveles):
    # definir mi matriz aleatoria SDP
    A = np.random.randn(2, 2)
    A = A @ A.T

    # Crear un conjunto de puntos en x y en y.
    X = np.linspace(-3, 3, N)
    Y = np.linspace(-3, 3, N)

    # Generar un mallado del espacio XxY en R^2
    XX, YY = np.meshgrid(X, Y)
    ZZ = np.zeros((N, N))

    # Definir el valor de x.T A x en todos los pares ordenados
    for idx in range(N):
        for jdx in range(N):
            vector = np.array([
                XX[idx, jdx],
                YY[idx, jdx],
            ])
            ZZ[idx, jdx] = vector.T @ A @ vector

    # Contour nos permite generar las curvas de nivel
    fig, ax = plt.subplots()
    CS = ax.contour(XX, YY, ZZ, niveles)
    ax.clabel(CS, inline=True, fontsize=10)
    ax.axis("equal")
    plt.show()

nivel(100, [0, 1, 2, 3, 4])