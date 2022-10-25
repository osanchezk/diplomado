
# -*- coding: utf-8 -*-
"""
Programa: Ejercicios de listas anidadas y matrices
Author: Omar K Sánchez
Fecha: 09/Junio/2022
"""

#Definimos librerias
from random import randint

#Definimos funciones

def menu():
    print("""
                                     LISTADO DE OPERACIONES

#######################################################################################################
###                                                                                                 ###
### 1    F1: Matriz de nXn y con asignación en cada indice con el valor de -1                       ###
### 2    F2: Matriz de nXn y con asignación en cada indice con el valor de la columna               ###
### 3    F3: Matriz de nXn y con asignación en cada indice con el valor del renglon                 ###
### 4    F4: Matriz de nXn y con asignación en cada indice random                                   ###
### 5    F5: Matriz de nXn y con número consecutivo a partir de uno, por renglones                  ###
### 6    F6: Matriz de nXn y con número consecutivo a partir de uno, por columnas                   ###
### 7    F7: Lista anidada de números y regresa total de #pares                                     ###
### 8    F8: Lista anidada de números, regresa total de números de valores mayores o iguales a cero ### 
### 9    F9: Lista anidada de números, regresa listado menosres a cero y colocandole un cero        ###
### 10  F10: Lista anidada de números, regresa listado menosres a cero y colocandole un cero        ###                                              
### 11  F11: Lista anidada de números, regresa True si esta x sino es False                         ###                                              
### 12  F12: Lista anidada de números, devuelve la suma de los números mayores a 5                  ###                                              
### 13  F13: Lista anidada de números, coloca ceros en la matriz y luego su su número de renglón    ### 
###          por su número de columna                                                               ###
###                                                                                                 ###
### 20  Salir                                                                                       ###
###                                                                                                 ###
#######################################################################################################

    """)


def crea_Matriz(r,c,s):
    m=[]
    cta=0
    for i in range(r): #Renglones
        f=[]
        for j in range(c): #Columnas
            if s=="especial":
                dat="-1"
            elif s=="col":
                dat=r
            elif s=="ren":
                dat=c
            elif s=="ran":
                dat=randint(1,100)
            elif s=="consecxr":
                cta+=1
                dat=cta
            elif s=="consecxc":
                cta+=1
                dat=cta
            elif s=="ceros":                
                dat=0
            else:
                dat=int(input(f"Dame el valor de la posición {i} {j}: "))            
            f.append(dat)
        m.append(f)
    return m        

def crea_Matriz5(newMatriz):
    #Se queda esa solución
    cta=0
    #print(*newMatriz, sep="\n")
    for fila in range(len(newMatriz)):
        for columna in range(len(newMatriz[0])):
            cta+=1
            #print(f"[{columna}][{fila}]-[{cta}]")
            newMatriz[columna][fila] = cta
    print(*newMatriz, sep="\n")

def barre_y_suma(newMatriz):
    suma=0
    cta=0
    for fila in range(len(newMatriz)):
        for columna in range(len(newMatriz[0])):
            cta+=1
            newMatriz[fila][columna] = cta
            print(f"Este es el consecutivo [{fila}][{columna}]")
            suma = fila + columna
            newMatriz[fila][columna] = suma
    print(*newMatriz, sep="\n")
            
def pintaMatriz(t):
    if t=="consecxc":
        #Se realiza este ajuste para que funciones a mi matriz cuadrada
        r = int(input("Cuantos renglones y columnas deseas par ala matriz cuadrada: "))
        #c = int(input("Cuantas columnas de la matriz desdeas: "))    
        matrizF1 = crea_Matriz(r,r,s=t)                
        crea_Matriz5(matrizF1)        
    elif t=="ceros":
        r = int(input("Cuantos renglones y columnas deseas par ala matriz cuadrada: "))
        matrizF1 = crea_Matriz(r,r,s=t)
        barre_y_suma(matrizF1)
        
    else:
        r = int(input("Cuantas renglones de la matriz desdeas: "))
        c = int(input("Cuantas columnas de la matriz desdeas: "))    
        matrizF1 = crea_Matriz(r,c,s=t)        
        print(*matrizF1, sep="\n")

