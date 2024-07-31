def normalizar_datos(lista:list):
    """_summary_
    # Valida que la lista de héroes no esté vacía
    # Recorre la lista de héroes
    # Recorre las keys de cada héroe
    # Valida que la key represente un dato numérico y que no sea None
    # Convierte el tipo de dato y marca como modificado
    Args:
        lista (_type_): _description_
    """
    
    if not lista:
        print("Error: Lista de héroes vacía")
        return
    modificado = False
    tipos_dato = {"PRECIO": float }
    for insumo in lista:
        for clave in insumo:
            if clave in tipos_dato and insumo[clave] is not None:
                
                if type(insumo[clave]) != tipos_dato[clave]:
                    
                    insumo[clave] = tipos_dato[clave](insumo[clave])
                    modificado = True
                    
    if modificado:
        print("Datos normalizados")
