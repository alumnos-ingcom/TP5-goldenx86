################
# Matías Locatti - @goldenx86
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def balanceado(string):
    """Comprobar salud de cadena de corchetes"""

    numero = 0
    for c in string:
        if c == '[':
            numero += 1
        elif c == ']':
            numero -= 1
        if numero < 0:
            return False
    if numero != 0:
        return False
    else:
        return True


def prueba():
    cadena = input("Ingrese corchetes: ")
    if balanceado(cadena) == True:
        print("OK")
    else:
        print("NO OK")


if __name__ == "__main__":
    prueba()
