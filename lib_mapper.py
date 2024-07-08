def mapper(lista, funcion):
    """recorre una lista y realiza una funcion a cada elemento

    Args:
        lista (list): lista de diccionarios de bicicletas
        funcion (funcion): funcion a realizar en cada elemento
    """
    for  bicicleta in lista:
        funcion(bicicleta)