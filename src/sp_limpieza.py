
from IPython.display import display
import pandas as pd
import numpy as np


def eda_preliminar(df):
    """
    Realiza un análisis exploratorio preliminar de un DataFrame como:
    Muestra una muestra aleatoria, información general, nulos, duplicados, 
    estadísticas descriptivas y frecuencias del dataframe.
    
    Parameters
    ----------
    df : El DataFrame a analizar.

    Returns
    -------
    Devuelve información de todo lo analizado del Dtaframe.
    """

    display(df.sample(5))
    print('____________________________')

    print('INFO')
    display(df.info())

    print('____________________________')

    print('NULOS')

    display(round(df.isnull().sum()/df.shape[0]*100,2))
    
    print('____________________________')

    print('DUPLICADOS')
    display(df.duplicated().sum())

    print('____________________________')

    print('DESCRIBE')
    display(df.describe().T)

    print('____________________________')

    print('DESCRIBE COLUMNAS OBJECT')
    
    display(df.describe(include = 'O').T)
    
    print('____________________________')

    print('VALUE COUNTS')

    for col in df.select_dtypes(include = 'O').columns:
        print(df[col].value_counts())

    print('____________________________')



#Pasar a minusculas los valores y los nombres de las columnas
def valores_a_minus(df):
    """
    Convierte a minúsculas los nombres de columnas, índice, nombre del índice y valores de texto del DataFrame original.

    Parameters
    ----------
    df : DataFrame a transformar.

    Returns
    -------
    DataFrame original con columnas, índice y textos en minúscula.
    """

    # Convertir los nombres de las columnas a minúsculas
    df.columns = df.columns.str.strip().str.lower()

    # Convertir el índice a minúsculas
    df.index = df.index.str.strip().str.lower()

    # Convertir el nombre del índice a minúsculas
        # is not None, comprueba que el índice tiene nombre.
    if df.index.name is not None:
        df.index.name = df.index.name.strip().lower()

    # Convertir los valores de tipo objeto (texto) a minúsculas
    for col in df.select_dtypes(include='O').columns:
        df[col] = df[col].str.strip().str.lower()
    
    return df



#Detectar nulos en numero y en porcentaje
def nulos_num_porcentaje(df):
    """Devuelve el numero y porcentaje de nulos de cada columna

    Args:
        df (dataframe): dataframe a analizar

    Returns:
        tupla: Dos series de pandas con los datos numéricos de nulos y los datos porcentuales
    """

    nulos_num = df.isnull().sum()
    nulos_porcentaje = (round(df.isnull().sum()/df.shape[0]*100,2))

    return nulos_num, nulos_porcentaje


#Calcular nulos mediante un umbral


#Pasar datos a formato fecha 
def convertir_columna_a_fecha(df, columna, formato='%Y-%m-%d'):
    """
    Convierte una columna de un DataFrame a formato datetime en estilo inglés (YYYY-MM-DD por defecto).

    Parámetros:
    - df: DataFrame de pandas.
    - columna: Nombre de la columna a convertir (string).
    - formato: (opcional) Formato de la fecha. Por defecto '%Y-%m-%d'.

    Devuelve:
    - DataFrame con la columna convertida a datetime.
    """
    try:
        df[columna] = pd.to_datetime(df[columna], format=formato, errors='coerce')
        print(f"Columna '{columna}' convertida a datetime con formato {formato}.")
    except Exception as e:
        print(f"Error al convertir la columna '{columna}': {e}")
    
    return df







