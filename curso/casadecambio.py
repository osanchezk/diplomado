"""

Programa para una casa de cambio que reciba
pesos mexicanos y presente cuántos dólares entregaría

Operación: pesos mexicanos / dólar 

Fecha: 13/05/2022
Autor: OKSM

"""
print ("###################################################")
print ("##### Conversión de pesos mexicanos a dolares #####")
print ("###################################################")

precioDolar = float(input("Precio del dólar en pesos: "))
pesos = float(input("Cuanto dinero mexicano desde cambiar $: "))
calculoConversion = pesos/precioDolar
print (f"La cantidad de {pesos:.0f} pesos a entregar en dolares es: {calculoConversion:.2f}")

print ("\n\n");

print ("##################################################")
print ("##### Conversión de dolares a pesos mexicanos#####")
print ("##################################################")

precioDolar = float(input("Precio del dólar en pesos: "))
dolares = float(input("Cantidad de dólares: "))
calculoConversion = dolares * precioDolar
print (f"La cantidad de {dolares:.0f} dolares a entregar pesos mexicanos es: {calculoConversion:.2f}")
