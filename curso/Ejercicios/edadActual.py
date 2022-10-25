"""
Programa para apreender if, y que identifica si una presona es mayor de edad
"""

print("Programa para saber si eres mayor de edad")
nombre= input("Dame tu nombre: ")
edad=int(input("Dame tu edad: "))
# Y aqui es donde planteo el if
if edad<=0:
    print(f"{nombre} creo que estás juando, no has nacido")
elif edad<=18:
    print("Creo que eres un niño")
elif edad<=30:
    print("Creo que eres un jovenazo")
elif edad<=65:
    print("Eres una persona muy productiva")
else edad>65:
    print("Tercera edad, enjoy the moment")
    