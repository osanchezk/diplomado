"""
Programa que reciba la calificación del examen y la del proyecto
"""

print("################################")
print("###Status de una calificación###")
print("################################")

calificacionExamen = float(input("Calificación del examen obtenida: "))
calificacionProyecto = float(input("Calificación del proyecto obtenida: "))

calificacionFinal = (calificacionExamen+calificacionProyecto)/2

if calificacionFinal>=0 and calificacionFinal<=100:
    if calificacionFinal >=80:
        print("Felicidades, estas APROBADO")
    elif calificacionFinal>=70 or calificacionFinal>50:
        print("Ups!, tu calificación esta CONDICIONADA")
    else:
        print("Tienes que ponerte las pilas y ponerte a estudiar")
else:
    print("El promedio de calificación debe de estar en rango de 0 y 100")