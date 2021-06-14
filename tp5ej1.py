################
# Matías Locatti - @goldenx86
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def parimpar(numero):
    """Identificar pares como True e impares como False"""
    return numero // 2 * 2 == numero

def prueba():
    num = int(input("Ingrese un número entero: "))
    print(parimpar(num))

if __name__ == "__main__":
    prueba()