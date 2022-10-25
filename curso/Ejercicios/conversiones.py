"""
Programa que convierta una medida en centimetros a pies, pulgadas y 
yardas. El programa recibe la cantidad de centímetros y muestra a pantalla su 
equivalente en pies, pulgadas y yardas. 
Entrada: Cantidad de centimetros
Proceso: 1.- Almacenamos 3 constantes de los valores de pies, pulgadas y yardas
         2.- Solicitamos la cantidad en centimetros
         3.- Calculamos los Centimetros entre los PIES
         4.- Calculamos los Centimetros entre las PULGADAS
         5.- Calculamos los Centimetros entre las YARDAS
         6.- Mostramos los resultados de cada uno de ellas
Salida: Los 3 resultados (pies, pulgadas y yardas)
Autor: Omar K Sánchez
Fecha: 17/05/2022
"""

#Constantes
PIES = 30.48
PULGADA = 2.54
YARDAS = 91.44

print ("\n")
print ("###############################################################")
print ("##### Conversion de centimetros a pies, pulgadas y yardas #####")
print ("###############################################################")

obtenemosCentimetros = float(input("\nTotal de centimetros a convertir (cm): "))
conversionAPies = obtenemosCentimetros/PIES
print (f"La conversión de centimetros a pies es de: {conversionAPies:.2f} pies")
conversionAPulgadas = obtenemosCentimetros/PULGADA
print (f"La conversión de centimetros a pulgadas es de: {conversionAPulgadas:.2f} pulgadas")
conversionAYardas = obtenemosCentimetros/YARDAS
print (f"La conversión de centimetros a yardas es de: {conversionAYardas:.2f} yardas")