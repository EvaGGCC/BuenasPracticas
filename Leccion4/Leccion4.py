# Eva González Correa

# Importamos los módulos necesarios
import pdb
#Importamos la funcion reduce. Obtiene un solo resultado de una lista
from functools import reduce

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
