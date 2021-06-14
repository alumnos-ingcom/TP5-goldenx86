################
# Matías Locatti - @goldenx86
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def busqueda(string,word):
    if word in string:
        return True
    else:
        return False


def prueba():
    texto = ("I am the bone of my sword. Steel is my body, and fire is my blood. I have created over a thousand blades. Unknown to Death. Nor known to Life. Have withstood pain to create many weapons. Yet, those hands will never hold anything. So as I pray, unlimited blade works.")
    palabra = input("Ingrese palabra a buscar: ")
    if busqueda(texto, palabra):
        print("Palabra encontrada")
    else:
        print("Palabra no encontrada")


if __name__ == "__main__":
    prueba()