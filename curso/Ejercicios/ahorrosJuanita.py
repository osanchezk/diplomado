"""
Acumulador con contador los ahorros de Juanita
"""
suma=0
dias=1
while dias<=7:
    #print (f"Cuando dinero ganaste el día {dias}")
    dinero = float(input(f"Ahorro del día {dias}:"))
    suma = suma + dinero
    dias = dias + 1
print("############################################")    
print(f"EL cochinito tiene una cantidad de: {suma}")
print("############################################")