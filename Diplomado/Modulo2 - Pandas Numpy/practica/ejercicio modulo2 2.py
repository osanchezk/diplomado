import numpy as np
rg = np.random.default_rng()
MatA = rg.integers(20, size = (4,3))
MatB = rg.integers(5, size = (3,2))
multiplicaMat = MatA @ MatB
print(MatA)
print(MatB)
print("Multiplicación de MatA  * \n" , multiplicaMat)