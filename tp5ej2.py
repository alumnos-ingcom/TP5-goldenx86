################
# Matías Locatti - @goldenx86
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def fibonacci(numero):
    """Imprimir serie de Fibonacci"""
    numero = int(input("Ingrese un número entero positivo, mayor a 2 si desea varios resultados: "))
    primero, segundo = 0,1
    for i in range(numero):
        print(primero, end=" ")
        primero, segundo = segundo, primero + segundo


if __name__ == "__main__":
    numero = 0
    fibonacci(numero)