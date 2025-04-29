
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

    print('CAMPOS VACÍOS POR COLUMNAS')

    empty_counts = (
        # solo columnas de texto             # recuentos de cada valor
    df.select_dtypes(include='object').apply(lambda col: col.value_counts().get('', 0)))# obtener el count de '' o 0 si no existe
    
    empty_counts = empty_counts[empty_counts > 0]  # quedarnos solo con las que tienen >0
    print(empty_counts)
    
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
def nulos_umbral(df, umbral = 10):

    columns_with_nulls = df.columns[df.isnull().any()]
    colmn_with_nulls_info = pd.DataFrame(
        {
            "Column": columns_with_nulls,
            "Datatype": [df[col].dtype for col in columns_with_nulls],
            "NullsCount":[df[col].isnull().sum() for col in columns_with_nulls],
            "Nulls%":[((df[col].isnull().sum()/df.shape[0])*100) for col in columns_with_nulls],
        }
    )

    display(colmn_with_nulls_info)
    high_nulls_colmn = colmn_with_nulls_info[colmn_with_nulls_info['Nulls%'] > umbral]['Column'].tolist()
    low_nulls_colmn = colmn_with_nulls_info[colmn_with_nulls_info['Nulls%'] <= umbral]['Column'].tolist()
    return high_nulls_colmn, low_nulls_colmn



