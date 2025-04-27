
#Importaciones
import pandas as pd
import numpy as np

#Para llamar a archivos de otras carpetas
import sys
sys.path.append('..')

#Visualizar todas las columnas
pd.set_option('display.max_columns', None)


#Después importamos el archivo de funciones ('sp_limpieza.py') 
import src.sp_limpieza as sp
#Importamos importlib para poder recargar el módulo y reflejar los cambios actualizados
import importlib  
importlib.reload(sp) 


#Para interactuar con el sistema operativo
import os
#Devuelve la ruta del directorio actual
print(os.getcwd())


#Librerías de visualización de gráficos
import seaborn as sns
import matplotlib.pyplot as plt


# 1. Transformación y limpieza de datos
# 1.1. Importación y visión general de los datos

#Leer los archivos
df_attendance = pd.read_csv("../data/data_raw/attendance.csv")
df_homework = pd.read_csv("../data/data_raw/homework.csv")
df_performance = pd.read_csv("../data/data_raw/performance.csv")
df_students = pd.read_csv("../data/data_raw/students.csv")
df_communication = pd.read_csv("../data/data_raw/communication.csv")



#Ver dataframe 'df_attendace'
df_att_preliminar =  sp.eda_preliminar(df_attendance)


# 1.2. Eliminar columnas redundantes o irrelevantes
# 1.3. Homogeinizar los nombres de las columnas
# 1.4. Homogeinizar datos categóricos
# 1.5. Cambio tipo de datos y gestión de nulos
# 1.6. Combinar ambas tablas

# 2. Análisis descriptivo de los datos
# 2.1. Resumen estadístico 

# 3. Visualización de los datos.
# 3.1. Histogramas para la distribución de variables numéricas
# 3.2. Boxplots para detectar outliers
# 3.3. Gráficos de barras para variables categóricas
# 3.4. Heatmap de correlaciones
# 4. Guardar archivos limpios



#rf