from lib_validaciones import *
from lib_ordenamiento import *
from lib_archivos import *
from lib_mostrar import *
from lib_asignaciones import *
from lib_mapper import *
from lib_calculos import *
#from funciones_secundarias import *
from lib_filtrado import *
#from lib_ordenamiento import *
import sys
def main ():
    
    
    bandera_carga = False
    bandera_ordenamiento = False
    bandera_tiempo=False
    
    lista_bicicletas= []
    lista_ganadores =[]
    
    confirmacion = "s"
    while confirmacion == "s":
            mostrar_mensaje("""Menu de opciones
                        1)cargar archivo csv
                        2)imprimir lista
                        3) Asignar tiempo
                        4)informar ganador
                        5)filtrar por tipo
                        6)informar promedio por tipo
                        7)Mostrar_posiciones
                        8) guardar posiciones
                        9)Exit""")
            
            opcion = input("Ingrese opcion")
            while not validar_entero(opcion):
                opcion= input("Ingrese opcion")
            match (opcion):
                case "1":
                    lista_bicicletas= archivo_a_lista("bicicletas.csv")
                    
                    bandera_carga = True
                
                case "2":
                    if not bandera_carga:
                        mostrar_mensaje("No se puede mostrar la lista sin cargarla primero")
                    else:
                        mostrar_bicicletas(lista_bicicletas)
                
                case "3":
                    if not bandera_carga:
                        mostrar_mensaje("No se puede asignar ratings  sin cargar la lista primero")
                    else:
                        
                        mapper(lista_bicicletas,asignar_tiempo)
                        bandera_tiempo=True
                        mostrar_bicicletas(lista_bicicletas)
                case "4":
                    if not bandera_tiempo:
                        mostrar_mensaje("No se puede mostrar al ganador sin  asignar tiempos primero")
                    else:
                        calcular_minimo(lista_bicicletas,"tiempo")
                        mostrar_nombre_tiempo(lista_ganadores,"nombre","tiempo")
                case "5":
                    if not bandera_carga:
                        mostrar_mensaje("No sse puede filtrar sin cargar el archivo")
                    else:
                        tipo_buscado = input("ingrese tipo buscado")
                        while not validar_tipo(lista_bicicletas,tipo_buscado):
                            tipo_buscado = input("Ingrese tipo")
                        lista_filtrada_tipo = filtrar_datos(lista_bicicletas,tipo_buscado,"tipo")
                        guardar_csv(lista_filtrada_tipo,f"{tipo_buscado}.csv")
                    
                
                case "6":
                    pass
              
                case "7":
                    if not bandera_tiempo:
                        mostrar_mensaje("No se puede realizar la operacion sin cargar los ratings")
                    else:     
                        ordenar_dos_criterios(lista_bicicletas,"tipo","tiempo")
                        mostrar_bicicletas(lista_bicicletas)
                        bandera_ordenamiento = True
                
                
                case "8":
                    if not bandera_carga:
                        mostrar_mensaje("No se puede guardar este archivo sin cargar el primero")
                    elif not bandera_ordenamiento:
                        mostrar_mensaje("No se puede guardar sin ordenar")
                    else:
                        guardar_json(lista_bicicletas,"posiciones")
                
                case "9":
                    sys.exit()
                    