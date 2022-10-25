"""
Realiza un script en Python que pida al usuario los tamaños de una matriz 
y sus valores y calcule el determinante de dicha matriz.
"""

ren = int(input("Dame los renglones: "))
col = int(input("Dame las columnas: "))
val = int(input("que valores requieres que contenga tu matriz: "))

import numpy as np
generaMatriz = np.full((ren, col), val)
print(generaMatriz)
print(np.mean(generaMatriz))
print(np.max(generaMatriz))
print(np.min(generaMatriz))

