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

def test_gastos():
    df=pd.DataFrame()
    df["Enero"]=[1,2,-3,-5,4]
    df["Febrero"]=[4,8,-1,-6,9]
    assert prueba1.gastos(df)==[-8,-7]

def test_ingresos():
    df=pd.DataFrame()
    df["Enero"]=[1,2,-3,-5,4]
    df["Febrero"]=[4,8,-1,-6,9]
    assert prueba1.ingresos(df)==[7,21]

def test_mes_mayor_gasto():
    lista=[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11]
    assert prueba1.mes_mayor_gasto(lista)=="Noviembre"
    
def test_mes_ahorro():
    lista_ingreso=[87,56,90,78,56,38]
    lista_gasto=[-83,-45,-7,-10,-57,-3]
    assert prueba1.mes_ahorro(lista_gasto, lista_ingreso)=="Marzo"