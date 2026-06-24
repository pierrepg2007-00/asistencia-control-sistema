# Evidencias del resultado

## Módulo de estudiantes

Archivos creados:

- `data/estudiantes.json`: inicia con una lista vacía (`[]`) para almacenar los estudiantes.
- `core/estudiantes.py`: contiene la estructura base y las funciones de carga, guardado, generación de código, registro, listado, búsqueda, actualización y validaciones.
- `web/estudiantes.html`: contiene la página HTML inicial del módulo.
- `static/estudiantes.js`: contiene el punto de partida para la interacción con JavaScript.

Se dejaron pendientes las funciones de registro, búsqueda y actualización para completarlas en una siguiente etapa.

## Funciones JSON listas

- `cargar_estudiantes()`: lee `data/estudiantes.json`, crea el archivo con una lista vacía si no existe, devuelve una lista vacía si está vacío o si ocurre un error de lectura.
- `guardar_estudiantes(estudiantes)`: guarda la lista recibida en `data/estudiantes.json` con sangría para mantener el JSON legible.

## Validaciones implementadas

- `validar_dni(dni)`: verifica que el DNI sea un texto de exactamente ocho dígitos numéricos.
- `validar_correo(correo)`: verifica de forma básica que el correo incluya `@` y un punto en el dominio.
- `dni_repetido(dni)`: revisa los estudiantes guardados y devuelve `True` si encuentra el DNI.
- `estudiante_existe(codigo)`: revisa los estudiantes guardados y devuelve `True` si encuentra el código.
