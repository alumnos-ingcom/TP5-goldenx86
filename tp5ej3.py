################
# Matías Locatti - @goldenx86
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def tribonacci(num):
    """Imprimir serie de Tribonacci"""
    primero = 1
    segundo = 1
    tercero = 1

    for i in range(3, num):
        actual = primero + segundo + tercero
        primero = segundo
        segundo = tercero
        tercero = actual
    return(tercero)

def prueba():
    numero = int(input("Ingrese un número entero positivo, mayor a 3: "))
    print(tribonacci(numero))

if __name__ == "__main__":
    prueba()