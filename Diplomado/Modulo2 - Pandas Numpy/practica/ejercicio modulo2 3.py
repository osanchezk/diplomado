import numpy as np
from scipy import linalg
rg = np.random.default_rng()
MatA = rg.integers(30, size=(4,3))
#print(MatA,"\n")

#Transpuesta
#transpuesta = np.transpose(MatA)
#print(transpuesta)

#Inversa
inversa = np.linalg.inv(MatA)
print(inversa)