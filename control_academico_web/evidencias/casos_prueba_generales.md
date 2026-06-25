# Casos de prueba generales

| Caso | Módulo | Acción | Resultado esperado | Estado |
|---|---|---|---|---|
| 1 | Estudiantes | Registrar estudiante válido | El estudiante se guarda correctamente | Pendiente de ejecución |
| 2 | Estudiantes | Buscar estudiante existente | El sistema muestra sus datos | Pendiente de ejecución |
| 3 | Estudiantes | Actualizar estudiante existente | El sistema guarda los nuevos datos permitidos | Pendiente de ejecución |

## Casos agregados - Login y rutas protegidas

| Caso | Modulo | Accion | Resultado esperado | Estado |
|---|---|---|---|---|
| 4 | Login | Ingresar con `admin` y contrasena correcta | El sistema crea sesion y permite entrar al inicio | Ejecutado correctamente |
| 5 | Login | Ingresar con contrasena incorrecta | El sistema muestra error y no crea sesion | Ejecutado correctamente |
| 6 | Seguridad | Abrir `/` sin sesion | Redirige a `/login` | Ejecutado correctamente |
| 7 | Seguridad | Abrir rutas internas con sesion | Responden con codigo 200 | Ejecutado correctamente |
| 8 | Seguridad | Cerrar sesion | El sistema elimina la cookie y vuelve a `/login` | Ejecutado correctamente |
| 9 | Seguridad | Consumir API protegida sin sesion | Devuelve respuesta 401 | Ejecutado correctamente |
| 10 | Persistencia | Guardar estudiante con sesion iniciada | Se guarda en `data/estudiantes.json` | Ejecutado correctamente |
| 11 | Persistencia | Guardar materia, periodo, matricula, nota y asistencia | Se guardan en sus archivos JSON | Ejecutado correctamente |
| 12 | Visual | Revisar nueva interfaz | Login y paginas internas usan diseno distinto al anterior | Ejecutado correctamente |
