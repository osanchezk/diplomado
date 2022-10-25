"""
Aplicación para que el huésped pueda, desde su celular, hacer las reservaciones correspondientes
y sea consciente del saldo que le queda por disfrutar.

Entrada: Días de reservación, Amenidad que le interese
Proceso: Se utilia un lista para controlar las restas al saldo inicial,
Se muestran menús para que elijan la amenidad deseada, otros 
Salida: Saldo por cada requerimiento y saldo final
Autor: Omar K Sánchez
Fecha: 25/05/2022

"""
from random import randint

print("###########################################")
print("###    Hotel Hard Rock Nuevo Vallarta   ###")
print("###########################################")
print("###########################################")
print("### B I E N V E N I D O - Reservaciones ###")
print("###########################################")

### Inicio de Funciones ###

##Función menu
def menuBono():
    print("""
                  MENU
        ________________________
        
        1. Paseo en Kayak ............................. $ 200 Pesos
        2. Cena en la orilla de la playa .............. $ 450 Pesos
        3. Spa ........................................ $ 250 Pesos
        4. Juego en linea 
        5. Salir
    """)

def menuKayak():
    print("""
                  MENU
        ________________________
        
        1. Paseo en Kayak entre semana................. $ 200 Pesos
        2. Paseo en Kayak fin de semana................ $ 350 Pesos
        3. Salir
    """)

def menuCena():
    print("""
                  MENU
        ________________________
        
        1. Cena en la orilla de la playa entre semana.. $ 450 Pesos
        2. Cena en la orilla de la playa fin de semana. $ 650 Pesos
        3. Salir
    """)

##Funcion del juego
def numRandom():
    print("##############################################")            
    print("### Bienvenido al juego: Adivina el numero ###")
    print("##############################################")            
    intento=1
    while intento<10:
        print(f"Intento #{intento}")
        num=randint(1,10)
        dameNumero = int(input("Dame un número de 1 a 10 : "))
        if dameNumero==num:
            print("************************************************************")
            print(f"Bien, adivinaste en el intento {intento}!")
            print("Gana el derecho a participar en la noche de casino del hotel")
            print("************************************************************")
            
            break
        else:
            print("Mucha suerte, sigue intentando")        
            intento = intento + 1
            if intento==8:
                print("#########################################################")
                print("Se terminaron los 8 intentos, pero puedes seguir jugando!")
                print("#########################################################")                
                break
    
## Limpiamos pantalla
def clear():
        _ = system('clear')
        
### Fin de Funciones ###

nocheHospedaje = int(input("Noches que desea reservar: "))

if nocheHospedaje>0:    
    if nocheHospedaje<=2:
        print("Gracias por reservar");
    else:
        #Aplicamos el bono de $10,000 pesos
        saldo = list()
        saldo.append(10000)
        print("************************************************************")
        print("**** Felicidades, tienes un bono de $10,000 Pesos       ****")
        print("****      Eliga en que lo quiere ocupar                 ****")
        print("************************************************************")        
        opcion = '1'
        while not(opcion=='5'):
            menuBono()
            opcion=int(input("Opción:"))
            if opcion==1:
                #Paseo en Kayak
                while not(opcion=='3'):                
                    menuKayak()
                    opcion=int(input("Opción:"))
                    if opcion==1:    
                        kayak = 200
                        if saldo[0]>kayak:
                            print(f"su saldo actual es de: {saldo[0]}")                    
                            saldo[0] = saldo[0] - kayak
                            print(f"Usted adquirió el la Paseo en Kayak entre semana, su saldo es: {saldo[0]}")
                        else:
                            print(f"Disculpa, pero ya no tiene saldo para utilizar esta actividad: saldo {saldo[0]}")                        
                    elif opcion==2:
                        kayak = 350
                        if saldo[0]>kayak:
                            print(f"su saldo actual es de: {saldo[0]}")                    
                            saldo[0] = saldo[0] - kayak
                            print(f"Usted adquirió el la Paseo en Kayak fin de semana, su saldo es: {saldo[0]}")
                        else:
                            print(f"Disculpa, pero ya no tiene saldo para utilizar esta actividad: saldo {saldo[0]}")
                    elif opcion==3:
                        break
            elif opcion==2:
                #Cena en la orilla de la playa
                while not(opcion=='3'):                
                    menuCena()
                    opcion=int(input("Opción:"))
                    if opcion==1:    
                        cenaPlaya = 450
                        if saldo[0]>cenaPlaya:
                            print(f"su saldo actual es de: {saldo[0]}")                    
                            saldo[0] = saldo[0] - cenaPlaya
                            print(f"Usted adquirió la cena en la orilla entre semana, su saldo es: {saldo[0]}")
                        else:
                            print(f"Disculpa, pero ya no tiene saldo para utilizar esta actividad: saldo {saldo[0]}")
                    elif opcion==2:
                        cenaPlaya = 550
                        if saldo[0]>cenaPlaya:
                            print(f"su saldo actual es de: {saldo[0]}")                    
                            saldo[0] = saldo[0] - cenaPlaya
                            print(f"Usted adquirió la cena en la orilla fin de semana, su saldo es: {saldo[0]}")
                        else:
                            print(f"Disculpa, pero ya no tiene saldo para utilizar esta actividad: saldo {saldo[0]}")
                    elif opcion==3:
                        break                        
            elif opcion==3:
                #Spa
                spa = 350
                if saldo[0]>spa:
                    print(f"su saldo actual es de: {saldo[0]}")                    
                    saldo[0] = saldo[0] - spa
                    print(f"Usted adquirió el Spa, su saldo es: {saldo[0]}")
                else:
                    print(f"Disculpa, pero ya no tiene saldo para utilizar esta actividad: saldo {saldo[0]}")                    
            elif opcion==4:
                #Juego en linea
                numRandom()
            elif opcion==5:
                #Salir
                #Si no compra ninguna amenidad, se le regala el pin
                print("La Tienda de Regalos tiene un pin Hard Rock para que lo lleve como recuerdo de su estancia")
                print(f"El saldo actual es de: {saldo[0]}")
                break
            else:
                #Error
                print ("error")
else:
    print ("Las reservas tienen que ser mayores a 0")