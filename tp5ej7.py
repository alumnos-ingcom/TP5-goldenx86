################
# Matías Locatti - @goldenx86
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def distancia():
    """Entrega la distancia entre dos nmúeros"""
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))
    resultado = numero1 - numero2
    if resultado < 0:
        resultado = -resultado
    print(resultado)


if __name__ == "__main__":
    distancia()