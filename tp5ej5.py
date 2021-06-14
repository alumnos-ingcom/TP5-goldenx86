################
# Matías Locatti - @goldenx86
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def mayusminus(string):
    """Invierte mayusculas y minusculas"""
    invertido = ""
    for i in range (len(string)):
        if string[i].isupper():
            invertido += string[i].lower()
        elif string[i].islower():
            invertido += string[i].upper()
        else:
            invertido += string[i]
    return invertido


def prueba():
    cadena = input("Ingrese un texto: ")
    print(mayusminus(cadena))


if __name__ == "__main__":
    prueba()