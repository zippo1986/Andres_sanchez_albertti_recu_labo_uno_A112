def mostrar_mensaje(mensaje):
    print(mensaje)
    
def mostrar_bicicletas(lista):
    
    print("ID_BIKE   NOMBRE                     TIPO         TIEMPO ")
    for pelicula in lista:
        mostrar_bicicleta(pelicula)        

def mostrar_bicicleta(bicicleta) -> None:
    """Muestra las peliculas por aatributo

    Args:
        pelicula (dict): diccionario de pelicula
    """
    print(
        f"{bicicleta['id_bike']:3}| "
        f"{bicicleta['nombre']:29}| "
        f"{bicicleta['tipo']:15}| "
        f"{bicicleta['tiempo']:6}|"
    )

def mostrar_nombre_tiempo(lista,clave_uno,clave_dos):
    """Muestra el nombre y e tiempo

    Args:
        lista (list): lista de bicis
        clave_uno (str): tipo de bicicleta
        clave_dos (str): tiempo
    """
    print("---------------------------------")
    print(f"{clave_uno}                  {clave_dos}")
    print("---------------------------------")
    
    for elemento in lista:
        print(f" {elemento[clave_uno]:15}   {elemento[clave_dos]}")    