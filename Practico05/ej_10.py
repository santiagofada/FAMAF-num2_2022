import numpy as np

def sol_gradcon(A_,b_, it):

    A=A_.copy()
    b=b_.copy()

    n=A.shape[1]

    x=np.ones(n)
    r0=b-(A@x)
    p=r0.copy()
    k=0
    while np.linalg.norm(r0,2)>=1e-4 and k<=it:
        v =np.dot(A, p)
        a = np.inner(r0,r0) / np.inner(v,p)
        x = x + (a*p)
        r1 = r0-(a*v)
        beta = (np.linalg.norm(r1,2)**2)/(np.linalg.norm(r0,2)**2)
        p = r1+(beta*p)
        r0 = r1.copy()
        k += 1
    return x