# Estudiante 1 - Evidencias de resultado

## Base general del proyecto

- Se revisó la estructura principal del proyecto `control_academico_web`.
- Se confirmó la existencia de las carpetas `data/`, `core/`, `web/`, `static/`, `evidencias/`, `reportes_generados/` y `prompts/`.
- Se creó `AGENTS.md` con reglas de desarrollo, estructura, módulos y definición de terminado.
- Se actualizó `README.md` con objetivo, módulos, tecnologías, estructura e integrantes.

## Pendiente después de la base

- Completar la lógica del módulo estudiantes.
- Organizar evidencias y prompts por estudiante.
- Agregar pruebas documentadas del módulo estudiantes.

## Organización de prompts y evidencias

- Se creó la estructura de archivos `prompts/estudiante_1_prompts.md` hasta `prompts/estudiante_5_prompts.md`.
- Se crearon evidencias por estudiante en la carpeta `evidencias/`.
- Se agregaron archivos generales de apoyo: `matriz_roles.md`, `bitacora_equipo.md`, `casos_prueba_generales.md` y `declaracion_uso_ia.md`.
- La evidencia del Integrante 1 queda centralizada en `evidencias/estudiante_1_evidencias_resultado.md`.

## Código automático de estudiante

- Se desarrolló `generar_codigo_estudiante()`.
- La función genera códigos con formato `EST001`, `EST002`, `EST003`.
- La función revisa los códigos ya guardados y evita repetirlos.
- Se ajustó la ruta del archivo JSON para que apunte a `control_academico_web/data/estudiantes.json`.
- Archivo modificado: `core/estudiantes.py`.

## Registro de estudiantes

- Se desarrolló `registrar_estudiante(nombres, apellidos, dni, correo, estado)`.
- Se validan nombres, apellidos, DNI, DNI repetido, correo y estado.
- El estudiante se guarda con código, nombres, apellidos, DNI, correo y estado.
- La función devuelve resultado, mensaje y datos del estudiante registrado.
- Archivo modificado: `core/estudiantes.py`.

## Listado y búsqueda de estudiantes

- `listar_estudiantes()` devuelve todos los estudiantes guardados en el JSON.
- `buscar_estudiante(valor)` permite buscar por código o DNI.
- La búsqueda devuelve un mensaje claro si encuentra o no encuentra resultados.
- Archivo modificado: `core/estudiantes.py`.

## Actualización de estudiantes

- Se desarrolló `actualizar_estudiante(codigo, nuevos_datos)`.
- La función permite modificar `nombres`, `apellidos`, `correo` y `estado`.
- La función protege `codigo` y `dni`, por lo que no los modifica.
- Se validan campos vacíos, correo y estado antes de guardar.
- Archivo modificado: `core/estudiantes.py`.

## Interfaz web de estudiantes

- Se desarrolló `web/estudiantes.html`.
- La página contiene título, formulario de registro, sección de búsqueda, tabla de estudiantes y zona de mensajes.
- Se usaron identificadores claros para conectar luego con `static/estudiantes.js`.
- Falta integrar la página con el servidor Python.
