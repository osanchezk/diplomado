"""
Simulación
Numeros Aleatorios - > Fraccciones
Numeros Aleatorios - > Enteros
"""
import numpy as np

rg = np.random.default_rng()

#Float
#One Dimension
aleatorio = rg.random(4)
print("Matriz de números aleatorios: \n", aleatorio)

#Two Dimensions
aleatorio2 = rg.random((4,5))
print("Matriz de números aleatorios: \n", aleatorio2)

#Integer
#One Dimension
rgInt = np.random.randint(2, size=5)
print("Matriz de números aleatorios: \n", rgInt)

#Two Dimensions
rgInt2 = np.random.randint(2, size=(5,2))
print("Matriz de números aleatorios: \n", rgInt2)