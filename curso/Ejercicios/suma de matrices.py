matriz= [[1,2,3],[4,5,6],[7,8,9]]

f=len(matriz)
c=len(matriz[0])

#Suma de filas
for ren in range (f):
    total = 0
    for col in range (c):
        total= total+matriz[ren][col]
    print(f'La suma de la fila {ren} es igual a: {total}')
    
#Suma de columnas
for col in range (c):
    total = 0
    #for ren in range (len(matriz)):
    for ren in range (f):
        total= total+matriz[ren][col]
    print(f'La suma de la columna {col} es igual a: {total}')
    