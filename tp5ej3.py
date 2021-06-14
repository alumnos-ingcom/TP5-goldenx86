################
# Matías Locatti - @goldenx86
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def tribonacci(numero):
    """Imprimir serie de Tribonacci"""
    numero = int(input("Ingrese un número entero positivo, mayor a 3 si desea varios resultados: "))
    if (numero < 1):
        return
    primero = 1
    segundo = 1
    tercero = 1

    print(primero, " ", end="")
    if (numero > 1):
        print(segundo, " ", end="")
    if (numero > 2):
        print(segundo, " ", end="")

    for i in range(3, numero):
        actual = primero + segundo + tercero
        primero = segundo
        segundo = tercero
        tercero = actual

        print(actual, " ", end="")


if __name__ == "__main__":
    numero = 0
    tribonacci(numero)