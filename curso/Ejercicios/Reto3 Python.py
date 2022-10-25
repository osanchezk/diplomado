"""
programa que de inicio tenga un menú, en donde muestre las funciones u
operaciones que puede resolver el programa.
Resolver al menos 7 de las 16 funciones
Autor: Omar K Sánchez
Fecha: 02/06/2022

Observación: Se realizaron 14 de 16; la 11 no me quedó claro y la 13 ya no me dio tiempo de realizarla por trabajo
"""
from random import randint


def operadores():
    print("""
    LISTADO DE OPERACIONES
_______________________________
    
1   Función que debe devolver cuántos de los elementos de la lista son mayores a n
2   Funcion que devuelve cuántos de los strings de la lista tiene n letras o mas
3   Función que deberá devolver cuántas de esas palabras empiezan con la letra recibida
4   Función que modifica el valor de los elementos de la lista a su doble
5   Función que devuelve otro string en el cual cambian letras
6   Función que deverá devolver otro string en el cual se hayan cambiado las vocales en que estaban en minúsculas por mayúsculas
7   Funcion que recibe un string y devuelve otro, con un espacio en cada caracter
8   Función que invierte que recibe como parámetro en una lista y devuelve otra lista con los datos invertidos.
9   Función que recibe dos listas, como resultado devuelve una lista con los datos de las dos listas intercaladas
10  Función que recibe un numero entero y devuelve la suma de los puntos generados por la simulación de tirar n veces un dado
11  Función que recibe un string y devuleve otro string con las letras del string recibido pero en desorden
12  Función que recibe una lista de string y un numero, modifica la lista y de cada elemento debe de dejar solo x primero caracteres
13  Función que recibe dos cadenas, devuelve cuantas letras coinciden de manera continua en las dos cadenas
14  Función que recibe una lista de datos numéricos y te regresa otra lista con los 3 elementos mas pequeños de una lista
15  Función la cual recibe como parámetro dos listas, deberá devolver otra lista con los elementos que coinciden en las dos listas
16  Función que recibe una cadena y un número, crea una nueva cadena con la cadena original pero dividida en guiones cada intervalo
    del número recibido
17  Salir    
_______________________________

    """)

### Funciones

#Generamos una lista
def generaLista(tipo):
    guardaLista = []
    while True:
        if tipo=='int':
            numLista = int(input("Dame un número para agregar a la lista: "))
        else:
            numLista = input("Dame un string para agregar a la lista: ")
        guardaLista.append(numLista)
        op=input('Desea agregar otro dato? (si|no): ')
        op=op.lower()
        if (op=='si'):
            continue
        else:
            break
    return guardaLista

#Generamos una segunda lista
def generaSegundaLista(tipo):
    guardaSegundaLista = []
    while True:
        if tipo=='int':
            numSegLista = int(input("Dame un número para agregar a la lista: "))
        else:
            numSegLista = input("Dame un string para agregar a la lista: ")
        guardaSegundaLista.append(numSegLista)
        op=input('Desea agregar otro dato? (si|no): ')
        op=op.lower()
        if (op=='si'):
            continue
        else:
            break
    return guardaSegundaLista

def generaListaCondicion(tipo):
    guardaLista = []
    i = 1
    while True:
        if tipo=='int':
            numLista = int(input("Dame un número para agregar a la lista: "))
        else:
            numLista = input("Dame un string para agregar a la lista: ")
        guardaLista.append(numLista)
        i+=1
        if i>3:
            op=input('Desea agregar otro dato? (si|no): ')
            op=op.lower()
            if (op=='si'):
                continue
            else:
                break
    return guardaLista

def generaListaGral():
    guardaLista = []
    while True:
        numLista = input("Dame un dato para agregar a la lista: ")
        guardaLista.append(numLista)
        op=input('Desea agregar otro dato? (si|no): ')
        op=op.lower()
        if (op=='si'):
            continue
        else:
            break
    return guardaLista

#F-1
def mayores_N():
    nuevaLista = generaLista('int')
    totalElementos = len(nuevaLista)
    num = int(input("Agregar el número a comparar:"))
    cta=0
    for x in range(0,len(nuevaLista)):
        if num > nuevaLista[x]:
            cta+=1
            print(f"{num} >",nuevaLista[x])
    print(f"total de elementos mayores a {num} es: {cta}")
            

#F-2
def _N_letras():
    nuevaLista = generaLista('str')
    num = int(input("Agregar el número a comparar con los stings:"))
    for x in range(0,len(nuevaLista)):
        if num > len(nuevaLista[x]):
            print(f"La palabra {nuevaLista[x]} con {len(nuevaLista[x])} caracteres es mayor a {num} caracteres")
        else:
            print(f"La palabra {nuevaLista[x]} con {len(nuevaLista[x])} caracteres es menor a {num} caracteres")
