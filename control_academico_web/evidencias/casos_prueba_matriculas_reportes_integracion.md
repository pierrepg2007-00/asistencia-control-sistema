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
