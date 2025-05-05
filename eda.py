
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


# 1.2. Limpieza y transformación de los datos

#Ver dataframe 'df_attendace'
df_att_preliminar =  sp.eda_preliminar(df_attendance)


#Quitar los espacios y pasar a misnuculas las tabla
df_attendance = sp.valores_a_minus(df_attendance)
df_attendance.sample(10)


#Ver en la columna attendance_status que valores tiene.
conteo = df_attendance['attendance_status'].value_counts()
conteo


#Corregimos el valor 'absnt' por 'absent' y comprobamos los resultados de la columna
df_attendance['attendance_status'] = df_attendance['attendance_status'].replace('absnt','absent')

conteo = df_attendance['attendance_status'].value_counts()
conteo
#Ya tenemos los valores de esta columna corregidos.



#Cambiar nombre de columna 'date' para hacerla mas descriptiva y 'attendace_status' para hacerla mas corta.
df_attendance.rename(columns={'date':'att_date', 'attendance_status':'att_status'}, inplace= True)


# Como la columna 'date' es de tipo 'Object' vamos a pasarla a tipo Datetime y comprobamos el tipo de dato que sea correct
df_attendance = sp.convertir_columna_a_fecha(df_attendance, 'att_date')
df_attendance.sample(10)



#Comprobación del tipo de dato de la columna
print(df_attendance['att_date'].dtype)


#Comprobamos el resto de columnas que sean de tipo correcto.
print(df_attendance.dtypes)


#Ver dataframe 'df_homework'
df_hw_preliminar =  sp.eda_preliminar(df_homework)
df_hw_preliminar


#Pasar dataframe a minusculas
df_homework = sp.valores_a_minus(df_homework)
df_homework.sample(10)


#La columna 'due_date' tiene valores de fecha con diferentes formatos.
# Hay que pasarlo a un formato y asignalo como de tipo datetime.

df_homework = sp.convertir_columna_a_fecha(df_homework, 'due_date')
df_homework.sample(10)


#Comprobación del tipo de dato de la columna
print(df_homework['due_date'].dtype)



#Sacar nulos de la columna 'due_date' mediante funcion de sp.limpieza.py
nulos = sp.nulos_num_porcentaje(df_homework)
print(nulos)



# La columna 'due_date' tiene una cantidad elevada de nulos (20.33%) por lo que antes de imputarla comprobamos
#como es la distribución de sus valores para poder así valorar si imputar los nulos, si por media, moda o mediana.

df_homework['due_date'].hist(bins=50, figsize=(10,5))
plt.title('Distribución de Due Date')
plt.xlabel('Fecha')
plt.ylabel('Cantidad')
plt.xticks(rotation=45)
plt.show()

#Comprobamos las estadísticas descriptivas de 'due_date'
print(df_homework['due_date'].describe())


#Dado que las fechas están bastante centradas en torno a finales de 2024, lo más razonable sería:
# Imputar con la mediana (50%), que es 2024-12-09, ya que la mediana es robusta frente a outliers y nos va a evitar 
# en caso de haber un par de fechas raras que el resultado no se distorsione demasiado.

mediana_fecha = df_homework['due_date'].median()
df_homework['due_date'].fillna(mediana_fecha, inplace= True)



#Comprobamos que los nulos han desaparecido
nulos = sp.nulos_num_porcentaje(df_homework)
print(nulos)



#Para coregir la columna 'status' vamos a comprobar primero el tipo de valores que tiene.
status_valores = df_homework['status'].value_counts()
status_valores



#Vamos a homogeinizar esos valores. 
mapeo_status = {
    '✅':'done',
    '❌':'not done',
    '✔':'done',
    'pending':'pending',
    'done':'done',
    'not done':'not done',
}

df_homework['status'] = df_homework['status'].replace(mapeo_status)

status_valores = df_homework['status'].value_counts()
status_valores



#Debemos comprobar la columna 'guardian_signatura' ya que tiene campos vacíos que pandas
# lo detecta como cadena de texto vacía.
valores = df_homework['guardian_signature'].value_counts()
print(valores)



#Debemos de convertir la cadena vacia por nulos de numpy. Después vamos a comprobar cuantos nulos son.
df_homework['guardian_signature'] = df_homework['guardian_signature'].replace('', np.nan)
ver_nulos= sp.nulos_num_porcentaje(df_homework['guardian_signature'])
ver_nulos


#Comprobamos la distribución (en porcentaje) de los 3 valores de la columna.
print(df_homework['guardian_signature'].value_counts(dropna=False, normalize=True)*100)


