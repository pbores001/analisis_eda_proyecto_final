# Análisis Exploratorio de Datos (EDA) - Asistencia y Rendimiento de Estudiantes

Este proyecto tiene como objetivo realizar un **análisis exploratorio de los datos** relacionados la información de varios archivos csv que tratan sobre la asistencia de alumnos de un centro académico, así como de su rendimiento, tanto en exámenes como en tareas de diferentes asignaturas y la comunicación entre padres y profesores.Los datos abarcan entre el primer año escolar de 2024 y el primer trimestre de 2025.

## Herramientas Utilizadas

Este proyecto ha sido realizado utilizando las siguientes herramientas:

- **Python**: Lenguaje de programación utilizado para el análisis y manipulación de los datos.
- **Pandas**: Librería principal para la manipulación de datos y análisis.
- **Visual Studio Code**: Editor de código utilizado para escribir y ejecutar los scripts de Python.
- **Power BI**: Herramienta de Business Intelligence para generar el Dashboard de este proyecto.


## Datos

Los datos utilizados en este proyecto provienen de cinco archivos diferentes:

1. **Dataset: attendance.csv**  
   Este archivo contiene datos sobre la asistencia de los alumnos al centro de estudio:
   - `Student_ID`: ID del estudiante.
   - `Date`: Fecha de asistencia.
   - `Subject`: Asignatura.
   - `Attendance_Status`: Si los alumnos han asistido a clase o si han llegado tarde o se han ido pronto.

2. **Dataset: communication.csv**
   - `Student_ID`: ID del estudiante.  
   - `Date`: Fecha de envói de mensaje.
   - `Message_Type`: Tipo de mensaje, si el destinatario son los padres o los profesores y si son mensajes automáticos.
   - `Message_Content`: Texto de mensaje.

3. **Dataset: homework.csv**
   - `Student_ID`: ID del estudiante.
   - `Subject`: Asignatura.
   - `Assignment_Name`: Nombre de la tarea.
   - `Due_Date`: Fecha de realización de tarea.
   - `Status`: Estado de tarea.
   - `Grade_Feedback`: Nota de la tarea.
   - `Guardian_Signature`:  Si tiene la tarea firma del tutor o no.

4. **Dataset: performance.csv**  
   - `Student_ID`: ID del estudiante.
   - `Subject`: Asignatura.
   - `Exam_Score`: Nota de Examen.
   - `Homework_Completion_%`: Porcentaje de realización de tareas.
   - `Teacher_Comments`: Respuesta de los profesores.

5. **Dataset: students.csv**  
   - `Student_ID`: ID del estudiante.
   - `Full_Name`: Nombre y apellido de alumno.
   - `Date_of_Birth`: Fecha de nacimiento.
   - `Grade_Level`: Nivel de grado (del 1 al 5).
   - `Emergency_Contact`: Número de contacto para emergencias.

## Archivos

 El repositorio contiene los siguientes archivos y carpetas:

- **Archivo `README.md`**: Descripción de los pasos seguidos durante el proyecto y el informe del análisis.
- **Carpeta `data/`**: Contiene los archivos de datos originales (carpeta 'data_raw') y transformados (carpeta 'data_transformed').
- **Carpeta `src/`**: Contiene el archivo de soporte `sp.limpieza.py`. donde hay funciones usadas en el EDA. 
- **Archivo `eda.py`**: Contiene el código del análisis y la visualización de los datos.
- **Archivo `rend_asist_estudiantes_dashboard.pbix`**: Contiene el archivo de Power BI con el dashboard del análisis.


## Pasos del Proyecto

### 1. Transformación y limpieza de datos

- **Importación y visión general de los datos (utilizando la librería Pandas).**
- **Pasar los valores y nombres de columnas a minúsculas.**
- **Cambiar nombres de algunas columnas para mejorar la comprensión.**
- **Corregir las columnas al tipo de dato correcto.**
- **Eliminar las columnas redundantes o irrelevantes.**
- **Gestión de nulos**


### 2. Análisis descriptivo de los datos

- **Resumen estadístico de los 5 dataframes**.


### 3. Visualización de datos

