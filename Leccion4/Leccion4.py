# Eva González Correa

# Importamos los módulos necesarios
import pdb
#Importamos la funcion reduce. Obtiene un solo resultado de una lista
from functools import reduce

# -----> FUNCION MAXIMO

# ... Método convencional
def max_convencional(lista):
    """
    Calculo de los valores maximos de sublistas. Usando funcion max.
    Contador:
        i: cada una de las sublistas
    """
    maximos = []
    for i in lista:
        maximos.append(max(i))
    return maximos
