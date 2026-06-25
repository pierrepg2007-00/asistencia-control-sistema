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
