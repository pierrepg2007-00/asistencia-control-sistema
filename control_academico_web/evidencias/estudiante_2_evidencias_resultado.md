# Estudiante 2 - Evidencias de resultado

## Datos del estudiante

* Estudiante asociado: Integrante 2
* Módulo principal: Materias y periodos
* Responsabilidad adicional: apoyo al módulo Matrículas

## Resultados obtenidos

| N° | Actividad realizada | Resultado entregado por la IA | Cambios realizados manualmente | Archivo creado o modificado | Observación final |
| -- | ------------------- | ----------------------------- | ------------------------------ | --------------------------- | ----------------- |
| 1 | Preparar evidencias del Integrante 2 | Se revisaron y ordenaron los archivos de prompts y evidencias. | No aplica. | `prompts/estudiante_2_prompts.md`, `evidencias/estudiante_2_evidencias_resultado.md` | Estructura lista para registrar el trabajo del módulo. |
| 2 | Crear base del módulo Materias y periodos | Se crearon archivos JSON, Python, HTML y JavaScript iniciales. | No aplica. | `data/materias.json`, `data/periodos.json`, `core/materias.py`, `core/periodos.py`, `web/materias.html`, `static/materias.js` | Funciones preparadas para desarrollo posterior. |
| 3 | Agregar lectura y guardado JSON | Se desarrollaron funciones para cargar y guardar materias y periodos. | No aplica. | `core/materias.py`, `core/periodos.py` | Los JSON se crean vacíos si no existen y se guardan legibles. |
| 4 | Agregar validaciones de materias | Se implementaron validaciones de ciclo, estado y existencia de materia. | No aplica. | `core/materias.py` | Se recomienda probar ciclos vacíos, inválidos y códigos existentes. |
| 5 | Generar código automático de materia | Se desarrolló `generar_codigo_materia()` con formato `MAT001`. | No aplica. | `core/materias.py` | La función evita repetir códigos existentes. |
| 6 | Registrar y listar materias | Se desarrollaron `registrar_materia()` y `listar_materias()`. | No aplica. | `core/materias.py` | El registro valida campos obligatorios, ciclo y estado. |
| 7 | Buscar y actualizar materias | Se desarrollaron `buscar_materia()` y `actualizar_materia()`. | No aplica. | `core/materias.py` | Se protege `codigo_materia` y se validan los campos editables. |
| 8 | Gestionar periodos académicos | Se desarrollaron registro, listado, búsqueda, activación y validaciones de periodos. | No aplica. | `core/periodos.py` | Al activar un periodo, los demás quedan cerrados. |

## Conversación o resumen de interacción con IA

- Se indicó que el Integrante 2 trabajará el módulo Materias y periodos.
- Se indicó que también dará apoyo al módulo Matrículas.
- Se preparó la estructura inicial para registrar prompts, resultados y evidencias.
- Después se desarrollarán los archivos base de materias y periodos.
- Se crearon los archivos iniciales del módulo Materias y periodos con funciones base y JSON vacíos.
- Se implementaron funciones de lectura y escritura JSON para materias y periodos.
- Se implementaron validaciones básicas para materias.
- Se agregó generación automática de códigos de materia.
- Se completó el registro y listado básico de materias.
- Se completó la búsqueda y actualización de materias.
- Se completó la gestión básica de periodos académicos.
