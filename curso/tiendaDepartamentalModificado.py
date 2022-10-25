"""
==== Tienda departamental ====
==== Segunda Fase, Temporada de descuentos ====
Un producto puede tener la etiqueta del 50%+20%
El programa debe recibir el precio inicial y los dos descuentos y como 
resultado deberá mostrar el precio a pagar por el cliente después de los dos 
descuentos. 

Entrada: Precio inicial
Proceso: 1.- Definimos 2 constantes para el 50 y el 20 porciento
         2.- Solicitamos el precio del producto
         3.- Obtenemos el porcentaj de 50%: precioTotal*(PORCENTAJE 50 / cien)
         4.- Aplicamos el porcentaje y se lo restamos al precio del producto
         5.- El resultado del punto anterior le aplicamos el 20%: descuento del resultado del 50% *(PORCENTAJE 20 / cien)
         6.- Aplicamos el porcentaje del punto anterior y se lo restamos al precio con el descuento del 50%
Salida: Se muestra el precio con el descuento del 50%+20%
Autor: Omar K Sánchez
Fecha: 15/05/2022

"""

print ("\n")
print ("#########################################################################")
print ("##### Precio total del producto aplicando el descuento de 50%+20% #####")
print ("#########################################################################")

#Definimos 2 constantes
PORCENTAJE_50 = 50
PORCENTAJE_20 = 20

precioTotal = float(input("\nPrecio del producto($): "))

descuento_50 = precioTotal*(PORCENTAJE_50 / 100)
descuento_50Aplicado = precioTotal-descuento_50
descuento_20 = descuento_50Aplicado*(PORCENTAJE_20 / 100)
descuento_20Aplicado = descuento_50Aplicado-descuento_20
print(f"\nEl precio final del producto aplicando el {PORCENTAJE_50}%+{PORCENTAJE_20}% es de ${descuento_20Aplicado:.2f} pesos")
