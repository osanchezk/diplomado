"""
De acuerdo al monto total de la cuenta de la mesa y el porcentaje de propina que quieren 
dejar, se repartan el monto de la propina entre un número de comensales. El 
programa deberá arrojar lo que debe aportar cada uno.

Entrada: Total de consumo, Número de comensales, Porcentaje a aplicar
Proceso: 1.- Solicitamos el total de consumo en pesos mexicanos
         2.- Solicitamos el total de comensales
         3.- Solitamos el porcentaje a aplicar
         4.- Obtenemos la propina: total * (porcentaje / cien)
         5.- Obtenesmo el total por cada comensal: calculoPorcentaje = propina / comensales
Salida: Mostramos el total de consumo y la reparticion de la comision de cada comensal
Autor: Omar K Sánchez
Fecha: 15/05/2022

"""

print ("\n")
print ("#################################################################################")
print ("##### Propina distribuida por el total de comensales, del total del consumo #####")
print ("#################################################################################")
total = float (input("\nCantidad total en pesos mexicanos del consumo de alimentos ($):"))
comensales = int(input("\nNúmero de comensales: "))
porcentaje = int (input("\nPorcentaje para aplicar(%): "))
propina = total*(porcentaje / 100)
calculoPorcentaje = propina / comensales
print (f"\nLa propina a entregar al mesero es: ${propina} Pesos; a cada comensal le toca un total de {calculoPorcentaje} pesos" )
print("\n")