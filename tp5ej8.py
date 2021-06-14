################
# Matías Locatti - @goldenx86
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def enc_cesar():
    """Codificación Cesar"""
    cadena = input("Ingrese un texto a codificar: ")
    valor = int(input("Ingrese el desplazamiento a usar: "))
    resultado = ""
    for c in cadena:
        if c.isupper():
            c_indice = ord(c) - ord("A")
            c_corrido = (c_indice + valor) % 26 + ord("A")
            c_nuevo = chr(c_corrido)
            resultado += c_nuevo
        elif c.islower():
            c_indice = ord(c) - ord("a")
            c_corrido = (c_indice + valor) % 26 + ord("a")
            c_nuevo = chr(c_corrido)
            resultado += c_nuevo
        elif c.isdigit():
            c_nuevo = (int(c) + valor) % 10
            resultado += str(c_nuevo)
        else:
            resultado += c
    print(resultado)

def dec_cesar():
    """Decodificación Cesar"""
    cadena = input("Ingrese un texto a decodificar: ")
    valor = int(input("Ingrese el desplazamiento a usar: "))
    resultado = ""
    for c in cadena:
        if c.isupper():
            c_indice = ord(c) - ord("A")
            c_pos_original = (c_indice - valor) % 26 + ord("A")
            c_original = chr(c_pos_original)
            resultado += c_original
        elif c.islower():
            c_indice = ord(c) - ord("a")
            c_pos_original = (c_indice - valor) % 26 + ord("a")
            c_original = chr(c_pos_original)
            resultado += str(c_original)
        else:
            resultado += c
    print(resultado)


if __name__ == "__main__":
    enc_cesar()
    dec_cesar()