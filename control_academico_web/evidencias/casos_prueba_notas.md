# Casos de prueba del módulo Notas

## Datos de la prueba

- Integrante: Integrante 3
- Módulo: Notas
- Fecha de documentación: 2026-06-24
- Archivos verificados: `core/notas.py`, `static/notas.js`

## Tabla de casos de prueba

| # | Acción realizada | Datos de entrada | Resultado esperado | Resultado obtenido | Observación |
| -- | ----------------- | ---------------- | ------------------ | ----------------- | ----------- |
| 1 | Registrar nota correctamente | `EST001`, `MAT101`, `PER2026A`, `15`, `14`, `16` | `resultado: True`, `mensaje: "Nota registrada correctamente."`, promedio 15.0, `estado_final: "aprobado"` | `resultado: True`, `mensaje: "Nota registrada correctamente."`, promedio 15.0, `estado_final: "aprobado"` | Requiere matrícula activa previa. |
| 2 | Registrar nota con estudiante vacío | `""`, `MAT101`, `PER2026A`, `15`, `14`, `16` | `resultado: False`, `mensaje: "El código de estudiante no puede estar vacío."` | Coincide con lo esperado. | Validación temprana sin consultar JSON. |
| 3 | Registrar nota con materia vacía | `EST001`, `""`, `PER2026A`, `15`, `14`, `16` | `resultado: False`, `mensaje: "El código de materia no puede estar vacío."` | Coincide con lo esperado. | Validación temprana sin consultar JSON. |
| 4 | Registrar nota con periodo vacío | `EST001`, `MAT101`, `""`, `15`, `14`, `16` | `resultado: False`, `mensaje: "El código de periodo no puede estar vacío."` | Coincide con lo esperado. | Validación temprana sin consultar JSON. |
| 5 | Registrar nota menor a 0 | `EST001`, `MAT101`, `PER2026A`, `-5`, `14`, `16` | `resultado: False`, `mensaje: "Las notas deben ser números entre 0 y 20."` | Coincide con lo esperado. | `validar_nota` rechaza valores negativos. |
| 6 | Registrar nota mayor a 20 | `EST001`, `MAT101`, `PER2026A`, `15`, `25`, `16` | `resultado: False`, `mensaje: "Las notas deben ser números entre 0 y 20."` | Coincide con lo esperado. | `validar_nota` rechaza valores >20. |
| 7 | Registrar nota con texto en vez de número | `EST001`, `MAT101`, `PER2026A`, `"abc"`, `14`, `16` | `resultado: False`, `mensaje: "Las notas deben ser números entre 0 y 20."` | Coincide con lo esperado. | El `float()` falla con texto no numérico. |
| 8 | Registrar nota de estudiante no matriculado | `EST999`, `MAT101`, `PER2026A`, `15`, `14`, `16` | `resultado: False`, `mensaje: "El estudiante no está matriculado en esa materia y periodo."` | Coincide con lo esperado. | `verificar_matricula_para_nota` busca en `matriculas.json`. |
| 9 | Registrar nota duplicada para el mismo estudiante, materia y periodo | `EST001`, `MAT101`, `PER2026A`, `12`, `13`, `14` (segunda vez) | `resultado: False`, `mensaje: "Ya existe una nota registrada para esa matrícula."` | Coincide con lo esperado. | `nota_existe` evita duplicados. |
| 10 | Calcular promedio aprobado | `nota1=15`, `nota2=14`, `nota3=16` | `promedio=15.0`, `estado_final="aprobado"` | Coincide con lo esperado. | Promedio ≥ 11 aprueba. |
| 11 | Calcular promedio desaprobado | `nota1=8`, `nota2=9`, `nota3=10` | `promedio=9.0`, `estado_final="desaprobado"` | Coincide con lo esperado. | Promedio < 11 desaprueba. |
| 12 | Listar notas registradas | Sin filtros | Devuelve todas las notas en `notas.json`. | Coincide con lo esperado. | `listar_notas()` retorna la lista completa. |
| 13 | Listar notas por estudiante | `codigo_estudiante="EST001"` | Solo notas de EST001. | Coincide con lo esperado. | `listar_notas_por_estudiante()` filtra correctamente. |
| 14 | Listar notas por materia y periodo | `codigo_materia="MAT101"`, `codigo_periodo="PER2026A"` | Solo notas de MAT101 en PER2026A. | Coincide con lo esperado. | `listar_notas_por_materia()` filtra por ambos campos. |
| 15 | Actualizar notas existentes | `EST001`, `MAT101`, `PER2026A`, `notas: {nota1: 18, nota2: 17, nota3: 19}` | `resultado: True`, `mensaje: "Nota actualizada correctamente."`, promedio 18.0, `estado_final: "aprobado"` | Coincide con lo esperado. | Recalcula promedio y estado automáticamente. |
| 16 | Intentar actualizar nota inexistente | `EST999`, `MAT101`, `PER2026A`, `notas: {nota1: 15, nota2: 14, nota3: 16}` | `resultado: False`, `mensaje: "No existe una nota para ese estudiante, materia y periodo."` | Coincide con lo esperado. | No crea registros nuevos; solo actualiza existentes. |
| 17 | Verificar estudiantes matriculados sin nota | `codigo_materia="MAT101"`, `codigo_periodo="PER2026A"` | Estudiantes con matrícula activa en MAT101/PER2026A que no tengan nota registrada. | Coincide con lo esperado. | `listar_estudiantes_sin_nota()` cruza `matriculas.json`, `notas.json` y `estudiantes.json`. |

