# Eva Gonzalez Correa

import pytest
import prueba1
import pandas as pd

def test_abrir_fichero():
    archivo_1= "finanzas2020[1].csv"
    archivo_2= "fian.csv"
    assert prueba1.abrir_fichero(archivo_1)=="El archivo existe"
    assert prueba1.abrir_fichero(archivo_2)=="El archivo no existe"

def test_comprobar_columnas():
    csv = "finanzas2020[1].csv"
    fichero = pd.read_csv(csv, delimiter = "\t", header = 0)
    assert prueba1.comprobar_columnas(fichero)==12

def test_comprobar_columnas2():
    fichero=pd.DataFrame()
    fichero["Enero"]=[1,2,3,4,5]
    assert prueba1.comprobar_columnas(fichero)==1

def test_tipo_de_dato():
    df=pd.DataFrame()
    df["Enero"]=[1,2,"error",-5,4]
    df["Febrero"]=[4,8,-1,"-6","no"]
    assert prueba1.tipo_de_dato(df)==["error","no"]