#Hay un 33% de nulos de la columna 'guardian_signature' por tanto vamos a ver sus cuartiles, media etc.
print(df_homework['guardian_signature'].describe())



#Vamos a imputar los nulos con 'unknown' ya que así no modificamos artificialmente la proporción original y
# dejamos constancia de que falta esta información.

df_homework['guardian_signature'].fillna('unknown', inplace = True)

#Comprobamos la distribución (en porcentaje) de los 3 valores de la columna.
print(df_homework['guardian_signature'].value_counts())


df_homework.sample(10)


#Ver dataframe 'df_communication'
df_comm_preliminar =  sp.eda_preliminar(df_communication)
df_comm_preliminar


df_communication = sp.valores_a_minus(df_communication)
df_communication.sample(10)



#Cambiar el nombre de date a uno mas descriptivo y convertirlo a tipo datetime
df_communication.rename(columns={'date':'date_message'}, inplace=True)

df_communication = sp.convertir_columna_a_fecha(df_communication, 'date_message')
df_communication.sample(10)


#Comprobación del tipo de dato de la columna
print(df_communication['date_message'].dtype)


#Comprobar los valores que hay en la columna 'date_message'
print(df_communication['message_type'].value_counts())


#Viendo la columna 'message_content' a través de la funcion eda_preliminar parece que hay campos vacíos (cadenas de texto vacías)
# que no figuran como nulos.

df_communication['message_content'] = df_communication['message_content'].replace('', np.nan)
ver_nulos= sp.nulos_num_porcentaje(df_communication['message_content'])
ver_nulos

#Eliminamos los nulos de 'message_content' ya que son escasos y buscamos tener el  dataframe lo más limpio posible.
df_communication = df_communication.dropna(subset=['message_content'])



df_prfm_preliminar = sp.eda_preliminar(df_performance)
df_prfm_preliminar



df_performance = sp.valores_a_minus(df_performance)
df_performance.sample(10)



#Sabiendo que las notas deben ser entre 0-100, aquellas inferiores a 0 y superiores a 100 van a ser outliers, tenemos que identificarlos 
#y saber cuantos son en porcentaje. 

#Filas de la columna
total_filas = df_performance.shape[0]

#Outliers inferioes
outliers_inf = df_performance[df_performance['exam_score'] < 0]
outliers_inf_num = outliers_inf.shape[0]
outiersl_inf_porcentaje = round(outliers_inf_num / total_filas * 100, 2)

#Outliers superiores
outliers_sup = df_performance[df_performance['exam_score'] > 100]
outliers_sup_num = outliers_sup.shape[0]
outliers_sup_porcentaje = round(outliers_sup_num / total_filas * 100, 2)

#Mostramos los resultados
print(f"Outliers inferiores (<0):{outliers_inf_num}, que corresponden al {outiersl_inf_porcentaje} de los datos")
print(f"Outliers superiores (>100):{outliers_sup_num}, que corresponden al {outliers_sup_porcentaje} de los datos")



#Dado que las notas deben oscilar entre 0 y 100 como mínimo y máximo esos outliers que representan un 14.09% de los datos,
#no vamos a eliminarlos ya que en este análisis vamos a tener en cuenta el rendimiento en los exámenes. Por eso, los outliers vamos
#a reescalarlos al máximo permitido, asumiendo que han sido errores del dataset original. 

df_performance.loc[df_performance['exam_score'] > 100, 'exam_score'] = 100



#Comprobamos que ya no hay outliers
print(f"Outliers superiores (>100):{outliers_sup_num}, que corresponden al {outliers_sup_porcentaje} de los datos")




def limpiar_homework_completion(x):
    """
    Limpia y convierte los valores de 'homework_completion_%' a números. Elimina el '%' de las cadenas y convierte a `float`. 
    Los valores negativos se convierten en 0 y los mayores a 100 se ajustan a 100.

    Parámetros:
    x (str, int, float): Valor a limpiar y convertir.

    Devuelve:
    float: Valor entre 0 y 100, o None si hay un error.
    """
    try:
        if isinstance(x, str) and '%' in x:
            x = float(x.replace('%', '').strip())
        elif isinstance(x, str):
            x = float(x.strip())
        elif isinstance(x, (int, float)):
            x = float(x)
        else:
            return None
        
        if x < 0:
            x = 0
        elif x > 100:
            x = 100
        return x
    except:
        return None

