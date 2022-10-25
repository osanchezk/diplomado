"""
Programa calculadora
"""

print("#############################")
print("### C A L C U L A D O R A ###")
print("#############################")

primerNumero = float(input("Dame el primer número: "))
segundoNumero = float(input("Dame un segundo número: "))

print(f"La suma de {primerNumero} + {segundoNumero} números es de: {primerNumero+segundoNumero:.2f}")
print(f"La resta de {primerNumero} - {segundoNumero} números es de: {primerNumero-segundoNumero:.2f}")
print(f"La multiplicacion de {primerNumero} * {segundoNumero} números es de: {primerNumero*segundoNumero:.2f}")
if primerNumero%segundoNumero == 0:
    print("El resultado de la división es cero, Error!")
else:
    print(f"La división de {primerNumero} / {segundoNumero} números es de: {primerNumero/segundoNumero:.2f}")