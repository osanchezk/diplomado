
from termcolor import colored

planetaGral = []

planeta1 = 'Alderaan,24,364,12500,temperate,1 standard,"grasslands, mountains",40,2000000000'
planeta2 = 'Yavin IV,24,4818,10200,"temperate, tropical",1 standard,"jungle, rainforests",8,1000'
planeta3 = 'Hoth,23,549,7200,frozen,1.1 standard,"tundra, ice caves, mountain ranges",100,NA'
planeta4 = 'Dagobah,23,341,8900,murky,N/A,"swamp, jungles",8,NA'

planetaGral.append(planeta1)
planetaGral.append(planeta2)
planetaGral.append(planeta3)
planetaGral.append(planeta4)

for i in planetaGral:
    #Separamos el texto por comas
    separaPlaneta = i.split(",")
    #print(separaPlaneta)

    #Convierte el texto en la segunda posición  a un entero
    separaPlaneta[1] = int(separaPlaneta[1])

    #print(separaPlaneta)

    #Convertir el texto en la tercera posición a un entero
    separaPlaneta[2] = int(separaPlaneta[2])

    #print(separaPlaneta)

    #Imprime por cada planeta: Nombre, periodo rotacional y periodo orbital
    print(f"Nombre: \033[1m",colored(separaPlaneta[0],"blue"),"\033[0m. Periodo Rotaciónal: \033[1m",separaPlaneta[1],"\033[0m. Periodo Orbital: \033[1m",separaPlaneta[2],"\033[0m")
    
    
    