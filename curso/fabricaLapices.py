"""
Fabrica de lápices no importado la cantidad de lapices 

"""

print("""
   ### Acomodar lápices en cajas de: ###
   ### 80 ###
   ### 40 ###
   ### 20 ###

""")


print ("################################################################")
print ("##### Fabrica de lápices empacados en cajas de 80, 40 y 20 #####")
print ("################################################################")
totalLapices = int(input("Total de lapices a acomodar:"))

caja80 = totalLapices//80
caja40 = totalLapices//50
caja20 = totalLapices//20

resid80 = totalLapices%80
resid40 = totalLapices%40
resid20 = totalLapices%20

print(f"Cajas de 80 lápices se requieren {caja80} cajas y {resid80} lápices")
print(f"Cajas de 40 lápices se requieren {caja40} cajas y {resid40} lápices")
print(f"Cajas de 20 lápices se requieren {caja20} cajas y {resid20} lápices")

