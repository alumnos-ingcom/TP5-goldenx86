################
# Matías Locatti - @goldenx86
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def promedio_movil(lista, suavizado):
    promedios = []
    for indice in range(len(lista) - suavizado + 1):
        promedio = 0
        for sub_indice in range(suavizado):
            promedio += lista[indice + sub_indice]
        promedio /= suavizado
        promedios.append(promedio)
    return promedios


def prueba():
    assert(promedio_movil([3, 3, 3], 2) == [3, 3])
    assert(promedio_movil([3, 3, 3], 3) == [3])
    assert(promedio_movil([3, 3, 6], 3) == [4])


if __name__ == "__main__":
    prueba()