"""
    Operaciones Suma, Resta, Multipliacion, Division
"""

def operadores():
    print("""
           OPERADORES VALIDOS
        ________________________
        
         Resta ............. -
         Suma .............. +
         Multiplicación .... *
         Division .......... /
    """)

def operacion(x,y,dat):
    if dat=="-":
        resultado = x-y
    elif dat=="+":
        resultado = x+y
    elif dat=="*":
        resultado = x*y
    elif dat=="/":
        resultado = x%y
    else:
        print("Este operador no esta identificado")
    return resultado

while True:
    operadores()
    #dat1 = float(input("Dame el primer número: "))
    #dat2 = float(input("Dame el segundo número: "))
    dat1 = int(input("Dame el primer número: "))
    dat2 = int(input("Dame el segundo número: "))    
    dat3 = input("Que operación desea utilizar: ")

    print(f"El resultado de la operacion de {dat1} {dat3} {dat2} =",operacion(dat1,dat2,dat3))
    
    op=input('Desea salir? (si|no): ')
    op=op.lower()
    if (op=='si'):
        break
    else:
        continue
 