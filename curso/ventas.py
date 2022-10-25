"""
Calculo de total de ventas y promedio de ventas
OKSM -X 
14/05/2022
"""

print ("###########################################")
print ("###  Calculo total de ventas y promedio ###")
print ("###########################################")

print ("""
   #####   MENU   #####
   VENTA1................
   VENTA2................
   VENTA3................
   VENTA4................
   VENTA5................
   VENTA6................
""")

print ("\n\t#####   MENU   #####\n\tVENTA1................\n\tVENTA2................\n\tVENTA3................\n\tVENTA4................\n\tVENTA5................\n\tVENTA6................\n")

venta1 = float(input("\tDame la primera venta: $"))
venta2 = float(input("\tDame la segunda venta: $"))
venta3 = float(input("\tDame la tercera venta: $"))
venta4 = float(input("\tDame la cuarta venta: $"))
venta5 = float(input("\tDame la quinta venta: $"))
venta6 = float(input("\tDame la sexta venta: $"))

sumaVenta = venta1 + venta2 + venta3 + venta4 + venta5 + venta5 + venta6
promedioVenta = sumaVenta / 6

print (f"\n\tLa suma total de la venta es: {sumaVenta:.2f} ")
print (f"\n\tEl promedio de venta es: ${promedioVenta:.2f}")