# Verificamos primero existencia de la columna antes de limpiar
if 'homework_completion_%' in df_performance.columns:
    # Limpiamos la columna 'homework_completion_%' directamente 
    df_performance['homework_completion_%'] = df_performance['homework_completion_%'].apply(limpiar_homework_completion)
    # Convertimos los valores a formato porcentaje
    df_performance['homework_completion_%'] = df_performance['homework_completion_%'].apply(lambda x: f"{round(x)}%" if x is not None else None)
    print("Columna 'homework_completion_%' limpiada correctamente.")
else:
    print("La columna 'homework_completion_%' no existe en df_performance.")




#Comprobamos que los valores de la columna 'homework_completion_%' sean consistentes
df_performance.sample(10) 



#Los campos vacíos de la columna 'teacher_comments' pasarlos a nulos para saber cuantos hay.np
df_performance['teacher_comments'] = df_performance['teacher_comments'].replace('', np.nan)

# Contar valores nulos en la columna 'teacher_comments'
nulos = sp.nulos_num_porcentaje(df_performance['teacher_comments'])
nulos



#Imputar las filas que tienen nulos (un 9.74%) ya que no queremos
# perder el resto de información de esas filas.

df_performance['teacher_comments'] = df_performance['teacher_comments'].fillna('No comment')
df_performance.sample(10)



df_std_preliminar = sp.eda_preliminar(df_students)
df_std_preliminar


df_students = sp.valores_a_minus(df_students)
df_students.sample(10)


#Pasar la columna date_of_birth al formato correcto
df_students = sp.convertir_columna_a_fecha(df_students,'date_of_birth')
df_students.sample(10)


#Comprobar los valores nulos de 'date_of_birth'
nulos = sp.nulos_num_porcentaje(df_students['date_of_birth'])
nulos


#Eliminar los nulos de 'date_of_birth' de los estudiantes porque no es un dato relevante este dato demográfico para el analisis.
#Estamos analizando las notas, asistencias y productividad de los estudiantes.
df_students = df_students.dropna(subset=['date_of_birth'])


#Contar los nulos de emergency_contact y valor que hacer con ellos.
nulos_emergency_contact =sp.nulos_num_porcentaje(df_students['emergency_contact'])
nulos_emergency_contact


#Eliminamos estos nulos porque no son relevantes y queremos filas lo más completaas posibles.
df_students = df_students.dropna(subset=['emergency_contact'])


# 2. Análisis descriptivo de los datos
# 2.1. Resumen estadístico


#Ver estadísticas df_attendance
att_stats = sp.obtener_estadisticas(df_attendance)
att_stats


#Ver estadísticas df_homework
hmw_stats = sp.obtener_estadisticas(df_homework)
hmw_stats


perf_stats = sp.obtener_estadisticas(df_performance)
perf_stats


#Ver estadísticas df_communication 
comm_stats = sp.obtener_estadisticas(df_communication)
comm_stats


#Ver estadísticas df_students
std_stats = sp.obtener_estadisticas(df_students)
std_stats


#. Visualización de los datos

#Analizamos los dataframes por separado y uniendo algunos para sacar visualziaciones relevantes. No hacemos un merge general de todos los dataframes a la vez
# porque se generan una cantidad muy elevada de NaN.

#Como vamos a necesitar resetear los índices de algunos dataframes para que 'student_id' salga como columna,
#lo vamos a hacer con el resto de dataframes para que todos estén igual y no haya problemas en Power BI.
df_attendance = df_attendance.reset_index()
df_homework = df_homework.reset_index()
df_performance = df_performance.reset_index()
df_communication = df_communication.reset_index()
df_students = df_students.reset_index()


#🟢🟢Datos de asistencia.
#Ver cual es el promedio de asistencia general.
# Crear una columna numérica para mapear el estado de asistencia
df_attendance['att_numeric'] = df_attendance['att_status'].map({
    'present': 1,
    'late': 1,
    'left early': 1,
    'absent': 0,
    'excused': 0
})

#Calcular la tasa de asistencia general
attendance_rate = df_attendance['att_numeric'].mean()*100
print(f"El promedio de la asistencia general es {attendance_rate:.2f}%")




#Ver la tasa de asistencia por grado.
#Unimos el df_attendande con df_students para poder tener la información de la columna 'grade_level'.
df_att_grade = pd.merge(df_attendance, df_students[['student_id', 'grade_level']], on='student_id', how='left')

# Agrupar por 'grade_level' y calcular la tasa de asistencia promedio por grado
att_by_grade = df_att_grade.groupby('grade_level')['att_numeric'].mean().reset_index()

