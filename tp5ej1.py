################
# Matías Locatti - @goldenx86
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def parimpar():
    """Identificar pares como True e impares como False"""
    numero = int(input("Ingrese un número entero: "))
    print(numero // 2 * 2 == numero)


if __name__ == "__main__":
    parimpar()