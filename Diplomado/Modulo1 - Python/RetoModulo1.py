"""
Problem: Fenómeno de deserción laboral que tanto afecta en la actualidad a las empresas y organizaciones. 
Source of information: Hackathon HackerEarth 2020 - Employees.csv
Description: Programa el cual obtiene la edad promedio de los empleados durante en 
las fechas en las que se recabo la información y si la mayoría son hombres o mujeres.
Question: ¿Cuál es la edad promedio de los empleados?
           ¿Hay más hombres o mujeres en la muestra?
Date: September 12, 2022
Author: Omar K Sánchez Miranda
"""

#Abrimos el archivo como lectura
file_hander = open('Employees.csv', 'r')

#Omitimos la primera fila
next(file_hander)

#Inicializamos conteo
m = 0
f = 0
cuenta = 0
suma = 0

#Iteramos el archivo
for line in file_hander:
    separaDatos = line.split(",")
    genero = separaDatos[1].lower();
    anio = separaDatos[2]
    
    if genero!="":
        if genero == "m":
            m = m+1
        elif genero == "f":
            f = f+1

    if anio!="":
        cuenta += 1
        suma = suma + int(anio)

print ("\n")
print ("##############################################################################")
print ("##### Programa el cual obtiene la edad promedio de los empleados durante ####")
print ("##### las fechas en las que se recabo la información y si la mayoría son ####")
print ("##### hombres o mujeres.                                                 #### ")
print ("##############################################################################")
print ("\n")

#print (f"Promedio de Edad: {suma/cuenta:.2f}")
print (f"Edad promedio de los empleados: {round(suma/cuenta)}")
print ("\n")
print("Total del género masculino:", m, "Total del género femenino:", f)
print ("\n")
print ("################################################")
if m>f:
    print("\t"+"Hay mas hombres que mujeres")
else:
    print("\t"+"Hay mas mujeres que hombres")
print ("################################################")

#Cerramos el archivo
file_hander.close()
