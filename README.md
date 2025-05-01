# analisis_eda_proyecto_final

## Sesión 6
- Revisar las visualizaciones de asistencia.
-🟡 df_performance – Notas y rendimiento
### Qué analizar:
    -Distribución de exam_score y homework_completion_%
    -¿Hay valores extremos? (outliers, negativos, mayores a 100)
    -¿Qué asignaturas tienen mayores o menores notas?
    -Promedio de nota por asignatura o grado (si tienes grade_level asociado)
### Visualizaciones útiles:
    -histplot, boxplot o violinplot para scores
    -barplot con promedio de nota por asignatura



-🔵 df_homework – Tareas
### Qué analizar:
    -Cantidad de tareas entregadas o completadas por asignatura.
    -Porcentaje de tareas entregadas frente al total por estudiante.
    -Fechas de entrega: ¿hay muchas tareas con due_date en ciertas semanas?
    -Estados de las tareas: submitted, missing, etc.
### Visualizaciones útiles:
    -countplot de status
    -lineplot con número de tareas por fecha



-🔴 df_communication – Comunicación con padres
### Qué analizar:
    -Tipos de mensaje más comunes (message_type)
    -Frecuencia de mensajes por estudiante
    -¿Qué temas se tratan más en los mensajes (message_content)?
    -¿Hay más mensajes en ciertos grados?
### Visualizaciones útiles:
    -countplot de message_type
    -Nube de palabras (wordcloud) del contenido de los mensajes
    -Frecuencia de mensajes por fecha



-🟣 df_students – Datos generales de estudiantes
### Qué analizar:
    -Cantidad de estudiantes por grado.
    -Distribución por edad (si puedes calcularla con date_of_birth).
    -¿Cuántos tienen emergency_contact faltante?
### Visualizaciones útiles:
    -barplot por grado
    -pie chart por nivel educativo
    -Histograma de edades




### ✅ Ventajas de este enfoque:
    -Nos aseguramos de sacar insights limpios y específicos de cada fuente de datos.
    -No se fuerzan uniones que generan muchos NaN.
    -Mejor hacemos visualizaciones claras y luego combinarlas solo si lo necesitamos.

# Pasar los graficos a visualizacion de graficos




