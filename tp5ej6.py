################
# Matías Locatti - @goldenx86
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def parentesis_balanceados():
    """Comprobar salud de cadena de corchetes"""
    cadena = input("Ingrese paréntesis: ")
    numero = 0
    for c in cadena:
        if c == '[':
            numero += 1
        elif c == ']':
            numero -= 1
        if numero < 0:
            print("NO OK")
            return
    if numero != 0:
        print("NO OK")
    else:
        print("OK")


if __name__ == "__main__":
    parentesis_balanceados()