## Resultados de validación visual (JavaScript)

| # | Acción realizada | Datos de entrada | Resultado esperado | Resultado obtenido | Observación |
| -- | ----------------- | ---------------- | ------------------ | ----------------- | ----------- |
| V1 | Validar formulario con todos los campos | Códigos y notas válidos | Sin error, nota agregada a `notasTemporales`. | Funciona correctamente. | La validación JS es independiente de Python. |
| V2 | Validar formulario con campos vacíos | Código de estudiante vacío | Mensaje: "Ingrese el código de estudiante." | Funciona correctamente. | Validación del lado del cliente. |
| V3 | Validar formulario con nota fuera de rango | Nota = -1 | Mensaje: "Las notas deben ser números entre 0 y 20." | Funciona correctamente. | JS también valida rango 0-20. |
| V4 | Filtrar por estudiante | Código existente en `notasTemporales` | Muestra solo notas del estudiante. | Funciona correctamente. | Filtro visual sin backend. |
| V5 | Filtrar por materia y periodo | Códigos existentes en `notasTemporales` | Muestra solo notas de esa materia/periodo. | Funciona correctamente. | Filtro visual sin backend. |
| V6 | Preparar actualización visual | Click en botón "Editar" | Carga los datos en el formulario. | Funciona correctamente. | Solo carga visual; la persistencia depende de Python. |

## Conclusión del módulo

El módulo de notas quedó listo para integrarse con matrículas, estudiantes, materias y reportes.

- **Integración con matrículas:** La función `verificar_matricula_para_nota` consulta `matriculas.json` y valida matrícula activa antes de registrar notas. La función `listar_estudiantes_sin_nota` cruza matrículas con notas para identificar pendientes.
- **Integración con estudiantes:** `listar_estudiantes_sin_nota` consulta opcionalmente `estudiantes.json` para mostrar nombres.
- **Integración con materias:** Las funciones de listado y registro usan `codigo_materia` y `codigo_periodo` como claves de relación.
- **Integración con reportes:** Las funciones `listar_notas`, `listar_notas_por_estudiante` y `listar_notas_por_materia` entregan datos listos para ser consumidos por el módulo de reportes.
- **Pendiente:** Conectar `static/notas.js` con `core/notas.py` mediante un servidor web (Flask, FastAPI o similar) para que las operaciones del frontend persistan en los archivos JSON.
