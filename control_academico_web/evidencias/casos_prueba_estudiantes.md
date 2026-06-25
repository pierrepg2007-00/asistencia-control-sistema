# Casos de prueba - Módulo estudiantes

| N.º | Acción realizada | Datos de entrada | Resultado esperado | Resultado obtenido | Observación |
|---|---|---|---|---|---|
| 1 | Registrar estudiante correctamente | Nombres, apellidos, DNI válido, correo válido, estado activo | El estudiante se registra y se guarda en JSON | Pendiente de ejecución | Validar código automático |
| 2 | Registrar estudiante con nombres vacíos | Nombres vacío | El sistema muestra error y no guarda | Pendiente de ejecución | Validación obligatoria |
| 3 | Registrar estudiante con apellidos vacíos | Apellidos vacío | El sistema muestra error y no guarda | Pendiente de ejecución | Validación obligatoria |
| 4 | Registrar estudiante con DNI incompleto | DNI con menos de 8 dígitos | El sistema muestra error y no guarda | Pendiente de ejecución | Validar longitud |
| 5 | Registrar estudiante con DNI repetido | DNI ya existente | El sistema muestra error y no guarda | Pendiente de ejecución | Validar duplicados |
| 6 | Registrar estudiante con correo inválido | Correo sin `@` o sin punto | El sistema muestra error y no guarda | Pendiente de ejecución | Validación básica |
| 7 | Registrar estudiante con estado inválido | Estado diferente de activo o inactivo | El sistema muestra error y no guarda | Pendiente de ejecución | Validar estado |
| 8 | Listar estudiantes registrados | JSON con estudiantes | El sistema devuelve todos los estudiantes | Pendiente de ejecución | Validar lista |
| 9 | Buscar estudiante por código | Código existente, ejemplo `EST001` | El sistema devuelve el estudiante encontrado | Pendiente de ejecución | Buscar por código |
| 10 | Buscar estudiante por DNI | DNI existente | El sistema devuelve el estudiante encontrado | Pendiente de ejecución | Buscar por DNI |
| 11 | Buscar estudiante inexistente | Código o DNI no registrado | El sistema muestra mensaje de no encontrado | Pendiente de ejecución | Validar mensaje |
| 12 | Actualizar estudiante existente | Código existente y nuevos datos permitidos | El sistema actualiza nombres, apellidos, correo o estado | Pendiente de ejecución | No modificar DNI ni código |
| 13 | Intentar actualizar estudiante inexistente | Código no registrado | El sistema muestra mensaje de no existencia | Pendiente de ejecución | Validar búsqueda |
| 14 | Cambiar estado de activo a inactivo | Código existente y estado inactivo | El sistema guarda el nuevo estado | Pendiente de ejecución | Validar cambio de estado |

## Conclusión del módulo

El módulo estudiantes queda con funciones base listas para integrarse con los demás módulos. Falta realizar pruebas ejecutadas en un entorno integrado con la web y confirmar la conexión entre JavaScript y Python.
