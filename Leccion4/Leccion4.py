# Eva González Correa

# Importamos los módulos necesarios
import pdb
#Importamos la funcion reduce. Obtiene un solo resultado de una lista
from functools import reduce

"""
    Calculo valores maximos de una lista
"""

# -----> FUNCION MAXIMO

# ... Método compresion de listas
def max_compresion(lista):
    # Añadimos el depurador
    #pdb.set_trace()
    """
    Calculo de los valores maximos de sublistas con compresion de listas y
    funcion max.
    Contador:
        i: cada una de las sublistas
    """
    maximos=[max(i) for i in lista]
    return maximos


# -----> MEDIANTE BUCLES FOR


def maximo_dos_valores(n,m):
    """
    Devuelve el maximo entre dos valores.
    """
    if n>=m:
        return n
    else:
        return m


def maximo_compresion(maximo_dos_valores,lista):
    """
    Calcula el maximo de una lista de listas utilizando conpresion de listas.
    Inputs:
        maximo_dos_valores: funcion ya definida que calcula el maximo de n y m
        lista: lista que contiene otra lista sobre la que calcular el maximo
    Outputs:
        maximos: Lista con valores maximo de cada sublista
    Contador:
        i: cada una de las sublistas
    """
    maximos = [reduce(maximo_dos_valores,i) for i in lista]
    return maximos