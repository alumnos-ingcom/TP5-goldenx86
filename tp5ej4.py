################
# Matías Locatti - @goldenx86
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def perfecto():
    """Identifica si un número es perfecto"""
    numero = int(input("Ingrese un número entero positivo: "))
    suma = 0
    for i in range(1, numero):
        if (numero % i == 0):
            suma = suma + i
    if numero == suma:
        print("Es perfecto.")
    else:
        print("No es perfecto.")


if __name__ == "__main__":
    perfecto()