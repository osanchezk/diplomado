"""
    Programa que calcula la raíz cuadrada de un numero dado
"""

#from math import sqrt

#print ("Programa que calcula la raíz cuadrada de un numero dado")
#num=int(input("Dame un número para obtener su raíz: "))
#raiz=sqrt(num)
#print(f"{raiz:.4f}")

"""
###################################################################
###################################################################
"""
"""
    Calculamos el volumen de una esfera
    V = 4/3 * pi * radio a la 3
"""
#Constante

#PI = 3.1416
from math import pi

obtenerRadio = float(input("Radio: "))
calculamosVolumen = (4/3)*pi*obtenerRadio**3
print(f"{calculamosVolumen:.2f} Centimetros cubicos")

