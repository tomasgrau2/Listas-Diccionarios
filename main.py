def buscar_repetidos(lista):
    resultado = {}
    for elem in lista:
        resultado[elem] = lista.count(elem)

    return resultado