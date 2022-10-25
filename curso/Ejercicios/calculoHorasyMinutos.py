"""
Programa que dada la cantidad horas y minutos, nos indique a cuántos 
segundos equivale.  
  
Entrada: Cantidad de Horasnu y minutos
Proceso: 0.- Definimos una constante de 1 munuto a 60 segundos
         1.- Solicitamos Horas
         2.- Solicitamos Minutos
         3.- Calculamos las Horas * SEGUNDOS y el resultado por SEGUNDOS
         4.- Calculamos los Minutos * SEGUNDOS
         5.- Sumamos el resultado de punto 3 y 4
         6.- Mostramos los resultados de cada uno de ellas
Salida: Total en segundos
Autor: Omar K Sánchez
Fecha: 18/05/2022
"""

#Constantes
SEGUNDOS = 60

print ("\n")
print ("####################################################")
print ("##### Conversion de horas y minutos a Segundos #####")
print ("####################################################")

obtenemosHoras = int(input("\nCantidad de Horas (HH): "))
obtenemosMinutos = int(input("\nCantidad de Minutos (MM): "))
conversionHorasASegundos = (obtenemosHoras*SEGUNDOS)*SEGUNDOS
conversionMinutosASegundos =  obtenemosMinutos*SEGUNDOS
sumaDeSegundos = conversionHorasASegundos + conversionMinutosASegundos
print (f"\n{obtenemosHoras} hora(s) equivale a {conversionHorasASegundos} segundos")
print (f"\n{obtenemosMinutos} minuto(s) equivale a {conversionMinutosASegundos} segundos")
print (f"\nEl total de Horas y Minutos en segundos es de: {sumaDeSegundos} segundos")