import numpy as np
n=int(input("Insérer la taille (doit être impaire) : "))
a=np.array([["XX" for _ in range(n)] for _ in range(n)],dtype=str)
for k in range(0,n):
    for i in range(0,n):
        a[(-i+2*k)%n,(int((n-1)/2)+i-k)%n]=f"{k*n+i+1}"
print(a)