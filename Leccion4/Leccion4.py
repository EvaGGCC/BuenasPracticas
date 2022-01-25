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


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ FUNCION FILTER ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Uso de Filter para el calculo de los numeros de una lista que son primos

class Error(Exception):
    """
    Clase donde se define un Error
    """
    pass

# Creamos la funcion a la que aplicar Filter
def primosB(n):
    """
    Números primos. Indica si un valor es primo. Un valor es primo cuando
    es divisible unicamente por dos valores, 1 y si mismo.
    Input
        n: valor a consultar
    Output:
        Informa si es o no primo
    """
    try:
        if n<0:    # Exepcion de numeros negativos
            raise Error
        elif n==0 or n==1:  #0 y 1 no primos
            return False
        else:
            for i in range (2,n):  # Excluido el 1 y el propio numero
                # Condicion de primo
                if n%i==0:      # Si Resto 0 no es primo
                    return False    # No es primo
            return True    # Si no se a cumplido lo demas es primo
    except Error:
        return False   #print(f"Los numeros negativos no son naturales")

