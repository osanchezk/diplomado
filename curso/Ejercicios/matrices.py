ren=int(input("Dime la cantidad de renglones: "))
col=int(input("Dime la cantidad de columnas: "))

matriz=[]

for renglon in range(ren): #For que controla la posición de fila
    fila=[]  # Se inicia una lista vacia
    for columna in range(col): #For para recorrer posiciones (Columnas)
        dato=int(input(f"Dame el valor de la posición {renglon} {columna}: "))
        fila.append(dato) #Escribir el dato en la fila
    matriz.append(fila) # Escribir el dato en la matriz
print(matriz)    #Imprime los valores de lista
print()
#print(*matriz, sep="\n")  #Imprime como matriz
print()
total = 0
"""
for renglon in matriz:  #Imprime formato renglon
    for dato in renglon:
        total = total + dato
        print (dato, end=' ')
    print()
"""    
print("El total de la suma es: ", total)