# Visualizar el gráfico
plt.figure(figsize=(8,5))
sns.barplot(data=att_by_grade, x='grade_level', y='att_numeric', palette='viridis')
plt.title('Tasa promedio de Asistencia por Grado')
plt.xlabel('Nivel de Grado')
plt.ylabel('Tasa de Asistencia')
plt.ylim(0,1)
plt.show()



#Ver los días con más número de ausencias.

#Filtrar solo los registros 'absent' o 'excused'. 
df_absent = df_attendance[df_attendance['att_status'].isin(['absent','excused'])]

#Agrupar df_absent por la columna 'att_date' y contar las ausencias
absences_by_date = df_absent.groupby('att_date').size().reset_index(name = 'absence_count')

#Ordenar de mayor a menor para ver en primer lugar los días con más ausencias
# Mostrar solo los top 10 días con más ausencias
top_days = absences_by_date.head(10)

plt.figure(figsize=(12,6))
sns.barplot(data=top_days, x='att_date', y='absence_count', color='lightseagreen')
plt.title('Top 10 Días con Más Ausencias')
plt.xlabel('Fecha')
plt.ylabel('Número de Ausencias')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



#Ver el porcentaje del total de registros representa cada tipo de asistencia
#Usamos value_counts(normalize=True) para obtener el porcentaje de cada tipo de asistencia. Hacemos *100 para obtenerlo en porcentaje.
attendance_counts = round(df_attendance['att_status'].value_counts(normalize=True)*100,2)
print(attendance_counts)


#Ver cuántos estudiantes están en cada categoría de asistencia (present, late, absent, etc.).
plt.figure(figsize=(8,5))
sns.countplot(data=df_attendance, x='att_status', palette='viridis')
plt.title('Distribución de Estados de Asistencia')
plt.xlabel('Estado de Asistencia')
plt.ylabel('Cantidad de Registros')
plt.show()



#Datos de notas y rendimiento.


#Hacer un histograma de exam_score con la curva KDE, para visualizar mejor como la distribución de notas.
sns.histplot(df_performance['exam_score'], kde = True, color = 'lightseagreen')
plt.title('Distribución de Notas de Examen')
plt.xlabel('Nota de Examen')
plt.show()

#Hacer un histograma con la realización de tareas 'homework_completion_%'.
sns.histplot(df_performance['homework_completion_%'], kde = True, color = 'lightseagreen')
plt.title('Distribución de Porcentaje de Tareas Completadas')
plt.xlabel('Porcentaje de Tareas')
plt.show()



#Asignaturas con mayores o menores notas (promedio)
#Calcular promedio de asinaturas
avg_scores_by_subject = df_performance.groupby('subject')['exam_score'].mean().sort_values()

#Visualización de barras
sns.barplot(x = avg_scores_by_subject.values, y = avg_scores_by_subject.index, palette = 'viridis')
plt.title('Nota Media por Asignatura')
plt.xlabel('Nota Media')
plt.ylabel('Asignatura')
plt.show()

print(avg_scores_by_subject)



#Promedio de nota por asignatura y grado
#Hacer el merge por columna 'student_id'
df_perf_grade = pd.merge(df_performance, df_students[['student_id','grade_level']], on = 'student_id', how = 'left')

#Calcular el promedio por asignatura y grado agrupando por grado y asignatura
avg_by_subject_grade = df_perf_grade.groupby(['grade_level','subject'])['exam_score'].mean().reset_index()

#Visualizar gráfico
plt.figure(figsize = (10,6))
sns.barplot(data = avg_by_subject_grade, x = 'grade_level', y = 'exam_score', hue = 'subject', palette = 'Paired')
plt.title('Promedio de Nota por Asignatura y Grado')
plt.xlabel('Grado')
plt.ylabel('Notas Promedio')
plt.legend(title = 'Asignatura')
plt.show()



#Ver la distribución de 'exam_score' y 'subject'.
sns.violinplot(data = df_performance, x = 'subject', y = 'exam_score', palette = 'viridis')
plt.title('Distribución de Notas de Examen por Asignatura')
plt.xlabel('Asignatura')
plt.ylabel('Nota de Examen')
plt.xticks(rotation=45)
plt.show()



#Datos de Homework.

# Ver cantidad de tareas entregadas por asignatura.
#Filtrar a tarvés de df_homework aquellas tareas con estado 'done' y el nombre de la asignatura
submitted_by_subject = df_homework[df_homework['status'] == 'done']['subject'].value_counts()

sns.countplot(data=df_homework, x='status', order = df_homework['status'].value_counts().index, color = 'lightseagreen')
plt.title('Distribución de estados de tareas')
plt.ylabel('Cantidad de Tareas')
plt.xlabel('Estado de Tareas')
plt.show()



