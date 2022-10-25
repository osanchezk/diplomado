# Ejemplo de un menu
# las opciones se proponen por caracteres
# propuesta: edelros@espol.edu.ec

# menu
opcion = '0'
while not(opcion=='6'):
    print(' 1. menu opcion 01')
    print(' 2. menu opcion 02')
    print(' 3. menu opcion 03')
    print(' 4. menu opcion 04')
    print(' 5. menu opcion 05')
    print(' 6. Salir')

    opcion=input('  --- ¿Cuál opcion?: ')
    
    if (opcion=='1'):
        print('\n **** menu opcion 01 ****\n')
        
    elif (opcion=='2'):
        print('\n **** menu opcion 02 ****\n')
        
    elif (opcion=='3'):
        print('\n **** menu opcion 03 ****\n')
        
    elif (opcion=='4'):
        print('\n **** menu opcion 04 ****\n')
        
    elif (opcion=='5'):
        print('\n **** menu opcion 05 ****\n')
                
    elif (opcion=='6'):
        print(' **** Saliendo del menu  ****')
        print(' **** Ejemplo de un menu ****')
    else:
        print('No existe la opcion')