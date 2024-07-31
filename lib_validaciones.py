
def obtener_set(lista_diccionarios, clave):
    valores_unicos = set()
    for diccionario in lista_diccionarios:
        if clave in diccionario:
            valores_unicos.add(diccionario[clave])
    return valores_unicos
def validar_entero(numero:str):
    """_summary_
    Valida que el numero pasado por str sea enttero

    Args:
        numero (str): recibe un numero en str

    Returns:
        _type_: retorna true o false
    """
    for i in numero:
        try:
            int(i)
            return True
        except ValueError:
            return False
def validar_tipo(lista,tipo):
    """_summary_
    valida el tipo ingresado por el usuario a partir de una lista

    Args:
        genero (str): el genero buscado por el usuario

    Returns:
        bool: retorna True si encuentra el genero en la lista
    """
    lista_tipos=obtener_set(lista,"tipo")
    for t in lista_tipos:
        if tipo ==t:
            return True
        
def normalizar_datos(lista_diccionarios):
    if lista_diccionarios is not None:
        for diccionario in lista_diccionarios:
            if diccionario.get("tipo") is not None:
                diccionario["tipo"] = diccionario["tipo"].lower()                      
    