"""
==== Tienda departamental ====
Conocer cuánto es el precio total del producto ya aplicado el descuento. De 
manera que, tu programa deberá recibir el precio sin descuento del producto y el 
porcentaje que tiene de descuento. El resultado deberá ser, el monto a pagar, después 
del descuento.

Entrada: Precio del producto, porcentaje de descuento
Proceso: 1.- Solicitamos el precio del producto
         2.- Solicitamos porcentaje a aplicar
         3.- calculamos el precio del producto, multiplicarlo por (porcentaje / cien)
         4.- Realizamos la operación de descuento de precio del producto menos la comisión
Salida: Monto a pagar después de descuento
Autor: Omar K Sánchez
Fecha: 15/05/2022

"""

print ("\n")
print ("##############################################################")
print ("##### Precio total del producto ya aplicado el descuento #####")
print ("##############################################################")
precioTotal = float(input("\nPrecio del producto: "))
porcentajeAplicar = int(input("\nPorcentaje para aplicar(%): "))
descuento = precioTotal*(porcentajeAplicar / 100)
print (f"\nEl precio total del producto es de ${precioTotal:.2f} pesos, se le aplicó un descuento del {porcentajeAplicar}%, usted ahorra: {descuento} pesos")
print (f"\nEl precio con el descuento aplicado es de: {precioTotal-descuento:.2f} Pesos")

