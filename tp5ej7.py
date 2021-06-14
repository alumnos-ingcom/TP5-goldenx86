################
# Matías Locatti - @goldenx86
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def distancia(num1,num2):
    """Entrega la distancia entre dos nmúeros"""

    resultado = num1 - num2
    if resultado < 0:
        resultado = -resultado
    return resultado


def prueba():
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))
    print(distancia(numero1,numero2))


if __name__ == "__main__":
    prueba()