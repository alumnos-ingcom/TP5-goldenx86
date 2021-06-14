################
# Matías Locatti - @goldenx86
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def enc_cesar(string,key):
    """Codificación Cesar"""

    resultado = ""
    for c in string:
        if c.isupper():
            c_indice = ord(c) - ord("A")
            c_corrido = (c_indice + key) % 26 + ord("A")
            c_nuevo = chr(c_corrido)
            resultado += c_nuevo
        elif c.islower():
            c_indice = ord(c) - ord("a")
            c_corrido = (c_indice + key) % 26 + ord("a")
            c_nuevo = chr(c_corrido)
            resultado += c_nuevo
        elif c.isdigit():
            c_nuevo = (int(c) + key) % 10
            resultado += str(c_nuevo)
        else:
            resultado += c
    return resultado

def dec_cesar(string,key):
    """Decodificación Cesar"""

    resultado = ""
    for c in string:
        if c.isupper():
            c_indice = ord(c) - ord("A")
            c_pos_original = (c_indice - key) % 26 + ord("A")
            c_original = chr(c_pos_original)
            resultado += c_original
        elif c.islower():
            c_indice = ord(c) - ord("a")
            c_pos_original = (c_indice - key) % 26 + ord("a")
            c_original = chr(c_pos_original)
            resultado += str(c_original)
        else:
            resultado += c
    return resultado


def prueba():
    cadena = input("Ingrese un texto a codificar: ")
    valor = int(input("Ingrese el desplazamiento a usar: "))
    print(enc_cesar(cadena,valor))

    cadena = input("Ingrese un texto a decodificar: ")
    valor = int(input("Ingrese el desplazamiento a usar: "))
    print(dec_cesar(cadena,valor))


if __name__ == "__main__":
    prueba()