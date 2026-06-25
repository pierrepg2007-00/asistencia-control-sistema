# Estudiante 5 - Evidencias de resultado

## Datos del estudiante
- Estudiante asociado: Integrante 5
- Módulo principal: Reportes e integración
- Responsabilidad adicional: Matrículas

## Resultados obtenidos

| N° | Actividad realizada | Resultado entregado por la IA | Cambios realizados manualmente | Archivo creado o modificado | Observación final |
|---|---|---|---|---|---|
| 1 | Preparar estructura de prompts y evidencias | Se revisaron los archivos existentes y se actualizó la estructura | Ninguno | prompts/estudiante_5_prompts.md, evidencias/estudiante_5_evidencias_resultado.md | Estructura lista para registrar avances |
| 2 | Crear base de matriculas y reportes | Se crearon 7 archivos base con funciones borrador | Ninguno | data/matriculas.json, core/matriculas.py, core/reportes.py, web/matriculas.html, web/reportes.html, static/matriculas.js, static/reportes.js | Archivos base listos para desarrollar funciones completas |
| 3 | Agregar lectura y guardado de matriculas | Se implementaron cargar_matriculas() y guardar_matriculas() con manejo robusto de archivos | Ninguno | core/matriculas.py | Funciones listas siguiendo el patrón de estudiantes.py |
| 4 | Agregar validaciones de matriculas | Se implementaron 4 validaciones consultando JSON de otros módulos | Ninguno | core/matriculas.py | Validaciones listas: estudiante, materia, periodo y duplicados |
| 5 | Registrar matriculas con validaciones | Se implementó registrar_matricula() con todas las validaciones y guardado | Ninguno | core/matriculas.py | Función completa con estado inicial "activa" |
| 6 | Listar y buscar matriculas | Se implementaron 4 funciones de listado y búsqueda con enriquecimiento de datos | Ninguno | core/matriculas.py | Funciones completas con nombres de materia y datos de estudiantes |
| 7 | Cambiar estado de matriculas | Se implementó cambiar_estado_matricula() con 3 estados válidos | Ninguno | core/matriculas.py | Función completa: activa, retirada, finalizada |

## Conversación o resumen de interacción con IA

### Actividad 1: Preparar evidencias del Integrante 5

- Se revisó que los archivos prompts/estudiante_5_prompts.md y evidencias/estudiante_5_evidencias_resultado.md existen.
- Se actualizó la estructura de prompts con los datos del Integrante 5: módulo principal Reportes e integración, responsabilidad adicional Matrículas.
- Se actualizó la estructura de evidencias con la tabla de resultados y la sección de conversación.
- Se dejó preparada la base para registrar los siguientes desarrollos: matrículas, reportes, página principal, servidor, estilos y pruebas.

### Actividad 2: Crear base de matriculas y reportes

- Se creó data/matriculas.json con lista vacía.
- Se creó core/matriculas.py con 12 funciones borrador: cargar, guardar, validar estudiante/materia/periodo, matricula_existe, registrar, listar, buscar, listar por estudiante/materia, cambiar estado.
- Se creó core/reportes.py con 5 funciones borrador: reporte estudiantes por materia, notas por materia, asistencia por materia, estudiantes en riesgo, exportar txt.
- Se crearon web/matriculas.html y web/reportes.html con estructura base.
- Se crearon static/matriculas.js y static/reportes.js con carga inicial.
- Falta desarrollar las funciones completas y la interfaz web.

### Actividad 3: Agregar lectura y guardado de matriculas

- Se implementó cargar_matriculas() con manejo de FileNotFoundError, OSError, JSONDecodeError.
- Si el archivo no existe, se crea automáticamente con [] usando guardar_matriculas([]).
- Si el archivo está vacío, devuelve [].
- Se implementó guardar_matriculas() que crea la carpeta data/ si no existe y guarda con indent=4.
- Se usaron solo json y os (librerías estándar).
- El patrón sigue el mismo estilo de estudiantes.py.

### Actividad 4: Agregar validaciones de matriculas

- Se implementó validar_estudiante_para_matricula(): lee estudiantes.json, verifica existencia y estado activo.
- Se implementó validar_materia_para_matricula(): lee materias.json, verifica existencia y estado activo.
- Se implementó validar_periodo_para_matricula(): lee periodos.json, verifica existencia y estado activo.
- Se implementó matricula_existe(): verifica si ya existe una matrícula con los mismos datos.
- Todas las funciones consultan directamente los archivos JSON sin modificar los módulos de otros integrantes.
- Las funciones devuelven diccionarios con resultado y mensaje claro.

### Actividad 5: Registrar matriculas con validaciones

- Se implementó registrar_matricula() con validación de campos vacíos.
- Llama a validar_estudiante_para_matricula, validar_materia_para_matricula y validar_periodo_para_matricula.
- Verifica duplicados con matricula_existe().
- Asigna estado inicial "activa".
- Guarda en data/matriculas.json con la estructura requerida.
- Devuelve diccionario con resultado, mensaje y datos de la matrícula registrada.

### Actividad 6: Listar y buscar matriculas

- Se implementó listar_matriculas(): devuelve todas las matrículas registradas.
- Se implementó buscar_matricula(): busca matrícula exacta por los tres códigos.
- Se implementó listar_matriculas_por_estudiante(): filtra y enriquece con nombre de materia.
- Se implementó listar_matriculas_por_materia(): filtra por materia/periodo y enriquece con nombres, apellidos y DNI de estudiantes.

### Actividad 7: Cambiar estado de matriculas

- Se implementó cambiar_estado_matricula() que busca la matrícula por los tres códigos.
- Solo permite cambiar el campo estado, no los códigos.
- Estados permitidos: activa, retirada, finalizada.
- Devuelve mensaje claro si el estado es inválido o la matrícula no existe.
