#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Programa donde se registran alumnos, la alta de los campos son dinámicos y de eso depende
de que información requieres guardar del alumno
Archivos: registroAlumnos.py y alumnos.csv
@author: oksm
Date: 15-06/2022
"""
import csv
import pathlib
import os

def menu():
    print("""
        REGISTRO DE ALUMNOS
###############################################

Nota: Puedes generar tu propio encabezado y
      dar de alta al alumno(a)
      
      Puedes agragar los siguientes campos:
          Nombre, Matricula, Correo, Teléfono y Carrera

    """)

def generaArchivo(nombre, type):
    return open(nombre, type)

def armandoHeader(nombreArchivo):
    header=[]
    cta=0
    f = open(nombreArchivo, 'w')
    while True:
        cta+=1
        cabecera = input(f"Escribe el encabezado del CSV (Posición {cta}): ")
        header.append(cabecera)
        op=input('Desea agregar otro encabezdo? (si|no): ')
        op=op.lower()
        if (op=='si'):
            continue
        else:
            escribeCsv = csv.writer(f)
            escribeCsv.writerow(header)
            return header
    f.close()

def altaALumnos(header, nombreArchivo):
    f = open(nombreArchivo, 'a')
    guardaAlumno = []
    while True:
        for x in range(len(header)):
            alumnoDato = input(f"Escribe el {header[x]}: ")
            guardaAlumno.append(alumnoDato)
        escribeCsv = csv.writer(f)
        escribeCsv.writerow(guardaAlumno)
        guardaAlumno = []
        op=input('Desea agregar otro alumno? (si|no): ')
        op=op.lower()
        if (op=='si'):
            continue
        else:
            break
    f.close()    

def readAndShowCsv(nombreArchivo):
    archivo = open(nombreArchivo)
    reader = csv.reader(archivo, delimiter=",")
    for row in reader:
        print(row)
        
#Programa principal
nombreArchivo = "alumnos.csv"

archivoTmp = pathlib.Path(nombreArchivo)
if archivoTmp.exists():
    os.remove(nombreArchivo)

menu()
headerFinal = armandoHeader(nombreArchivo)
altaALumnos(headerFinal, nombreArchivo)
readAndShowCsv(nombreArchivo)
print("Gracias por utilizar este programa, Saludos")

