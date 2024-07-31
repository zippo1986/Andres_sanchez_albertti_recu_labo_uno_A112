def calcular_minimo(lista, atributo):
    """Calcula los  maximos de determinado atributo dentro de una lista de diccionarios

    Args:
        lista (list):lista de heroes
        atributo (str): la clave del diccionario de la que se quiere sacar el maximo

    Returns:
        list: retorna una lista de diccionarios que contiene los heroes del maximo en determinado atributo
    """
    bandera = True
    numero_minimo = None
    bicicleta_ganador = []
    for i in lista:
        if  (bandera ==True)or(int(i[atributo]) <(numero_minimo)) :
            
            numero_minimo =int(i[atributo])
            bandera= False
    
    for i in lista:
        if int(i[atributo])== numero_minimo:
            bicicleta_ganador.append(i)
    return bicicleta_ganador


def sacar_promedio_tipo(lista_diccionarios):
    # Crear un conjunto de tipos únicos
    set_tipo = set(diccionario["tipo"] for diccionario in lista_diccionarios)
    lista_promedios = []
    
    for tipo in set_tipo:
        suma_tiempo = 0
        contador_tipo = 0
        for diccionario in lista_diccionarios:
            if diccionario["tipo"] == tipo:
                suma_tiempo += diccionario["tiempo"]
                contador_tipo += 1
        promedio = suma_tiempo / contador_tipo if contador_tipo > 0 else 0
        lista_promedios.append({"tipo": tipo, "promedio_tiempo": promedio})
    
    return lista_promedios
    
                     
    