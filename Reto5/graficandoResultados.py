#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
En base de los resultados obtenidos, se realiza una gráfica para ver que sector se visita mas...
Este es un plus que tenía ganas de hacer, Saludos
Created on Wed Jun 15 17:29:31 2022
@author: oksm
"""
import matplotlib.pyplot as plt

sectorName = []
sectorTotal = []
with open("concentrado.txt") as f:
    for row in f:
        sectorName.append(row.split("|")[0])
        sectorTotal.append(row.split("|")[1])

sectorTotalInt = []
sectorNameStr = []

for j in range (len(sectorName)):
    sectorNameStr.append(sectorName[j].upper())

for i in range (len(sectorTotal)):
    sectorTotalInt.append(int(sectorTotal[i]))

font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 6}
plt.rc('font', **font)
                    
plt.bar(sectorNameStr, sectorTotalInt)
 
plt.xticks(rotation=70)
plt.title("Análisis de log de visitas de un sitio web con fecha: 09/Dec/2021") 
plt.ylabel('Total de visitas')
plt.xlabel('Sectores')
  
plt.show()
