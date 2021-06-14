################
# Matías Locatti - @goldenx86
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def perfecto(num):
    """Identifica si un número es perfecto"""
    suma = 0
    for i in range(1, num):
        if (num % i == 0):
            suma = suma + i
    if num == suma:
        return(True)
    else:
        return(False)


def prueba():
    numero = int(input("Ingrese un número entero positivo: "))
    print(perfecto(numero))


if __name__ == "__main__":
    prueba()