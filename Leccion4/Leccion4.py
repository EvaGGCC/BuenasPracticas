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

# ... Metodo convencional
def maximo_convencional(lista):
    """
    Calculo del maximo de lista de listas mediante bucles convencionales.
    No se puede trasladar como tal a compresion de listas, uno de los bucles
    no funciona mediante listas sino con variables
    Contador:
        i: cada una de las sublistas
        j: cada uno de las posiciones de la sublista
    """
    maximos=[]
    for i in lista:
        m=0
        for j in range(len(i)):
            if i[j] > m:
                m = i[j]
        maximos.append(m)
    return maximos