#Calculamos porcentaje de tareas entregadas por estudiantes
hmw_per_stu = df_homework.groupby('student_id')['status'].value_counts().unstack().fillna(0)
hmw_per_stu['porcentaje_entregadas'] = hmw_per_stu['done'] / hmw_per_stu.sum(axis=1) * 100

# Histograma del porcentaje de tareas entregadas
plt.figure(figsize=(8, 5))
sns.histplot(hmw_per_stu['porcentaje_entregadas'], bins=20, color='lightseagreen', kde=True)
plt.title('Distribución del % de Tareas Entregadas por Estudiante')
plt.xlabel('% de Tareas Entregadas')
plt.ylabel('Número de Estudiantes')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()



#Comunicacion con padres 
#Tipo de mensajes más comunes de los padres con los profesores
plt.figure(figsize=(8, 4))
sns.countplot(data=df_communication, x='message_type', order=df_communication['message_type'].value_counts().index, color = 'lightseagreen')
plt.title('Tipos de mensajes más comunes')
plt.xticks(rotation=45)
plt.show()



#Frecuencia de mensajes por estudiante
#Seleccionamos el numero de mensajes por numero de estudiantes
msg_per_student = df_communication['student_id'].value_counts()

plt.figure(figsize=(10, 4))
sns.histplot(msg_per_student, bins=30)
plt.title('Frecuencia de mensajes por estudiante')
plt.xlabel('Cantidad de mensajes')
plt.ylabel('Número de estudiantes')
plt.show()



# Comprobar si hay más mensajes en ciertos grados. Para ver si la comunicación entre padres y profesores varía según el grado.
df_comm_grade = pd.merge(df_communication, df_students[['student_id', 'grade_level']], on='student_id', how='left')

plt.figure(figsize=(8, 4))
sns.countplot(data=df_comm_grade, x='grade_level', order=sorted(df_comm_grade['grade_level'].dropna().unique()), color = 'lightseagreen')
plt.title('Cantidad de mensajes por grado')
plt.xlabel('Grado')
plt.ylabel('Cantidad de mensajes')
plt.show()


#Comprobar la frecuencia de mensajes por fecha
msgs_by_date = df_communication.groupby('date_message').size()

plt.figure(figsize=(12, 5))
msgs_by_date.plot(color = 'lightseagreen')
plt.title('Frecuencia de mensajes por fecha')
plt.xlabel('Fecha')
plt.ylabel('Cantidad de mensajes')
plt.tight_layout()
plt.show()


#Datos de estudiantes.df_students. 
#Comprobar la cantidad de estudiantes por grado
plt.figure(figsize=(8,5))
sns.countplot(data=df_students, x='grade_level', palette='viridis')
plt.title('Cantidad de estudiantes por grado')
plt.xlabel('Grado')
plt.ylabel('Cantidad de Estudiantes')
plt.show()



#Comprobar la distribución de los estudiantes por edad 
# Calcular edad (asumiendo análisis en 2025)
hoy = pd.Timestamp('2025-01-01')
df_students['edad'] = df_students['date_of_birth'].apply(lambda x: hoy.year - x.year if pd.notnull(x) else None)

# Histograma de edades
plt.figure(figsize=(8,5))
sns.histplot(df_students['edad'].dropna(), bins=10, kde=True, color='lightseagreen')
plt.title('Distribución de edades de los estudiantes')
plt.xlabel('Edad')
plt.ylabel('Cantidad')
plt.show()


#Comprobar si hay esrtudiantes que no tengan un contacto de emergencia.
faltantes = df_students['emergency_contact'].isna().sum()
total = len(df_students)

print(f"Número de estudiantes sin contacto de emergencia: {faltantes}")
print(f"Porcentaje: {faltantes / total:.1%}")


#Ver la distribución de estudiantes por grado
df_students['grade_level'].value_counts().plot.pie(autopct='%1.1f%%', figsize=(6,6), colors=sns.color_palette('viridis'))
plt.title('Distribución de estudiantes por nivel/grado')
plt.ylabel('')
plt.show()

#4.Guardar los archivos limpios
#Guardar los dataframes limpios
df_attendance.to_csv("../data/data_transformed/attendance_limpio.csv", index = False)
df_homework.to_csv("../data/data_transformed/homework_limpio.csv", index = False)
df_performance.to_csv("../data/data_transformed/performance_limpio.csv", index = False)
df_students.to_csv("../data/data_transformed/students_limpio.csv", index = False)
df_communication.to_csv("../data/data_transformed/communication_limpio.csv", index = False)