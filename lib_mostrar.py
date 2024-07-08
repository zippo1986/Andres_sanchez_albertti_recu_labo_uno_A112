def mostrar_mensaje(mensaje):
    print(mensaje)
    
def mostrar_bicicletas(lista):
    
    print("ID_BIKE   NOMBRE                     TIPO         TIEMPO ")
    for pelicula in lista:
        mostrar_bicicleta(pelicula)        

def mostrar_bicicleta(pelicula) -> None:
    """Muestra las peliculas por aatributo

    Args:
        pelicula (dict): diccionario de pelicula
    """
    print(
        f"{pelicula['id_bike']:3}| "
        f"{pelicula['nombre']:29}| "
        f"{pelicula['tipo']:15}| "
        f"{pelicula['tiempo']:6}|"
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