import numpy as np
#Una dimensión
#a = np.array([10,20,30,40,50])
#b = np.array([1,2,3,4,5])
#resta = a - b
#print("Resultados de la resta de arreglos: \n", resta)

#2 dimensiones
#rg = np.random.default_rng()
#MatA = rg.integers(20, size= (3,3))
#MatB = rg.integers(5, size = (3,3))
#sumaMat = MatA + MatB
#print ( "MatA : \n ", MatA)
#print ( "MatB: \n ", MatB)
#print ( "Suma de MatA + MatB: \n ",  sumaMat)


arreglo = np.arange(6)
print ( "Arreglo: ", arreglo)
cuadrados  =  arreglo**2
print ( "Valores del arreglo al cuadrado: ", cuadrados )
arrescalar = arreglo * 5
print ( "Valores del arreglo por un escalar  5 :  ",  arrescalar )