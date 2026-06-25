# Estudiante 3 - Evidencias de resultado

## Datos del estudiante

* Estudiante asociado: Integrante 3
* Módulo principal: Notas
* Responsabilidad adicional: apoyo al módulo Matrículas

## Resultados obtenidos

| N° | Actividad realizada | Resultado entregado por la IA | Cambios realizados manualmente | Archivo creado o modificado | Observación final |
| -- | ------------------- | ----------------------------- | ------------------------------ | --------------------------- | ----------------- |
| 1 | Preparar evidencias del Integrante 3 | Se revisaron y ordenaron los archivos de prompts y evidencias. | Se corrigió el módulo principal del Integrante 3 a Notas. | `prompts/estudiante_3_prompts.md`, `evidencias/estudiante_3_evidencias_resultado.md` | Estructura lista para registrar el trabajo del módulo. |
| 2 | Crear base del módulo Notas | Se crearon archivos JSON, Python, HTML y JavaScript iniciales. | No aplica. | `data/notas.json`, `core/notas.py`, `web/notas.html`, `static/notas.js` | Funciones preparadas para desarrollo posterior. |
| 3 | Agregar lectura y guardado de notas | Se desarrollaron `cargar_notas()` y `guardar_notas()`. | No aplica. | `core/notas.py` | El JSON se crea vacío si no existe y se guarda legible. |
| 4 | Agregar validaciones y promedio de notas | Se desarrollaron validación de notas, cálculo de promedio y estado final. | No aplica. | `core/notas.py` | Se validan notas entre 0 y 20. |
| 5 | Validar matrícula antes de registrar notas | Se creó `verificar_matricula_para_nota()`. | No aplica. | `core/notas.py` | Consulta `data/matriculas.json` y acepta matrículas activas. |
| 6 | Evitar notas duplicadas por matrícula | Se desarrolló `nota_existe()`. | No aplica. | `core/notas.py` | Evita duplicar notas del mismo estudiante, materia y periodo. |
| 7 | Registrar notas con validaciones | Se desarrolló `registrar_nota()`. | No aplica. | `core/notas.py` | Valida matrícula, notas, duplicados, promedio y estado final. |
| 8 | Listar notas por estudiante y materia | Se desarrollaron listados generales, por estudiante y por materia/periodo. | No aplica. | `core/notas.py` | Devuelven listas simples para conectar con la web. |

## Conversación o resumen de interacción con IA

- Se indicó que el Integrante 3 trabajará el módulo Notas.
- Se indicó que también dará apoyo al módulo Matrículas.
- Se preparó la estructura inicial para registrar prompts, resultados y evidencias.
- Después se desarrollarán los archivos base del módulo Notas.
- Se crearon los archivos iniciales del módulo Notas con funciones base y JSON vacío.
- Se implementó lectura y escritura JSON para notas.
- Se implementó validación de notas, promedio y estado final.
- Se agregó validación de matrícula activa antes de registrar notas.
- Se agregó verificación para evitar notas duplicadas.
- Se completó el registro de notas con validaciones principales.
- Se agregaron funciones para listar notas por distintos criterios.
