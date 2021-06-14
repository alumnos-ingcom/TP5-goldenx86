################
# Matías Locatti - @goldenx86
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def binario(num):
    """Convierte decimal a binario"""
    cadena = []
    while num:
        cadena.append(num % 2)
        num >>= 1
    return cadena[::-1]


def decimal(num):
    """Convierte binario a decimal"""
    dec = 0
    for i in range(len(num)):
        dec += int(num[i]) * 2**abs(i - (len(num) - 1))
    return dec


def prueba():
    numero = int(input("Ingerse un número entero: "))
    print(binario(numero))

    numero = input("Ingerse un número binario: ")
    print(decimal(numero))


if __name__ == "__main__":
    prueba()