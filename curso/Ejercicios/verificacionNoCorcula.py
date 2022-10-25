"""
La secretaría de Vialidad y Transporte te ha solicitado que hagas una aplicación que presente un menú para que todos los 
usuarios  de  automóviles  puedan  consultar  tanto  su  mes  de  verificación,  como  si  su  automóvil  puede  o  no  circular  en 
CDMX. El programa deberá presentar el siguiente menú.

1-2 Enero - Febrero
3-4 Marzo - Abril
5-6 Mayo - Junio
7-8 Junio - Agosto - Septiembre
9-0 Octubre - Noviembre


==== “NO CIRCULA” ====
1-2 jueves
3-4 miércoles
5-6 lunes
7-8 martes
9-0 viernes

"""
def muestraMensaje(num, menu):
    print ("################################################")
    if menu==1:
        if num==1 or num==2:
            print ("\n\tMes de verificación: Enero - Febrero\n")
        elif num==3 or num==4:
            print ("\n\tMes de verificación: Marzo - Abril\n")
        elif num==5 or num==6:
            print ("\n\tMes de verificación: Mayo - Junio\n")
        elif num==7 or num==8:
            print ("\n\tMes de verificación: Junio - Agosto - Septiembre\n")
        elif num==9 or num==0:
            print ("\n\tOctubre - Noviembre\n")
        else:
            print("\n\tNo existe!\n")
    if menu==2:
        if num==1 or num==2:
            print ("\n\tNo circulas los: Jueves\n")        
        elif num==3 or num==4:
            print ("\n\tNo circulas los: Miercoles\n")        
        elif num==5 or num==6:
            print ("\n\tNo circulas los: Lunes\n")                
        elif num==7 or num==8:
            print ("\n\tNo circulas los: Martes\n")                
        elif num==9 or num==0:
            print ("\n\tNo circulas los: Viernes\n")
        else:
            print("\n\tNo existe!")
    print ("################################################")

menu=1
while menu!=3:
    print("""
                  MENU
        ________________________
        
        1. Mes de verificación
        2. Programa Hoy no circula
        3. Salir
        
    """)
    menu=int(input("Opción:"))
    placa=input("Escribe el número de placa (Ej: XSE-456): ")

    dameNumero = int(placa[-1])

    if menu==1:
        muestraMensaje(dameNumero, menu)
    elif menu==2:
        muestraMensaje(dameNumero, menu)
    elif menu==3:
        print("Gracias, saludos!")
    else:
        print("Introduce un numero entre 1 y 3")