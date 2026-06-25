# Casos de prueba - Matrículas, Reportes e Integración

## Datos del estudiante
- Estudiante asociado: Integrante 5
- Módulo principal: Reportes e integración
- Responsabilidad adicional: Matrículas

## Casos de prueba

### Matrículas

| N° | Módulo | Acción realizada | Datos de entrada | Resultado esperado | Resultado obtenido | Observación |
|---|---|---|---|---|---|---|---|
| 1 | Matrículas | Registrar matrícula correctamente | EST001, MAT001, 2026-I | Matrícula registrada con estado activa | Pendiente de ejecución | Requiere datos de prueba |
| 2 | Matrículas | Registrar matrícula con estudiante vacío | "", MAT001, 2026-I | Mensaje: código de estudiante vacío | Pendiente de ejecución | Validación de campos |
| 3 | Matrículas | Registrar matrícula con materia vacía | EST001, "", 2026-I | Mensaje: código de materia vacío | Pendiente de ejecución | Validación de campos |
| 4 | Matrículas | Registrar matrícula con periodo vacío | EST001, MAT001, "" | Mensaje: código de periodo vacío | Pendiente de ejecución | Validación de campos |
| 5 | Matrículas | Registrar matrícula con estudiante inexistente | EST999, MAT001, 2026-I | Mensaje: estudiante no existe | Pendiente de ejecución | Validación de existencia |
| 6 | Matrículas | Registrar matrícula con estudiante inactivo | Estudiante inactivo | Mensaje: estudiante no está activo | Pendiente de ejecución | Validación de estado |
| 7 | Matrículas | Registrar matrícula con materia inexistente | EST001, MAT999, 2026-I | Mensaje: materia no existe | Pendiente de ejecución | Validación de existencia |
| 8 | Matrículas | Registrar matrícula con materia inactiva | Materia inactiva | Mensaje: materia no está activa | Pendiente de ejecución | Validación de estado |
| 9 | Matrículas | Registrar matrícula con periodo inexistente | EST001, MAT001, 2099-X | Mensaje: periodo no existe | Pendiente de ejecución | Validación de existencia |
| 10 | Matrículas | Registrar matrícula con periodo cerrado | Periodo cerrado | Mensaje: periodo no está activo | Pendiente de ejecución | Validación de estado |
| 11 | Matrículas | Registrar matrícula duplicada | Matrícula ya existente | Mensaje: matrícula ya existe | Pendiente de ejecución | Validación de duplicados |
| 12 | Matrículas | Listar matrículas registradas | Sin parámetros | Lista de todas las matrículas | Pendiente de ejecución | Función listar_matriculas() |
| 13 | Matrículas | Buscar matrícula existente | EST001, MAT001, 2026-I | Datos de la matrícula | Pendiente de ejecución | Función buscar_matricula() |
| 14 | Matrículas | Buscar matrícula inexistente | EST999, MAT999, 2099-X | Mensaje: no encontrada | Pendiente de ejecución | Búsqueda sin resultados |
| 15 | Matrículas | Cambiar estado de matrícula | EST001, MAT001, 2026-I, retirada | Estado actualizado a retirada | Pendiente de ejecución | Función cambiar_estado_matricula() |

### Reportes

| N° | Módulo | Acción realizada | Datos de entrada | Resultado esperado | Resultado obtenido | Observación |
|---|---|---|---|---|---|---|
| 16 | Reportes | Reporte de estudiantes por materia | MAT001, 2026-I | Lista de estudiantes matriculados | Pendiente de ejecución | Función reporte_estudiantes_por_materia() |
| 17 | Reportes | Reporte de notas por materia | MAT001, 2026-I | Detalle de notas, aprobados, desaprobados, promedio | Pendiente de ejecución | Función reporte_notas_por_materia() |
| 18 | Reportes | Reporte de asistencia por materia | MAT001, 2026-I | Resumen de asistencia por estudiante | Pendiente de ejecución | Función reporte_asistencia_por_materia() |
| 19 | Reportes | Reporte de estudiantes en riesgo | Sin parámetros | Lista de estudiantes con nota baja o asistencia baja | Pendiente de ejecución | Función reporte_estudiantes_en_riesgo() |
| 20 | Reportes | Exportar reporte en texto | "reporte_notas", datos | Archivo .txt generado en reportes_generados/ | Pendiente de ejecución | Función exportar_reporte_txt() |
| 21 | Reportes | Generar reporte sin datos | Materia sin registros | Lista vacía o mensaje claro | Pendiente de ejecución | Manejo de datos vacíos |

### Integración

