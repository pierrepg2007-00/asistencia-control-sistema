# Estudiante 4 - Evidencias de resultado

## Datos del estudiante

- Estudiante asociado: Integrante 4
- Módulo principal: Asistencia
- Responsabilidad adicional: apoyo al módulo Matrículas

## Resultados obtenidos

| N° | Actividad realizada | Resultado entregado por la IA | Cambios realizados manualmente | Archivo creado o modificado | Observación final |
|---|---|---|---|---|---|---|
| 1 | Preparar evidencias del Integrante 4 | Se revisaron y ordenaron los archivos de prompts y evidencias. | Se corrigio el modulo principal a Asistencia y se agrego responsabilidad adicional de apoyo a Matriculas. | `prompts/estudiante_4_prompts.md`, `evidencias/estudiante_4_evidencias_resultado.md` | Estructura lista para registrar el trabajo del modulo Asistencia. |
| 2 | Crear base del modulo Asistencia | Se crearon archivos JSON, Python, HTML y JavaScript iniciales. | No aplica. | `data/asistencias.json`, `core/asistencia.py`, `web/asistencia.html`, `static/asistencia.js` | Funciones preparadas como borradores para desarrollo posterior. |
| 3 | Agregar lectura y guardado de asistencias | Se desarrollaron `cargar_asistencias()` y `guardar_asistencias()`. | No aplica. | `core/asistencia.py` | El JSON se crea vacio si no existe y se guarda legible con indentacion. |
| 4 | Agregar validaciones de asistencia | Se desarrollaron `validar_estado_asistencia()` y `validar_fecha()`. | No aplica. | `core/asistencia.py` | Valida estados presente/tarde/falta/justificado y fecha YYYY-MM-DD. |
| 5 | Validar matricula antes de registrar asistencia | Se creo `verificar_matricula_para_asistencia()`. | No aplica. | `core/asistencia.py` | Consulta `data/matriculas.json` y acepta solo matriculas activas. |
| 6 | Evitar asistencia duplicada | Se desarrollo `asistencia_duplicada()`. | No aplica. | `core/asistencia.py` | Evita duplicar asistencia del mismo estudiante, materia, periodo y fecha. |
| 7 | Registrar asistencia con validaciones | Se desarrollo `registrar_asistencia()`. | No aplica. | `core/asistencia.py` | Valida matricula, duplicados, campos obligatorios, fecha y estado. |
| 8 | Listar asistencia por estudiante y materia | Se desarrollaron `listar_asistencias()`, `listar_asistencia_por_estudiante()` y `listar_asistencia_por_materia()`. | No aplica. | `core/asistencia.py` | Filtros por estudiante y por materia/periodo con fecha opcional. |

## Conversación o resumen de interacción con IA

- Se indicó que el Integrante 4 trabajará el módulo Asistencia.
- Se indicó que también dará apoyo al módulo Matrículas.
- Se preparó la estructura inicial para registrar prompts, resultados y evidencias.
- Los archivos de prompts y evidencias ya existían pero con datos de "Notas y asistencia". Se actualizaron para reflejar correctamente "Asistencia" como módulo principal.
- Despues se desarrollaran los archivos base del modulo Asistencia (JSON, Python, HTML, JavaScript).
- Se crearon los archivos iniciales del modulo Asistencia con 12 funciones base como borradores, JSON vacio, HTML con formularios y JavaScript con eventos.
- En los proximos commits se desarrollara la logica de carga/guardado JSON y las validaciones de asistencia.
