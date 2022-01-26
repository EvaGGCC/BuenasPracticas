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