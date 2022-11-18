import numpy as np
def sol_Richardson(M,y, it):
    b=y.copy()
    A=M.copy()
    n=A[0,:].shape
    x=np.zeros(n)
    r=b-(A@x)
    l=np.linalg.eig(A)[0]
    l=np.sort(l)
    l1,ln=l[0], l[-1]
    a=2/(l1+ln)
    k=0
    while np.linalg.norm(r,2)>=1e-9 and k<=it:
        v=A@r
        x=x+(a*r)
        r=r-(a*v)
        k+=1
    return x