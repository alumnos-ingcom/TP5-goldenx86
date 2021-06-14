################
# Matías Locatti - @goldenx86
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def fibonacci(num):
    """Imprimir n valor de serie de Fibonacci"""
    primero, segundo = 0,1
    for i in range(num):
        primero, segundo = segundo, primero + segundo
    return segundo


def prueba():
    numero = int(input("Ingrese un número entero positivo, mayor a 2: "))
    print(fibonacci(numero))


if __name__ == "__main__":
    prueba()