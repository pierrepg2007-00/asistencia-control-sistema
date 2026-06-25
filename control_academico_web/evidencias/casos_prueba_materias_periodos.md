# Casos de prueba - Materias y periodos

| N.º | Módulo | Acción realizada | Datos de entrada | Resultado esperado | Resultado obtenido | Observación |
|---|---|---|---|---|---|---|
| 1 | Materias | Registrar materia correctamente | Nombre, docente, ciclo válido y estado activo | La materia se registra en JSON | Pendiente de ejecución | Validar código `MAT001` |
| 2 | Materias | Registrar materia con nombre vacío | Nombre vacío | El sistema muestra error y no guarda | Pendiente de ejecución | Campo obligatorio |
| 3 | Materias | Registrar materia con docente vacío | Docente vacío | El sistema muestra error y no guarda | Pendiente de ejecución | Campo obligatorio |
| 4 | Materias | Registrar materia con ciclo inválido | Ciclo vacío, texto o menor que 1 | El sistema muestra error y no guarda | Pendiente de ejecución | Validar número entero |
| 5 | Materias | Registrar materia con estado inválido | Estado diferente de activo o inactivo | El sistema muestra error y no guarda | Pendiente de ejecución | Validar estado |
| 6 | Materias | Listar materias registradas | JSON con materias | El sistema devuelve todas las materias | Pendiente de ejecución | Validar listado |
| 7 | Materias | Buscar materia por código existente | Código `MAT001` | El sistema devuelve la materia | Pendiente de ejecución | Buscar por código |
| 8 | Materias | Buscar materia inexistente | Código no registrado | El sistema muestra mensaje de no encontrado | Pendiente de ejecución | Validar mensaje |
| 9 | Materias | Actualizar materia existente | Código existente y datos permitidos | El sistema actualiza nombre, docente, ciclo o estado | Pendiente de ejecución | No modificar código |
| 10 | Materias | Intentar actualizar materia inexistente | Código no registrado | El sistema muestra mensaje de no existencia | Pendiente de ejecución | Validar búsqueda |
| 11 | Materias | Cambiar estado de materia de activo a inactivo | Materia existente y estado inactivo | El sistema guarda el nuevo estado | Pendiente de ejecución | Validar estado |
| 12 | Periodos | Registrar periodo correctamente | Código, año, nombre y estado válido | El periodo se registra en JSON | Pendiente de ejecución | Validar código como `2026-I` |
| 13 | Periodos | Registrar periodo con año inválido | Año vacío o texto | El sistema muestra error y no guarda | Pendiente de ejecución | Validar número |
| 14 | Periodos | Registrar periodo con nombre vacío | Nombre vacío | El sistema muestra error y no guarda | Pendiente de ejecución | Campo obligatorio |
| 15 | Periodos | Registrar periodo con estado inválido | Estado diferente de activo o cerrado | El sistema muestra error y no guarda | Pendiente de ejecución | Validar estado |
| 16 | Periodos | Registrar periodo repetido | Código ya registrado | El sistema muestra error y no guarda | Pendiente de ejecución | Validar duplicado |
| 17 | Periodos | Activar un periodo | Código existente | El periodo queda activo | Pendiente de ejecución | Usar `cambiar_periodo_activo()` |
| 18 | Periodos | Verificar que solo exista un periodo activo | Varios periodos | Solo un periodo queda activo y los demás cerrados | Pendiente de ejecución | Regla principal |
| 19 | Periodos | Buscar periodo existente | Código existente | El sistema devuelve el periodo | Pendiente de ejecución | Buscar por código |
| 20 | Periodos | Buscar periodo inexistente | Código no registrado | El sistema muestra mensaje de no encontrado | Pendiente de ejecución | Validar mensaje |
| 21 | Matrículas | Validar materia activa para matrícula | Materia activa | El sistema permite usarla en matrícula | Pendiente de ejecución | Apoyo a matrículas |
| 22 | Matrículas | Intentar validar materia inactiva para matrícula | Materia inactiva | El sistema no permite usarla | Pendiente de ejecución | Apoyo a matrículas |
| 23 | Matrículas | Validar periodo activo para matrícula | Periodo activo | El sistema permite usarlo en matrícula | Pendiente de ejecución | Apoyo a matrículas |
| 24 | Matrículas | Intentar validar periodo cerrado para matrícula | Periodo cerrado | El sistema no permite usarlo | Pendiente de ejecución | Apoyo a matrículas |

## Conclusión del módulo

El módulo Materias y periodos queda con funciones base listas para integrarse con Matrículas y con los demás módulos. Falta ejecutar los casos en una integración completa entre Python y la interfaz web.
