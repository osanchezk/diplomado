#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Este programa analiza un archivo .log de las visitas de un sitio web de mi empresa;
se obtienen las visitas por sector (energy, oilangas, mining, etc...)
Se toma una muestra de 20,000 Registros de 300,000 de un solo dia
Se genera un archivo llamado concentradoDatos.txt en donde extraer la información seleccionada
Se genera otro archivo con el concentrado con el total del sector con sus totales 
Archivos: access.log.0 (Archivo texto base), concentradoDatos.txt (Insertamos datos para analizar),
concentrado.txt (Concentrado de todos los sectores)
@author: Omar K Sánchez Miranda
Date: 14-06-2022
"""

import time
import os
import pathlib

path = "."
concentradoLista = "concentradoDatos.txt"
concentrado = "concentrado.txt"
sector = ['energy', 'oilandgas', 'mining', 'health', 'automotive', 'aerospace', 'infrastructure', 'tech', 'entrepreneurs', 'professional-services', 'finance', 'logistics', 'ecommerce', 'digital-transformation', 'agribusiness', 'talent', 'mobility', 'trade-and-investment', 'policyandeconomy']

#Limpiamos contenido de los archivos
concentradoLista1 = pathlib.Path(concentradoLista)
if concentradoLista1.exists ():
    os.remove(concentradoLista)

concentradoLista2 = pathlib.Path(concentrado)
if concentradoLista2.exists ():
    os.remove(concentrado)

#Definimos funciones
def separaLista(lineaText): #Traemos lo que nos interesa del string con un split doble
    try:
        getData = lineaText.split("\"GET /")[1].split("HTTP/1.1")[0]
        if getData:
            getData = getData.split("/")
            if getData != "":
                return (getData[0])
    except:
        return 0

def generaArchivo(nombre, type):
    return open(nombre, type)

def dameLaFecha(lineaText):
    getDate = lineaText.split("[")[1].split(":")[0]
    return getDate

def contamosYBuscamos(leerArchivo, sector, creaArchivo):
    cta=0
    archivoCos = open(leerArchivo)
    archivoCos = archivoCos.readlines()
    for linea in archivoCos:
        if sector in linea:
            cta+=1
    return cta

def formatDate(y):
    year = y[0].replace("/", "-")
    return year

with os.scandir(path) as filePath: #Podemos procesar varios archivos dentro de una carpeta
    for fileName in filePath: #Recorremos los archivos 
        nombreArchivo = fileName.name
        dateExtension = nombreArchivo.split(".")
        if dateExtension[1]=="log":
            cta = 0
            with open(nombreArchivo) as f:
                f = f.readlines()
                print("###########################################")
                print(" Nombre del archivo para anlizar  #####")
                print("     ", nombreArchivo, "      ")
                print("###########################################")
                for linea in f:
                    cta+=1
                    print(cta)
                    newData = separaLista(linea)
                    date = dameLaFecha(linea)
                    if newData in sector:
                        creaArchivo = generaArchivo(concentradoLista, type='a')
                        creaArchivo.write(date +","+newData+"\n")
                        print(date +","+newData+"\n")
                        creaArchivo.close()
                        time.sleep(0.02)

#Recuperamos datos y los concentramos, generamos archivo
creaArchivo = generaArchivo(concentrado, type="a")
for x in range (len(sector)):
    total = contamosYBuscamos(concentradoLista, sector[x], creaArchivo)    
    archivoConcentrado = open(concentrado, "a")
    archivoConcentrado.write(f"{sector[x]}|{total}\n")
    archivoConcentrado.close()    