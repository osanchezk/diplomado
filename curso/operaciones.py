"""
Programa que manipula los operadores DIV // Y MOD %
OKSM - X
INICIO
    1.- Recibo 2 numeros
    2.- Realizo las operaciones con DIV Y MOD
    3.- Imprimo resultados
FIN
"""

print ("#################################################################")
print ("###Este programa realiza divisiones enteras y obtiene residuos###")
print ("#################################################################")
num1 = int(input("Dame el primer numero: "))
num2 = int(input("Dame el segundo numero: "))
divisionEntera = num1 // num2
residuo = num1%num2
print (f"La division entera es {divisionEntera} y el residuo es {residuo}")