#F-3
def empiezan_Con():
    nuevaLista = generaLista('str')
    buscaStr = input("Agrega la letra a comparar con los stings:")
    for x in range(0,len(nuevaLista)):
        if nuevaLista[x][0:1].lower() == buscaStr.lower():
            print(f"Esta(s) palabra(s) empiezan con la letra {buscaStr}: {nuevaLista[x]}")

#F-4
def duplica():
    nuevaLista = generaLista('str')
    for x in range(0,len(nuevaLista)):
        print(f'La palabra [{nuevaLista[x]}] a su doble es:',2* nuevaLista[x])
        
#F-5
def locura():
    dateStr = input("Favor de darme un string: ")
    dateStr = dateStr.lower()
    dateStrNew = dateStr.replace('e','3')
    dateStrNew = dateStrNew.replace('o','h')
    dateStrNew = dateStrNew.replace('a','4')
    print(f"El resultado del string [{dateStr}] queda como: ", dateStrNew)
    

#F-6
def vocales_Mayusculas():
    dateStr = input("Favor de darme un string: ")
    dateStr = dateStr.lower()
    fraseFinal = ""
    for caracter in dateStr:
        if caracter in ('a', 'e', 'i', 'o', 'u'):
            caracter = caracter.upper()  #Aplicamos la mayuscula
            fraseFinal += caracter
        else:
            fraseFinal += caracter
    print(f"El string final sustituyendo vocales de minisculas a mayusculas es: {fraseFinal}")

#F-7
def espaciado():
    dateStr = input("Favor de darme un string: ")
    dateStr = dateStr.lower()
    for caracter in dateStr:
        print(caracter, end=' ')
    print('\n')

#F-8
def invierte():
    nuevaLista = generaLista('str')
    listaInvertida = []
    for x in range(0,len(nuevaLista)):
        listaInvertida.append(nuevaLista[x])
    listaInvertida.reverse()
    print("la lista invertida es la siguiente: ", listaInvertida)
 
#F-9
def combina_listas():
    nuevaLista = generaLista('str')
    print("#### Gracias, ahora favor de agregar una segunda lista #### ")
    segundaLista = generaSegundaLista('str')
    guardaListas = nuevaLista + segundaLista
    print(f"La concatenación de las 2 listas es: {guardaListas}")

#F-10
def tirada():
    suma=0
    dameNumero = int(input("Dame un número: "))
    for i in range(0,dameNumero):
        dado=randint(1,7)
        suma +=dado
    print(f"La suma total es de: {suma}, de un total de {dameNumero} tirados con el dado")

#F-11
def revuelvePalabra():
    print("En construcción, no me quedo claro este requerimiento ")    

#F-12
def solo_x():
    guardaNuevoStrings = []
    nuevaLista = generaLista('str')
    num = int(input("Ingresa un múmero en donde quieras cortar cada uno de los strings: "))
    for i in range(0, len(nuevaLista)):
        guardaNuevoStrings.append(nuevaLista[i][:num])
    print(f"El nuevo string recortado es: {guardaNuevoStrings}")

#F-13
def coincidencias():
    print("Pendiente...Ya no me dio tiempo, pero si la voy a hacer")

#F-14
def los_tres_menores():
    nuevaLista = generaListaCondicion('int')
    ordenamos = sorted(nuevaLista)
    generaNuevaLista = []
    for i in range(0,3):
        generaNuevaLista.append(ordenamos[i])
    print(f"La lista final ordenada es: {generaNuevaLista}")
        
#F-15
def coinciden():
    nuevaLista = generaListaGral()
    print("#### Gracias, ahora favor de agregar una segunda lista #### ")
    segundaLista = generaListaGral()
    coincidencias = set(nuevaLista).intersection(segundaLista)
    print("Las coincidencias de las 2 listas son: ", coincidencias)

#F-16
def separa_guiones():
    cad = input("Ingresa un string: ")
    num = int(input("Ingresa un múmero para separar el string: "))
    car = input("Ingresa el caracter, Ejemplo - : ")
    cad = cad.replace(" ", "")
    agregamosCaracter = car.join(cad[i:i+num] for i in range(0, len(cad), num))
    print("El string final es: ", agregamosCaracter)

### Programa principal

itera = 0
while True:
    operadores()
    opcion = int(input("Eliga la funcion que dease utilizar: "))
    print("\n")
    if opcion==1:
        mayores_N()
    elif opcion==2:
        _N_letras()
    elif opcion==3:
        empiezan_Con()
    elif opcion==4:
        duplica()
    elif opcion==5:
        locura()
    elif opcion==6:
        vocales_Mayusculas()
    elif opcion==7:
        espaciado()
    elif opcion==8:
        invierte()
    elif opcion==9:
        combina_listas()
    elif opcion==10:
        tirada()
    elif opcion==11:
        revuelvePalabra()
    elif opcion==12:
        solo_x()
    elif opcion==13:
        coincidencias()
    elif opcion==14:
        los_tres_menores()
    elif opcion==15:
        coinciden()
    elif opcion==16:
        separa_guiones()
    elif opcion==17:
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
print(f"##### Total de operaciones {itera} #######")
print("###########################################")

