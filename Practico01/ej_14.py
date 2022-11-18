from ej_12 import cholesky
from ej_03 import sol_trinf_fil,sol_trsup_fil
from ej_13 import matrix_generator
import numpy as np

def sol_defpos(A,b):
    G = cholesky(A)
    y = sol_trinf_fil(G.T,b)
    x = sol_trsup_fil(G,y)
    return x

if __name__ == "__main__":
    #n = 500
    #d = 10
    #A = matrix_generator(500)
    #b = [np.exp(-((j-n/d)**2)/100) for j in range(500)]

    A = np.array([
        [4,2,6],[2,2,5],[6,5,29]
    ])
    b = np.ones(3)


    x = sol_defpos(A,b)
    print(x)