Aquí se emplearon las librerías de seaborn (https://seaborn.pydata.org/) y matplolib (https://matplotlib.org/)

- **Promedio de asistencia por grado**.
- **Los días (top 10) con mayor númeor de ausencias**.
- **Distribución de estados de asistencia**.
- **Distribución de notas de examen**.
- **Nota media de asignatura**.
- **Nota media de asignatura por grado**.
- **Distribución de notas de examen por asignatura**.
- **Distribución de estado de tareas**.
- **Distribución de tareas entregadas por los estudiantes**.
- **Cantidad de mensajes por grado**.
- **Distribución de edad de los estudiantes**.
...etc.


### 4. Guarcar archivos limpios

Se guardaron estos archivos generados.


### 5. Generación del Dashboard en Power BI

El Dashboard se basa en cubrir la información principal de la asistencia  general de los alumnos y por grado, así como el rendimiento académico por realización de tareas y notas de examen en las diferentes asignaturas, los rangos de cumplimiento de tareas de los alumnos y la media de tareas hechas por asignatura, la comunicación entre padres y profesores como el número de intercambio de mensajes entre ambas partes y datos demográficos como número de estudiantes por grado o por rango de edad. Igualmente en el dashboard se han añadido unos slciers para poder visualziar la información de los gráficos y KPIs, por nivel de grado, asignatura, el estado de asistencia y los trimestres de 2024 y el primero de 2025. 


## Resultados
El análisis exploratorio de los datos escolares revela una estructura educativa con cierta uniformidad en aspectos como el rendimiento académico y la comunicación familia-escuela. Sin embargo, surgen indicios que merecen especial atención desde una perspectiva pedagógica y de gestión educativa.

**1. Asistencia escolar:**
La tasa general de asistencia del 62% es baja para un entorno educativo eficaz. Aunque las diferencias entre grados son leves, esta cifra global podría reflejar problemas sistémicos como falta de motivación, problemas familiares, o incluso eventos externos como enfermedades o condiciones sociales. La concentración de ausencias entre el 9 y el 18 de marzo de 2024 podría coincidir con una interrupción escolar temporal (como Semana Santa), lo que sugiere que el análisis de ausencias debe considerar el calendario escolar para evitar interpretaciones erróneas.

**2. Tipologías de asistencia:**
La predominancia de estados como “asistencia”, “ausencia” y “llegada tarde” sugiere que el sistema de control de asistencia es simple y que los eventos atípicos (como ausencias justificadas o salidas anticipadas) son minoritarios o menos registrados. Esto puede limitar el análisis de comportamientos de asistencia.

**3. Evaluación académica:**
El hallazgo de que casi 7,000 estudiantes tienen una puntuación perfecta (100) en exámenes, frente a otras calificaciones que se distribuyen en volúmenes mucho menores, plantea dudas sobre la validez o el rigor de las evaluaciones aplicadas. Este patrón puede deberse a pruebas poco desafiantes, criterios de corrección poco exigentes o incluso prácticas de calificación infladas. Lo mismo se observa en las tareas, donde los porcentajes de cumplimiento se agrupan en valores fijos (80%, 90%, 95%, 100%), sin variabilidad intermedia, lo que limita el poder de discriminación del sistema evaluador.

**4. Rendimiento homogéneo:**
La escasa dispersión en las notas medias entre asignaturas (73.8% a 74.4%) y la similitud en las distribuciones por grado indican una homogeneidad que puede ser positiva si refleja equidad entre docentes, pero también puede sugerir falta de personalización o adaptación de las evaluaciones al contexto de cada curso o materia.

**5. Distribución de tareas:**
Con más de 30,000 tareas completadas frente a 20,000 no hechas y 11,000 pendientes, el compromiso académico general parece adecuado, aunque todavía hay una porción importante de entregas no realizadas. Sería útil saber como se registra en el centro educativo los diferentes tipos de tareas. 

**6. Comunicación con las familias:**
Los mensajes entre padres y profesores están bien equilibrados en cantidad, lo que indica un canal de comunicación activo y posiblemente eficiente. Sin embargo, el hecho de que los grados superiores (3º y 4º) concentren más mensajes sugiere una mayor implicación de los docentes o una mayor necesidad de seguimiento a medida que se avanza en el nivel educativo. Esto podría estar relacionado con la preparación para etapas educativas posteriores.

**7. Distribución de estudiantes y edades:**
El mayor número de alumnos en 3º y 4º grado, así como los picos de edad en los 10, 14 y 18 años, puede estar relacionado con las etapas clave del sistema educativo: entrada a primaria, paso a secundaria y finalización del ciclo. Esto también podría reflejar fenómenos como repeticiones de curso, migraciones escolares o decisiones institucionales que priorizan ciertos niveles.

**Conclusión Final**
En conjunto, el análisis revela un sistema educativo donde los resultados académicos y las interacciones escolares parecen estables, pero también sugiere zonas grises que podrían estar enmascarando problemas estructurales. La baja tasa de asistencia, la posible sobrestimación del rendimiento académico y la desigual distribución de estudiantes por grados invitan a reflexionar sobre la calidad de la educación ofrecida, la validez de las evaluaciones y el compromiso real de los alumnos.

Además, este tipo de análisis pone en evidencia la necesidad de contextualizar los datos escolares dentro del calendario académico, la cultura institucional y las condiciones sociales del alumnado. Un uso continuo de herramientas de análisis de datos como este puede apoyar decisiones estratégicas, identificar estudiantes en riesgo y mejorar tanto el rendimiento como la equidad en el sistema escolar.

