################
# Matías Locatti - @goldenx86
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def capicua(num):
    return str(num) == str(num[::-1])


def prueba():
    numero = input("Ingrese primer número: ")
    if (capicua(numero)):
        print("Es capicúa")
    else:
        print("No es capicúa")


if __name__ == "__main__":
    prueba()