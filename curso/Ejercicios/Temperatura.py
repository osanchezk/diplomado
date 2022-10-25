""""
costo_actual = float(input(" Precio real del prodcuto: "))
venta = float(input(" Monto de las ventas: "))
 
if(costo_actual > venta):
    monto_total = costo_actual - venta
    print("Total de la perdida = {0}".format(monto_total))
elif(venta > costo_actual):
    monto_total = venta - costo_actual
    print("Beneficio = {0}".format(monto_total))
else:
    print("Sin ganacias y perdidas")
"""
""""
n = int(input("Que multiplicación requieres: "))

for f in range(1,11):
	multiplicacion = n * f 
	print(f'{n} x {f} = {multiplicacion}')

""""

n = int(input("Dame un numero: "))
otro = pow(n)