def generaLista(dat):
    guardaLista = []
    while True:
        numLista = int(input(f"Dame un nÚmero para agregar a la {dat} lista: "))
        guardaLista.append(numLista)
        op=input('Desea agregar otro dato? (si|no): ')
        op=op.lower()
        if (op=='si'):
            continue
        else:
            break
    return guardaLista

def cuenta_pares():
    primera = generaLista("primera")
    segunda = generaLista("segunda")
    tercera = primera + segunda
    cta=0
    for i in range(len(tercera)):
        if tercera[i]%2==0:
            cta+=1
    print(f"El total de numero pares es: {cta}")
    
def cuenta_positivos():
    primera = generaLista("primera")
    segunda = generaLista("segunda")
    tercera = primera + segunda
    cta=0
    for i in range(len(tercera)):
        if tercera[i]>=0:
            cta+=1
    print(f"El total de numero positivos es: {cta}")
    
def cambia_negativos():
    primera = generaLista("primera")
    segunda = generaLista("segunda")
    tercera = primera + segunda
    for i in range(len(tercera)):
        if tercera[i]<=0:
            tercera[i] = 0
    print(f"La cantidad de negativos es de: {tercera}")

def cuenta_repeticiones():
    primera = generaLista("primera")
    segunda = generaLista("segunda")
    tercera = primera + segunda
    dameNum = int(input("Dame número para buscar en la lista anidada y contarlas: "))
    cta=0
    for i in range(len(tercera)):
        if tercera[i]==dameNum:
            cta+=1
    print(f"El total de repeticiones del número {dameNum} es de: {cta}")

def busca():
    primera = generaLista("primera")
    segunda = generaLista("segunda")
    tercera = primera + segunda
    dameNum = int(input("Dame número para buscar en la lista anidada: "))
    for i in range(len(tercera)):
        if tercera[i]==dameNum:
            val = "TRUE"
            break
        else:
            val = "FALSE"
            break
    print (f"Status: {val}")


def suma_mayores5():
    primera = generaLista("primera")
    segunda = generaLista("segunda")
    tercera = primera + segunda
    dameNum = int(input("Agrega el número tope para sumar: "))
    suma=0
    for i in range(len(tercera)):
        if tercera[i]>dameNum:
            suma+=tercera[i]
    print(f"El total de la suma de numeros mayores a cero es: {suma}")    
    
itera = 0
while True:
    menu()
    opcion = int(input("Eliga la funcion que dease utilizar: "))
    print("\n")
    if opcion==1:
        pintaMatriz("especial")
    elif opcion==2:
        pintaMatriz("col")
    elif opcion==3:
        pintaMatriz("ren")        
    elif opcion==4:
        pintaMatriz("ran")                
    elif opcion==5:
        pintaMatriz("consecxr")                
    elif opcion==6:
        pintaMatriz("consecxc")
    elif opcion==7:
        cuenta_pares()                        
    elif opcion==8:
        cuenta_positivos()
    elif opcion==9:
        cambia_negativos()                                                
    elif opcion==10:
        cuenta_repeticiones()                                                        
    elif opcion==11:
        busca()                                                        
    elif opcion==12:
        suma_mayores5()                                                        
    elif opcion==13:
        pintaMatriz("ceros")
    elif opcion==20:
        break
    else:
        print("Opción inválida!")
        break

    op=input('Desea salir? (si|no): ')
    op=op.lower()
    itera+=1
    if (op=='si'):
        break
    else:
        continue

print("###########################################")   
print("#### Gracias por utilizar el programa #####")
print("###########################################")
print(f"##### Total de operaciones: {itera} #######")
print("###########################################")