| N° | Módulo | Acción realizada | Datos de entrada | Resultado esperado | Resultado obtenido | Observación |
|---|---|---|---|---|---|---|
| 22 | Integración | Abrir página principal | http://localhost:8000/web/index.html | Página principal con menú | Pendiente de ejecución | Navegación del sistema |
| 23 | Integración | Navegar a estudiantes | Click en enlace | Página estudiantes.html | Pendiente de ejecución | Enlace funcional |
| 24 | Integración | Navegar a materias | Click en enlace | Página materias.html | Pendiente de ejecución | Enlace funcional |
| 25 | Integración | Navegar a matrículas | Click en enlace | Página matriculas.html | Pendiente de ejecución | Enlace funcional |
| 26 | Integración | Navegar a notas | Click en enlace | Página notas.html | Pendiente de ejecución | Enlace funcional |
| 27 | Integración | Navegar a asistencia | Click en enlace | Página asistencia.html | Pendiente de ejecución | Enlace funcional |
| 28 | Integración | Navegar a reportes | Click en enlace | Página reportes.html | Pendiente de ejecución | Enlace funcional |
| 29 | Integración | Ejecutar servidor local | python server.py | Servidor iniciado en puerto 8000 | Pendiente de ejecución | Levantamiento del sistema |
| 30 | Integración | Verificar persistencia de datos | Reiniciar servidor | Datos JSON no se borran | Pendiente de ejecución | Los datos persisten en archivos |

## Conclusión del módulo

Los módulos de matrículas y reportes quedaron con su lógica Python completa y las páginas web preparadas. La integración básica está lista con el servidor simple y la página principal con enlaces a los 6 módulos.

Falta la conexión entre el frontend (HTML/JavaScript) y el backend (Python) para que las páginas consuman las funciones de core/. Esto se realizará en una etapa posterior de integración completa del proyecto.

## Casos de prueba agregados - Correccion general de integracion

| N° | Modulo | Accion realizada | Datos de entrada | Resultado esperado | Resultado obtenido | Observacion |
|---|---|---|---|---|---|---|
| 31 | Navegacion | Abrir ruta principal | `http://localhost:8000/` | Muestra inicio | Correcto, HTTP 200 | Ruta corregida |
| 32 | Navegacion | Abrir rutas de modulos | `/index`, `/estudiantes`, `/materias`, `/matriculas`, `/notas`, `/asistencia`, `/reportes` | Todas responden | Correcto, HTTP 200 | Barra comun agregada |
| 33 | Archivos estaticos | Cargar CSS y JS | `/static/styles.css`, `/static/estudiantes.js` | Archivos servidos | Correcto, HTTP 200 | Servidor sirve `static/` |
| 34 | Estudiantes | Guardar desde API/formulario | Prueba Integracion, DNI 12345678 | Guarda en JSON | Correcto, registro en `data/estudiantes.json` | Flujo JS -> server.py -> core -> JSON |
| 35 | Materias | Guardar desde API/formulario | Integracion Web, Docente Prueba | Guarda en JSON | Correcto, registro en `data/materias.json` | Codigo generado MAT001 |
| 36 | Periodos | Guardar periodo activo | 2026-I, 2026, Periodo Integracion | Guarda activo | Correcto, registro en `data/periodos.json` | Periodo activo disponible |
| 37 | Matriculas | Registrar matricula | EST001, MAT001, 2026-I | Guarda matricula activa | Correcto, registro en `data/matriculas.json` | Estado guardado como activa |
| 38 | Notas | Registrar nota | EST001, MAT001, 2026-I, 14, 15, 16 | Guarda nota y promedio | Correcto, registro en `data/notas.json` | Promedio 15.0 |
| 39 | Asistencia | Registrar asistencia | EST001, MAT001, 2026-I, 2026-06-25, presente | Guarda asistencia | Correcto, registro en `data/asistencias.json` | Porcentaje calculable |
| 40 | Reportes | Generar estudiantes por materia | MAT001, 2026-I | Muestra estudiante matriculado | Correcto, devuelve EST001 | Reporte visible en pantalla |
| 41 | Reportes | Generar notas por materia | MAT001, 2026-I | Muestra detalle y resumen | Correcto, total 1, aprobado 1 | Reporte visible en pantalla |
| 42 | Reportes | Generar asistencia por materia | MAT001, 2026-I | Muestra porcentaje | Correcto, asistencia 100% | Reporte visible en pantalla |
| 43 | Reportes | Generar estudiantes en riesgo | Sin datos | Lista o vacio controlado | Correcto, devuelve lista vacia | Sin error |
| 44 | Exportacion | Exportar TXT | reporte_integracion_prueba | Archivo TXT generado | Correcto, archivo en `reportes_generados/` | Exportacion verificada |

## Conclusion de la correccion general

La etapa de integracion completa quedo conectada con rutas del servidor, navegacion uniforme, APIs JSON, botones con `fetch`, guardado real en archivos JSON, reportes en pantalla y exportacion TXT.
