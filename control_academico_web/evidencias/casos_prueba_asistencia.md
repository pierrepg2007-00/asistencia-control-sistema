# Casos de prueba - Módulo Asistencia

## Datos del estudiante

- Estudiante asociado: Integrante 4
- Módulo principal: Asistencia
- Responsabilidad adicional: apoyo al módulo Matrículas

## Tabla de casos de prueba

| N° | Acción realizada | Datos de entrada | Resultado esperado | Resultado obtenido | Observación |
|---|---|---|---|---|---|
| 1 | Registrar asistencia correctamente | `codigo_estudiante: EST001, codigo_materia: MAT001, codigo_periodo: 2026-I, fecha: 2026-06-24, estado: presente` | Asistencia registrada correctamente. | Pendiente de ejecución. | Requiere estudiante matriculado en data/matriculas.json |
| 2 | Registrar asistencia con estudiante vacío | `codigo_estudiante: "", codigo_materia: MAT001, codigo_periodo: 2026-I, fecha: 2026-06-24, estado: presente` | Error: "El código de estudiante no puede estar vacío." | Pendiente de ejecución. | Validación básica de campo obligatorio. |
| 3 | Registrar asistencia con materia vacía | `codigo_estudiante: EST001, codigo_materia: "", codigo_periodo: 2026-I, fecha: 2026-06-24, estado: presente` | Error: "El código de materia no puede estar vacío." | Pendiente de ejecución. | Validación básica de campo obligatorio. |
| 4 | Registrar asistencia con periodo vacío | `codigo_estudiante: EST001, codigo_materia: MAT001, codigo_periodo: "", fecha: 2026-06-24, estado: presente` | Error: "El código de periodo no puede estar vacío." | Pendiente de ejecución. | Validación básica de campo obligatorio. |
| 5 | Registrar asistencia con fecha vacía | `codigo_estudiante: EST001, codigo_materia: MAT001, codigo_periodo: 2026-I, fecha: "", estado: presente` | Error: "La fecha no puede estar vacía." | Pendiente de ejecución. | Validación básica de campo obligatorio. |
| 6 | Registrar asistencia con fecha inválida | `codigo_estudiante: EST001, codigo_materia: MAT001, codigo_periodo: 2026-I, fecha: 24-06-2026, estado: presente` | Error: "La fecha debe tener el formato YYYY-MM-DD." | Pendiente de ejecución. | Se usa datetime.strptime para validar. |
| 7 | Registrar asistencia con estado inválido | `codigo_estudiante: EST001, codigo_materia: MAT001, codigo_periodo: 2026-I, fecha: 2026-06-24, estado: ausente` | Error: "El estado de asistencia debe ser: presente, tarde, falta o justificado." | Pendiente de ejecución. | Solo se aceptan 4 estados definidos. |
| 8 | Registrar asistencia de estudiante no matriculado | `codigo_estudiante: EST999, codigo_materia: MAT001, codigo_periodo: 2026-I, fecha: 2026-06-24, estado: presente` | Error: "El estudiante no está matriculado en esa materia y periodo." | Pendiente de ejecución. | Requiere que data/matriculas.json exista y no contenga al estudiante. |
| 9 | Registrar asistencia duplicada | Mismo estudiante, materia, periodo y fecha que un registro existente. | Error: "Ya existe una asistencia registrada para ese estudiante en esa fecha." | Pendiente de ejecución. | Verifica duplicados antes de guardar. |
| 10 | Listar asistencias registradas | Sin filtros. | Lista de todas las asistencias guardadas en data/asistencias.json. | Pendiente de ejecución. | Devuelve [] si no hay registros. |
| 11 | Listar asistencia por estudiante | `codigo_estudiante: EST001` | Solo asistencias de EST001. | Pendiente de ejecución. | Filtro por código de estudiante. |
| 12 | Listar asistencia por materia y periodo | `codigo_materia: MAT001, codigo_periodo: 2026-I` | Solo asistencias de MAT001 en 2026-I. | Pendiente de ejecución. | Filtro por materia y periodo. |
| 13 | Listar asistencia por materia, periodo y fecha | `codigo_materia: MAT001, codigo_periodo: 2026-I, fecha: 2026-06-24` | Solo asistencias de MAT001 en 2026-I del día 2026-06-24. | Pendiente de ejecución. | Filtro adicional por fecha. |
| 14 | Calcular porcentaje con asistencias y faltas | `codigo_estudiante: EST001, codigo_materia: MAT001, codigo_periodo: 2026-I`, con 3 presentes y 1 falta. | `total_clases: 4, asistencias: 3, faltas: 1, porcentaje: 75.0%` | Pendiente de ejecución. | Se cuentan presente, tarde y justificado como asistencia. |
| 15 | Calcular porcentaje cuando solo tiene faltas | `codigo_estudiante: EST001, codigo_materia: MAT001, codigo_periodo: 2026-I`, con 2 faltas. | `total_clases: 2, asistencias: 0, faltas: 2, porcentaje: 0%` | Pendiente de ejecución. | Porcentaje 0 si todas son faltas. |
| 16 | Calcular porcentaje cuando no hay registros | `codigo_estudiante: EST001, codigo_materia: MAT001, codigo_periodo: 2026-I`, sin asistencias. | `total_clases: 0, asistencias: 0, faltas: 0, porcentaje: 0%` | Pendiente de ejecución. | Sin registros, porcentaje 0. |
| 17 | Listar matriculados para tomar asistencia | `codigo_materia: MAT001, codigo_periodo: 2026-I` | Lista de estudiantes activos en MAT001, periodo 2026-I, con nombres y DNI si están disponibles. | Pendiente de ejecución. | Apoyo para saber a quiénes tomar asistencia. |

## Conclusión del módulo

El módulo de Asistencia quedó desarrollado con las siguientes capacidades:

- **Lectura y escritura JSON:** El módulo puede cargar y guardar asistencias en `data/asistencias.json`.
- **Validaciones:** Se validan estados de asistencia (presente, tarde, falta, justificado) y formato de fecha (YYYY-MM-DD).
- **Verificación de matrícula:** Antes de registrar asistencia, se verifica que el estudiante esté matriculado activamente en la materia y periodo.
- **Prevención de duplicados:** No se permite registrar dos veces la asistencia del mismo estudiante en la misma fecha, materia y periodo.
- **Registro completo:** La función `registrar_asistencia()` aplica todas las validaciones antes de guardar.
- **Consultas:** Se puede listar asistencias por estudiante, por materia/periodo y por fecha.
- **Cálculo de porcentaje:** Se calcula el porcentaje de asistencia considerando presente, tarde y justificado como asistencia, y falta como inasistencia.
- **Apoyo a matrículas:** La función `listar_matriculados_para_asistencia()` permite obtener los estudiantes que deben estar en clase, consultando `data/matriculas.json` y `data/estudiantes.json`.

### Estado de integración

El módulo asistencia está listo para integrarse con:

- **Matrículas:** Se validan matrículas antes de registrar asistencia.
- **Estudiantes:** Se consultan nombres y DNI al listar matriculados.
- **Materias y periodos:** Los códigos de materia y periodo son parte de todos los registros.
- **Reportes:** Las funciones de consulta y cálculo de porcentaje proveen los datos necesarios para generar reportes.

### Pendiente

- Integración completa con el frontend (conexión de `asistencia.js` con las funciones Python mediante un servidor).
- Ejecución de los 17 casos de prueba para verificar resultados reales.
