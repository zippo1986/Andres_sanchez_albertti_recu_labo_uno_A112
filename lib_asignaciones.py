from random import randint
def asignar_tiempo(i, max=120, min=100):
    """asigna un valor random

    Args:
        i (dict): diccionario de la lista
        max (int): numero maximo
        min (int): numero minimo
    """
    i["tiempo"] = randint(min, max)