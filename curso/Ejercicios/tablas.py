"""
tabla de multiplicar
"""
print ("####################")
print ("Tabla de multiplicar")
print ("####################")
numTabla = int(input("Tabla de multipĺicar (num): "))
tope = int(input("Hasta que número: "))

for num in range(1,tope+1):
    print(f'{numTabla} x {num} = {numTabla * num}')