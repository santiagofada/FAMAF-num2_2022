import numpy as np

def sol_gradopt(M, y, it):
    b = y.copy()
    A = M.copy()
    n = A[0, :].shape
    x0 = np.zeros(n)
    r = b - (A @ x0)

    k = 0
    while np.linalg.norm(r, 2) >= 1e-9 and k <= it:
        v = A @ r
        a = (np.linalg.norm(r, 2) ** 2) / np.inner(v, r)
        x0 = x0 + (a * r)
        r = r - (a * v)
        k += 1
    return x0