################
# Matías Locatti - @goldenx86
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def lista(l1,l2):
    a = set(l1)
    b = set(l2)

    if a == b:
        return True
    else:
        return False


def prueba():
    lista1 = [9, 5, 1, 7, 5, 3]
    lista2 = [1, 5, 9, 3, 5, 7]
    if lista(lista1,lista2) == True:
        print("Las listas son iguales")
    else:
        print("Las listas son distintas")

if __name__ == "__main__":
    prueba()