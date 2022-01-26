# Eva Gonzalez Correa


# Importamos modulos
import pandas as pd
import matplotlib.pyplot as plt


# Abrimo fichero y comprobamos su existencia
#Defino una variable global, que se indicara en la función y se actualizara
fichero=0
def abrir_fichero(documento):
    # Indicamos que fichero es variable global
    global fichero
    try:
        # Abrimos el documento csv
        with open(documento) as csv:
            # Añadimos el documento a la variable global definida
			# Tenemos en cuenta el delimitador de las columnas en este caso.
            fichero = pd.read_csv(csv, delimiter = "\t", header = 0)
            respuesta = "El archivo existe"
    # En caso de que no exista generamos una excepcion
    except FileNotFoundError as e:
        respuesta = "El archivo no existe"
        print(respuesta)
    return respuesta

# Funcion comprobar numero de columnas correcto
class DemasidosMeses(Exception):
    pass
class PocosMeses(Exception):
    pass

def comprobar_columnas(fichero):
    # Numero de columnas del fichero, con la longitud de este
    numero_columnas = len(fichero.columns)
    # Condiciones de columnas
    try:
        # Si es mayor lo indica la excepcion, al igual que si es menor
        if numero_columnas > 12:
            #Añadimos excepcion
            raise DemasidosMeses
        elif  numero_columnas > 12:
            raise PocosMeses
        else:
            # Si es igual a 12 (12 meses) Lo indica
            print(f"EL numero de meses es {numero_columnas}")
    # Llamamos las excepciones
    except DemasidosMeses:
        print(f"El documento contiene mas de 12 columnas, {numero_columnas}")
    except PocosMeses:
        print(f"El documento contiene {numero_columnas}")
    # Devolvemos el numero de columnas
    return numero_columnas

def tipo_de_dato(fichero):
    # Lista vacia donde introduciremos los valores erroneos para los test unitarios
    errores=[]
    # Bucle que recorre las columnas
    for i in fichero:
        # Bucle que recorre las filas
        for j in fichero[i]:
            # Si el valor es una cadena de texto (str)
            if type(j)==str:
                # Convertimos a entero
                try:
                    nuevo_j=int(j)
                    fichero[i]=fichero[i].replace(j, nuevo_j)
                    # Si no es posible lo convertimos en 0
                except:
                    fichero[i]=fichero[i].replace(j, int(0))
                    print(f"Mes: {i} ; errorneo: {j}")
                    # Añadimos los valores que no se pueden transformar a errores
                    # Haremos uso de ella en los test unitarios
                    errores.append(j)
    # Devolvemos la lsita de errores
    return errores