from scipy.optimize import linprog
import matplotlib.pyplot as plt
import numpy as np
from Practico04.ej_07 import sol_cuadmin


a = np.ones(10)
b = np.arange(1,11)
A = np.column_stack((a,b))


yi = np.arange(1, 11, 1)
yi[-1] = 0
xi = np.arange(1, 11, 1)

x = sol_cuadmin(A, yi)[0]
print(x)



fig, ax = plt.subplots()
#Ploteo norma 2
plt.plot(xi, yi, 'o', color='purple')
plt.plot(xi, x[0] * xi + x[1] , color='green', label='Norma 2')

#Ploteo norma 1
A_ub = np.zeros((20,12))
A_ub[:10, :2] = A
A_ub[10:, :2] = -A
A_ub[:10, 2:] = -np.eye(10)
A_ub[10:, 2:] = -np.eye(10)
c = np.ones(12)
c[:2] = 0
b_ub = np.zeros(20)
b_ub[:10] = yi
b_ub[10:] = -yi
norma_uno = linprog(c, A_ub, b_ub)
recta_norma_uno = norma_uno.x[:2]
plt.plot(xi, recta_norma_uno[0] * xi + recta_norma_uno[1], label='Norma 1')

#Ploteo norma infinito
A_ub_inf = np.zeros((20,3))
A_ub_inf[:10, :2] = A
A_ub_inf[10:, :2] = -A
A_ub_inf[:, 2] = - np.ones(20)
b_ub_inf = b_ub
c_inf = np.array([0,0,1])
norma_inf = linprog(c_inf, A_ub_inf, b_ub_inf)
recta_norma_inf = norma_inf.x[:2]
plt.plot(xi, recta_norma_inf[0] * xi + recta_norma_inf[1], label='Norma infinito')



plt.legend()
plt.grid()
plt.show()
