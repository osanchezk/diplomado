numero=int(input("num: "))
#Asc
#for i in range(0, numero+1,1):
#    for j in range(1,i+1):
#        print(j, end=' ') ### Pinta de manera horizontal
#    print()
#print()
#Desc
#for i in range(numero, 0,-1):
#    for j in range(1,i+1):
#        print(j, end=' ') ### Pinta de manera horizontal
#    print()
#
#print()

"""
Con while y for
"""
col=0

#while col<numero:
#    fil=col+1 #Filas
#    #print(fil)
#    for j in range(1,fil+1):
#        print(j, end=' ') #Columnas
#    col=col+1
#    print()

while col<numero:
    fil=col+1 #Filas
    while col<numero:
        print(fil,numero)
        #for j in range(1,fil+1):
        #    print(j, end=' ') #Columnas
        #col=col+1
        #print()


    