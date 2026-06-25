# Estudiante 5 - Prompts utilizados

## Datos del estudiante
- Estudiante asociado: Integrante 5
- Módulo principal: Reportes e integración
- Responsabilidad adicional: Matrículas

## Prompts usados

Cada prompt debe registrarse con este formato:

### Prompt N - Título del prompt
**Estudiante asociado:** Integrante 5
**Módulo trabajado:** Reportes / Integración / Matrículas
**Objetivo:** objetivo breve del prompt

Aquí se pega el prompt completo utilizado.

---

### Prompt 1 - Preparar evidencias del Integrante 5
**Estudiante asociado:** Integrante 5
**Módulo trabajado:** Reportes e integración
**Objetivo:** Revisar y preparar archivos de prompts y evidencias

```text
Trabaja como agente de desarrollo dentro del proyecto control_academico_web.

Este trabajo corresponde al Integrante 5.
Módulo principal: Reportes e integración.
Responsabilidad adicional: módulo Matrículas.

Antes de modificar archivos, revisa:
- AGENTS.md
- README.md
- estructura actual del proyecto
- prompts/estudiante_5_prompts.md
- evidencias/estudiante_5_evidencias_resultado.md

No borres archivos existentes.
No modifiques de forma innecesaria los módulos ya trabajados por otros integrantes.
No reemplaces archivos completos si solo necesitas agregar algo pequeño.

Primero asegúrate de que existan estos archivos:

- prompts/estudiante_5_prompts.md
- evidencias/estudiante_5_evidencias_resultado.md

Si no existen, créalos.

El archivo prompts/estudiante_5_prompts.md debe tener esta estructura:

# Estudiante 5 - Prompts utilizados

## Datos del estudiante
- Estudiante asociado: Integrante 5
- Módulo principal: Reportes e integración
- Responsabilidad adicional: Matrículas

## Prompts usados

Cada prompt debe registrarse con este formato:

### Prompt N - Título del prompt
**Estudiante asociado:** Integrante 5
**Módulo trabajado:** Reportes / Integración / Matrículas
**Objetivo:** objetivo breve del prompt

Aquí se pega el prompt completo utilizado.

El archivo evidencias/estudiante_5_evidencias_resultado.md debe tener esta estructura:

# Estudiante 5 - Evidencias de resultado

## Datos del estudiante
- Estudiante asociado: Integrante 5
- Módulo principal: Reportes e integración
- Responsabilidad adicional: Matrículas

## Resultados obtenidos

| N° | Actividad realizada | Resultado entregado por la IA | Cambios realizados manualmente | Archivo creado o modificado | Observación final |
|---|---|---|---|---|---|

## Conversación o resumen de interacción con IA

Al terminar, guarda este prompt completo en:
prompts/estudiante_5_prompts.md

Luego actualiza:
evidencias/estudiante_5_evidencias_resultado.md

Indicando:
- qué archivos de prompts y evidencias se revisaron o crearon
- qué estructura quedó preparada para el Integrante 5
- qué se desarrollará después

Finalmente revisa los cambios y deja todo listo para commit.
```

---

### Prompt 2 - Crear base de matriculas y reportes
**Estudiante asociado:** Integrante 5
**Módulo trabajado:** Matrículas / Reportes
**Objetivo:** Crear archivos base para los módulos matrículas y reportes

```text
Continúa con el proyecto control_academico_web.

Este trabajo corresponde al Integrante 5.
Módulo principal: Reportes e integración.
Responsabilidad adicional: Matrículas.

Crea únicamente los archivos necesarios para empezar el módulo matrículas y reportes:

- data/matriculas.json
- core/matriculas.py
- core/reportes.py
- web/matriculas.html
- web/reportes.html
- static/matriculas.js
- static/reportes.js

El archivo data/matriculas.json debe iniciar con una lista vacía [].

En core/matriculas.py deja preparada la estructura base con estas funciones:

- cargar_matriculas()
- guardar_matriculas(matriculas)
- validar_estudiante_para_matricula(codigo_estudiante)
- validar_materia_para_matricula(codigo_materia)
- validar_periodo_para_matricula(codigo_periodo)
- matricula_existe(codigo_estudiante, codigo_materia, codigo_periodo)
- registrar_matricula(codigo_estudiante, codigo_materia, codigo_periodo)
- listar_matriculas()
- buscar_matricula(codigo_estudiante, codigo_materia, codigo_periodo)
- listar_matriculas_por_estudiante(codigo_estudiante)
- listar_matriculas_por_materia(codigo_materia, codigo_periodo)
- cambiar_estado_matricula(codigo_estudiante, codigo_materia, codigo_periodo, nuevo_estado)

En core/reportes.py deja preparada la estructura base con estas funciones:

- reporte_estudiantes_por_materia(codigo_materia, codigo_periodo)
- reporte_notas_por_materia(codigo_materia, codigo_periodo)
- reporte_asistencia_por_materia(codigo_materia, codigo_periodo)
- reporte_estudiantes_en_riesgo()
- exportar_reporte_txt(nombre_reporte, datos)

Por ahora algunas funciones pueden quedar como borrador, pero deben estar ordenadas y con comentarios simples.

No modifiques los módulos de estudiantes, materias, periodos, notas ni asistencia, salvo que sea estrictamente necesario para importar o consultar datos.

Al terminar, guarda este prompt completo en:
prompts/estudiante_5_prompts.md

Luego actualiza:
evidencias/estudiante_5_evidencias_resultado.md

Indicando:
- qué archivos se crearon
- qué funciones quedaron preparadas
- qué falta desarrollar

Finalmente revisa los cambios y deja todo listo para commit.
```


### Prompt 3 - Agregar lectura y guardado de matriculas
**Estudiante asociado:** Integrante 5
**Módulo trabajado:** Matrículas
**Objetivo:** Implementar cargar_matriculas() y guardar_matriculas() con manejo de archivos JSON

```text
Continúa con el módulo matrículas.

Este trabajo corresponde al Integrante 5.
Responsabilidad adicional: Matrículas.

Desarrolla en core/matriculas.py las funciones para leer y guardar matrículas usando JSON:

- cargar_matriculas()
- guardar_matriculas(matriculas)

Reglas para cargar_matriculas():

- debe leer data/matriculas.json
- si el archivo no existe, debe crearlo con []
- si el archivo está vacío, debe devolver []
- si ocurre un error al leer, debe devolver []
- no debe romper el programa

Reglas para guardar_matriculas(matriculas):

- debe recibir una lista de matrículas
- debe guardar esa lista en data/matriculas.json
- el JSON debe quedar ordenado y legible

Usa Python básico.
Usa solo librerías estándar como json y os si hace falta.

No modifiques otros módulos.

Al terminar, guarda este prompt completo en:
prompts/estudiante_5_prompts.md

Luego actualiza:
evidencias/estudiante_5_evidencias_resultado.md

Indicando:
- qué funciones se desarrollaron
- qué validaciones de archivo se agregaron
- qué archivo fue modificado

Finalmente revisa los cambios y deja todo listo para commit.
```

---

### Prompt 4 - Agregar validaciones de matriculas
**Estudiante asociado:** Integrante 5
**Módulo trabajado:** Matrículas
**Objetivo:** Implementar validaciones de estudiante, materia, periodo y duplicados

```text
[Prompt 4 registrado - validaciones de matriculas]
```


### Prompt 5 - Registrar matriculas con validaciones
**Estudiante asociado:** Integrante 5
**Módulo trabajado:** Matrículas
**Objetivo:** Implementar registrar_matricula() con todas las validaciones

```text
[Prompt 5 registrado - registrar matriculas]
```


---

### Prompt de corrección general - Rutas, navegación, guardado JSON e interfaz
**Estudiante asociado:** Integrante 5
**Módulo trabajado:** Reportes / Integración / Matrículas
**Objetivo:** Corregir rutas, navegacion, API JSON, conexion de botones, guardado real en JSON, interfaz y evidencias

```text
Necesito corregir la integración general del proyecto control_academico_web.

Actualmente el sistema ya tiene módulos y páginas, pero hay problemas importantes:

1. Las páginas no siguen bien las rutas.
2. Falta una barra de navegación visible para moverse entre módulos.
3. Al presionar botones como “Guardar”, no se están guardando los datos en los archivos JSON.
4. Algunos módulos comparten funciones y la pantalla debería separar mejor las acciones con botones claros.
5. La parte visual del sistema necesita ordenarse para que parezca una web académica sencilla y uniforme.

IMPORTANTE:
- No borres archivos existentes.
- No reemplaces módulos completos si solo necesitas corregir integración.
- No modifiques datos ya existentes en los JSON, salvo que sea necesario para probar.
- No uses frameworks.
- Mantén Python, HTML, CSS, JavaScript básico y JSON.
- No subas ni modifiques users-tokens.txt.
- No rompas el trabajo de los integrantes anteriores.
- El código debe seguir siendo entendible para estudiantes principiantes.

Primero revisa el estado del proyecto:

- server.py
- web/index.html
- web/estudiantes.html
- web/materias.html
- web/matriculas.html
- web/notas.html
- web/asistencia.html
- web/reportes.html
- static/styles.css
- static/estudiantes.js
- static/materias.js
- static/matriculas.js
- static/notas.js
- static/asistencia.js
- static/reportes.js
- core/estudiantes.py
- core/materias.py
- core/periodos.py
- core/matriculas.py
- core/notas.py
- core/asistencia.py
- core/reportes.py

Luego realiza estas correcciones:

------------------------------------------------------------
1. CORREGIR RUTAS DEL SISTEMA
------------------------------------------------------------

Corrige server.py para que el sistema pueda abrir correctamente estas rutas:

- /
- /index
- /estudiantes
- /materias
- /matriculas
- /notas
- /asistencia
- /reportes

Cada ruta debe mostrar su archivo HTML correspondiente:

- / o /index -> web/index.html
- /estudiantes -> web/estudiantes.html
- /materias -> web/materias.html
- /matriculas -> web/matriculas.html
- /notas -> web/notas.html
- /asistencia -> web/asistencia.html
- /reportes -> web/reportes.html

También debe servir correctamente archivos CSS y JS desde static/.

El sistema debe ejecutarse con:

python server.py

Y abrirse desde:

http://localhost:8000

------------------------------------------------------------
2. AGREGAR BARRA DE NAVEGACIÓN
------------------------------------------------------------

Agrega una barra de navegación en todas las páginas HTML:

- index.html
- estudiantes.html
- materias.html
- matriculas.html
- notas.html
- asistencia.html
- reportes.html

La barra debe tener enlaces a:

- Inicio
- Estudiantes
- Materias y periodos
- Matrículas
- Notas
- Asistencia
- Reportes

Los enlaces deben usar las rutas del servidor:

- /
- /estudiantes
- /materias
- /matriculas
- /notas
- /asistencia
- /reportes

La barra debe verse igual en todas las páginas.

------------------------------------------------------------
3. CONECTAR BOTONES CON PYTHON Y JSON
------------------------------------------------------------

Corrige server.py para agregar rutas API simples que reciban y devuelvan JSON.

Usa fetch desde JavaScript para conectar los formularios con Python.

Como mínimo deben funcionar estas acciones:

ESTUDIANTES:
- Guardar estudiante
- Listar estudiantes
- Buscar estudiante
- Actualizar estudiante

MATERIAS:
- Guardar materia
- Listar materias
- Buscar materia
- Actualizar materia

PERIODOS:
- Guardar periodo
- Listar periodos
- Buscar periodo
- Cambiar periodo activo

MATRÍCULAS:
- Registrar matrícula
- Listar matrículas
- Buscar matrícula
- Listar matrículas por estudiante
- Listar matrículas por materia
- Cambiar estado de matrícula

NOTAS:
- Registrar nota
- Listar notas
- Listar notas por estudiante
- Listar notas por materia
- Actualizar nota

ASISTENCIA:
- Registrar asistencia
- Listar asistencias
- Listar asistencia por estudiante
- Listar asistencia por materia
- Calcular porcentaje de asistencia

REPORTES:
- Reporte de estudiantes por materia
- Reporte de notas por materia
- Reporte de asistencia por materia
- Reporte de estudiantes en riesgo
- Exportar reporte TXT

Cada botón de la interfaz debe llamar a una función JavaScript.
Cada función JavaScript debe llamar a server.py mediante fetch.
server.py debe llamar a la función correspondiente del módulo en core/.
El módulo debe guardar o leer el archivo JSON correspondiente.

Ejemplo de flujo obligatorio:

Botón Guardar estudiante
-> static/estudiantes.js
-> fetch a server.py
-> core/estudiantes.py
-> data/estudiantes.json
-> respuesta JSON a la página

No basta con mostrar datos en pantalla.
Debe guardar realmente en el archivo JSON.

------------------------------------------------------------
4. SEPARAR BOTONES EN MÓDULOS QUE COMPARTEN FUNCIONES
------------------------------------------------------------

Corrige la interfaz para que los módulos que tienen varias funciones no estén mezclados.

En web/materias.html separa visualmente:

A. Sección Materias
- Guardar materia
- Listar materias
- Buscar materia
- Actualizar materia

B. Sección Periodos
- Guardar periodo
- Listar periodos
- Buscar periodo
- Cambiar periodo activo

Cada sección debe tener sus propios botones, campos y tabla si corresponde.

En web/matriculas.html separa visualmente:

A. Registro de matrícula
- Registrar matrícula

B. Consultas de matrícula
- Listar todas
- Buscar matrícula exacta
- Listar por estudiante
- Listar por materia y periodo

C. Estado de matrícula
- Cambiar estado

En web/notas.html separa visualmente:

A. Registro de notas
- Guardar nota

B. Consultas
- Listar todas
- Listar por estudiante
- Listar por materia y periodo

C. Actualización
- Actualizar nota

En web/asistencia.html separa visualmente:

A. Registro de asistencia
- Guardar asistencia

B. Consultas
- Listar todas
- Listar por estudiante
- Listar por materia y periodo

C. Indicadores
- Calcular porcentaje de asistencia

En web/reportes.html separa visualmente:

A. Reportes académicos
- Estudiantes por materia
- Notas por materia
- Asistencia por materia

B. Alertas
- Estudiantes en riesgo

C. Exportación
- Exportar reporte TXT

------------------------------------------------------------
5. CORREGIR LA PARTE VISUAL
------------------------------------------------------------

Actualiza static/styles.css para que el sistema tenga una apariencia uniforme y ordenada.

Debe incluir estilos para:

- barra de navegación
- contenedor principal
- tarjetas o secciones
- formularios
- inputs
- selects
- botones
- tablas
- mensajes de error
- mensajes de éxito
- títulos y subtítulos

El diseño debe ser simple, limpio y académico.
No uses librerías externas.
No uses diseños complicados.

Todas las páginas deben usar el mismo CSS.

------------------------------------------------------------
6. VERIFICAR GUARDADO REAL EN JSON
------------------------------------------------------------

Después de corregir la integración, realiza pruebas manuales mínimas:

1. Registrar un estudiante y verificar que aparece en data/estudiantes.json.
2. Registrar una materia y verificar data/materias.json.
3. Registrar un periodo activo y verificar data/periodos.json.
4. Registrar una matrícula y verificar data/matriculas.json.
5. Registrar una nota y verificar data/notas.json.
6. Registrar una asistencia y verificar data/asistencias.json.
7. Generar un reporte y verificar que se muestra en pantalla.
8. Exportar un reporte TXT y verificar que se guarde en reportes_generados/.

Si alguna acción no guarda en JSON, corrígela.

------------------------------------------------------------
7. ACTUALIZAR EVIDENCIAS Y PROMPTS
------------------------------------------------------------

Como esta corrección corresponde al Integrante 5 por integración general, guarda este prompt completo en:

prompts/estudiante_5_prompts.md

No borres los prompts anteriores.
Agrega este prompt como un nuevo registro con el título:

### Prompt de corrección general - Rutas, navegación, guardado JSON e interfaz

También actualiza:

evidencias/estudiante_5_evidencias_resultado.md

Indicando:

- qué rutas se corrigieron
- qué barra de navegación se agregó
- qué botones fueron conectados
- qué acciones ahora guardan en JSON
- qué pantallas se reorganizaron
- qué mejoras visuales se aplicaron
- qué pruebas manuales se hicieron

También actualiza:

evidencias/casos_prueba_matriculas_reportes_integracion.md

Agregando casos de prueba sobre:

- navegación entre páginas
- guardar datos desde formularios
- verificar cambios en JSON
- generar reportes
- exportar TXT

------------------------------------------------------------
8. COMMIT FINAL
------------------------------------------------------------

Al terminar, revisa:

git status

Luego haz commit con este mensaje:

git add .
git commit -m "fix: corregir rutas navegacion guardado json e interfaz"

No hagas push todavía.
Primero deja el repositorio limpio y confirma qué archivos fueron modificados.
```
### Prompt 6 - Listar y buscar matriculas
**Estudiante asociado:** Integrante 5
**Módulo trabajado:** Matrículas
**Objetivo:** Implementar listar_matriculas, buscar_matricula, listar por estudiante y por materia

```text
[Prompt 6 registrado - listar y buscar matriculas]
```


### Prompt 7 - Cambiar estado de matriculas
**Estudiante asociado:** Integrante 5
**Módulo trabajado:** Matrículas
**Objetivo:** Implementar cambiar_estado_matricula() con estados: activa, retirada, finalizada

```text
[Prompt 7 registrado - cambiar estado de matriculas]
```


### Prompt 8 - Reportar estudiantes por materia
**Estudiante asociado:** Integrante 5
**Módulo trabajado:** Reportes
**Objetivo:** Implementar reporte_estudiantes_por_materia() consultando matriculas, estudiantes y materias

```text
[Prompt 8 registrado - reportar estudiantes por materia]
```


### Prompt 9 - Reportar notas por materia
**Estudiante asociado:** Integrante 5
**Módulo trabajado:** Reportes
**Objetivo:** Implementar reporte_notas_por_materia() con cálculos de aprobados, desaprobados y promedio

```text
[Prompt 9 registrado - reportar notas por materia]
```


### Prompt 10 - Reportar asistencia por materia
**Estudiante asociado:** Integrante 5
**Módulo trabajado:** Reportes
**Objetivo:** Implementar reporte_asistencia_por_materia() con conteo y porcentaje

```text
[Prompt 10 registrado - reportar asistencia por materia]
```


### Prompt 11 - Reportar estudiantes en riesgo
**Estudiante asociado:** Integrante 5
**Módulo trabajado:** Reportes
**Objetivo:** Implementar reporte_estudiantes_en_riesgo() con criterios de nota baja y asistencia

```text
[Prompt 11 registrado - reportar estudiantes en riesgo]
```


### Prompt 12 - Exportar reportes en texto
**Estudiante asociado:** Integrante 5
**Módulo trabajado:** Reportes
**Objetivo:** Implementar exportar_reporte_txt() para generar archivos .txt

```text
[Prompt 12 registrado - exportar reportes en texto]
```


### Prompt 13 - Crear interfaz web de matriculas
**Estudiante asociado:** Integrante 5
**Módulo trabajado:** Matrículas
**Objetivo:** Desarrollar la página web/matriculas.html completa

```text
[Prompt 13 registrado - crear interfaz web de matriculas]
```


### Prompt 14 - Agregar logica visual de matriculas
**Estudiante asociado:** Integrante 5
**Módulo trabajado:** Matrículas
**Objetivo:** Desarrollar static/matriculas.js con funciones de interacción visual

```text
[Prompt 14 registrado - agregar logica visual de matriculas]
```


### Prompt 15 - Crear interfaz web de reportes
**Estudiante asociado:** Integrante 5
**Módulo trabajado:** Reportes
**Objetivo:** Desarrollar la página web/reportes.html completa

```text
[Prompt 15 registrado - crear interfaz web de reportes]
```


### Prompt 16 - Agregar logica visual de reportes
**Estudiante asociado:** Integrante 5
**Módulo trabajado:** Reportes
**Objetivo:** Desarrollar static/reportes.js con funciones de interacción visual

```text
[Prompt 16 registrado - agregar logica visual de reportes]
```


### Prompt 17 - Crear pagina principal del sistema
**Estudiante asociado:** Integrante 5
**Módulo trabajado:** Integración
**Objetivo:** Crear web/index.html con menú de navegación y tarjetas de módulos

```text
[Prompt 17 registrado - crear pagina principal]
```


### Prompt 18 - Agregar servidor web simple
**Estudiante asociado:** Integrante 5
**Módulo trabajado:** Integración
**Objetivo:** Crear server.py para servir el sistema en localhost

```text
[Prompt 18 registrado - agregar servidor web]
```


### Prompt 19 - Agregar estilos generales del sistema
**Estudiante asociado:** Integrante 5
**Módulo trabajado:** Integración
**Objetivo:** Completar static/styles.css con estilos uniformes para todas las páginas

```text
[Prompt 19 registrado - agregar estilos generales]
```


### Prompt 20 - Documentar pruebas de matriculas reportes e integracion
**Estudiante asociado:** Integrante 5
**Módulo trabajado:** Reportes / Integración / Matrículas
**Objetivo:** Crear casos de prueba para matrículas, reportes e integración

```text
[Prompt 20 registrado - documentar pruebas]
```


### Prompt 21 - Revisar entrega del integrante 5
**Estudiante asociado:** Integrante 5
**Módulo trabajado:** Reportes / Integración / Matrículas
**Objetivo:** Revisión final de todos los archivos y correcciones menores

```text
[Prompt 21 registrado - revisar entrega final]
```

---

### Prompt de mejora - Login, rutas protegidas y rediseño visual
**Estudiante asociado:** Integrante 5
**Módulo trabajado:** Integración / Seguridad / Interfaz
**Objetivo:** Agregar login real con hash, proteger rutas, agregar logout, rediseñar la interfaz y documentar evidencias

```text
Necesito agregar inicio de sesión, proteger las páginas internas y mejorar la interfaz del sistema.

IMPORTANTE:
- No borres archivos existentes.
- No reemplaces módulos completos si solo necesitas corregir algo.
- No modifiques users-tokens.txt.
- No subas users-tokens.txt.
- No muestres tokens en pantalla.
- No rompas los módulos ya desarrollados.
- Mantén el proyecto con Python, HTML, CSS, JavaScript básico y JSON.
- No uses frameworks.
- El código debe ser entendible para estudiantes principiantes.

La tarea consiste en:

1. Crear login con usuarios guardados en JSON.
2. Guardar las contraseñas usando hash.
3. Proteger las rutas del sistema.
4. Cambiar el diseño visual.
5. Registrar prompts y evidencias del integrante que tenga menos commits.
6. Hacer un commit final.

------------------------------------------------------------
1. IDENTIFICAR AL INTEGRANTE CON MENOS COMMITS
------------------------------------------------------------

Después de revisar los commits, identifica el integrante con menos commits.

Luego usa sus archivos de prompts y evidencias:

Si es Integrante 1:
- prompts/estudiante_1_prompts.md
- evidencias/estudiante_1_evidencias_resultado.md

Si es Integrante 2:
- prompts/estudiante_2_prompts.md
- evidencias/estudiante_2_evidencias_resultado.md

Si es Integrante 3:
- prompts/estudiante_3_prompts.md
- evidencias/estudiante_3_evidencias_resultado.md

Si es Integrante 4:
- prompts/estudiante_4_prompts.md
- evidencias/estudiante_4_evidencias_resultado.md

Si es Integrante 5:
- prompts/estudiante_5_prompts.md
- evidencias/estudiante_5_evidencias_resultado.md

No inventes otro archivo de evidencia.

------------------------------------------------------------
2. CREAR ARCHIVO JSON DE USUARIOS
------------------------------------------------------------

Crea el archivo:

data/usuarios.json

Este archivo debe guardar usuarios del sistema.

No guardes contraseñas en texto plano.

Debe tener una estructura parecida a esta:

[
  {
    "usuario": "admin",
    "nombre": "Administrador",
    "password_hash": "...",
    "salt": "...",
    "rol": "administrador",
    "estado": "activo"
  }
]

Crea un usuario inicial:

usuario: admin
contraseña inicial: admin123
nombre: Administrador
rol: administrador
estado: activo

La contraseña admin123 debe guardarse con hash, no como texto plano.

Usa hashlib de Python.

Preferencia:
Usa hashlib.pbkdf2_hmac con salt.

Si eso se complica, usa hashlib.sha256 con salt, pero explica en comentarios que es una implementación académica básica.

------------------------------------------------------------
3. CREAR MÓDULO DE AUTENTICACIÓN
------------------------------------------------------------

Crea el archivo:

core/auth.py

Debe tener funciones simples:

- cargar_usuarios()
- guardar_usuarios(usuarios)
- generar_salt()
- generar_hash_password(password, salt)
- verificar_password(password, salt, password_hash)
- buscar_usuario(usuario)
- autenticar_usuario(usuario, password)
- crear_usuario(usuario, nombre, password, rol="usuario", estado="activo")

Reglas:

cargar_usuarios():
- debe leer data/usuarios.json
- si no existe, debe crearlo con el usuario admin por defecto
- si está vacío, debe crear el usuario admin por defecto

generar_salt():
- debe generar un salt seguro usando librerías estándar

generar_hash_password():
- debe generar el hash de la contraseña usando salt

verificar_password():
- debe comparar la contraseña ingresada con el hash guardado

autenticar_usuario():
- debe verificar que el usuario exista
- debe verificar que el estado sea activo
- debe validar la contraseña usando hash
- debe devolver un diccionario con resultado, mensaje y datos básicos del usuario sin mostrar password_hash ni salt

crear_usuario():
- debe permitir crear un usuario nuevo
- debe evitar usuarios repetidos
- debe guardar password_hash y salt
- no debe guardar password en texto plano

No uses clases.
No uses base de datos.
No uses frameworks.

------------------------------------------------------------
4. CREAR PÁGINA DE LOGIN
------------------------------------------------------------

Crea la página:

web/login.html

Debe tener:

- título del sistema
- formulario de inicio de sesión
- campo usuario
- campo contraseña
- botón Ingresar
- zona para mensajes de error
- texto breve indicando que es un sistema académico

Debe usar el CSS general del proyecto.

No debe tener la misma apariencia que las páginas antiguas.
Debe verse como una pantalla de acceso moderna, simple y limpia.

También crea o actualiza:

static/login.js

Debe tener funciones:

- obtenerDatosLogin()
- validarLogin(datos)
- mostrarMensajeLogin(mensaje, tipo)
- iniciarSesion()

La función iniciarSesion() debe enviar usuario y contraseña a server.py usando fetch.

------------------------------------------------------------
5. MODIFICAR SERVER.PY PARA LOGIN Y SESIONES
------------------------------------------------------------

Actualiza server.py para manejar autenticación básica.

Debe permitir estas rutas públicas:

- /login
- /api/login
- /static/...
- archivos CSS y JS necesarios para login

Debe proteger estas rutas:

- /
- /index
- /estudiantes
- /materias
- /matriculas
- /notas
- /asistencia
- /reportes

Si el usuario no está logueado, debe redirigir a:

/login

Agrega rutas API:

POST /api/login
- recibe usuario y password en JSON
- llama a core/auth.py
- si las credenciales son correctas, crea una sesión
- devuelve respuesta JSON positiva
- guarda una cookie de sesión

POST /api/logout
- elimina la sesión del usuario
- borra o invalida la cookie
- devuelve respuesta JSON positiva

GET /api/session
- indica si el usuario está logueado
- devuelve datos básicos del usuario si hay sesión activa

Implementa sesiones simples usando cookies.

Puedes usar:
- http.cookies
- uuid
- json
- urllib.parse si hace falta

Puedes mantener sesiones en memoria con un diccionario simple en server.py.

Ejemplo conceptual:

SESIONES = {
  "session_id": {
    "usuario": "admin",
    "nombre": "Administrador",
    "rol": "administrador"
  }
}

No muestres password_hash ni salt en respuestas al navegador.

------------------------------------------------------------
6. AGREGAR BOTÓN DE CERRAR SESIÓN
------------------------------------------------------------

Agrega en todas las páginas internas una barra superior con:

- nombre del sistema
- enlaces de navegación
- botón Cerrar sesión

El botón Cerrar sesión debe llamar a /api/logout usando fetch y luego redirigir a /login.

Debe estar en:

- index.html
- estudiantes.html
- materias.html
- matriculas.html
- notas.html
- asistencia.html
- reportes.html

No debe aparecer en login.html.

------------------------------------------------------------
7. PROTEGER TAMBIÉN DESDE JAVASCRIPT
------------------------------------------------------------

Crea o actualiza una función general en static/app.js o en cada JS si no existe app.js:

- verificarSesion()
- cerrarSesion()

verificarSesion():
- debe consultar /api/session
- si no hay sesión, debe redirigir a /login

cerrarSesion():
- debe llamar /api/logout
- luego redirigir a /login

Incluye verificarSesion() al cargar cada página interna.

Esto no reemplaza la protección en server.py, solo la refuerza visualmente.

------------------------------------------------------------
8. CAMBIAR EL DISEÑO VISUAL DEL SISTEMA
------------------------------------------------------------

Actualiza static/styles.css con un diseño diferente.

Nuevo estilo recomendado:

- diseño académico tipo panel administrativo
- barra lateral o barra superior más marcada
- colores diferentes al diseño anterior
- tarjetas con bordes suaves
- formularios más ordenados
- tablas más limpias
- botones con estilos diferenciados
- mensajes de éxito y error más visibles
- mejor separación entre secciones

No uses librerías externas.
No uses Bootstrap.
No uses frameworks.

La interfaz debe verse distinta, pero seguir siendo simple y entendible.

Aplica el nuevo diseño a:

- login.html
- index.html
- estudiantes.html
- materias.html
- matriculas.html
- notas.html
- asistencia.html
- reportes.html

------------------------------------------------------------
9. REORGANIZAR VISUALMENTE PÁGINAS CON FUNCIONES COMPARTIDAS
------------------------------------------------------------

Revisa especialmente estas páginas:

- materias.html
- matriculas.html
- notas.html
- asistencia.html
- reportes.html

Deben tener secciones separadas con títulos claros.

materias.html:
- sección Materias
- sección Periodos

matriculas.html:
- sección Registrar matrícula
- sección Consultar matrículas
- sección Cambiar estado

notas.html:
- sección Registrar notas
- sección Consultar notas
- sección Actualizar notas

asistencia.html:
- sección Registrar asistencia
- sección Consultar asistencia
- sección Indicadores de asistencia

reportes.html:
- sección Reportes académicos
- sección Estudiantes en riesgo
- sección Exportar reporte

Cada acción debe tener su propio botón claro.
No mezcles varias acciones en un solo botón.

------------------------------------------------------------
10. VERIFICAR FUNCIONAMIENTO
------------------------------------------------------------

Realiza pruebas manuales:

1. Abrir http://localhost:8000
Resultado esperado:
- redirige a /login si no hay sesión.

2. Ingresar con:
usuario: admin
contraseña: admin123

Resultado esperado:
- ingresa al sistema.

3. Intentar entrar a /estudiantes sin login.
Resultado esperado:
- redirige a /login.

4. Ingresar con contraseña incorrecta.
Resultado esperado:
- muestra error y no ingresa.

5. Cerrar sesión.
Resultado esperado:
- vuelve a /login y no permite entrar a rutas internas.

6. Guardar un estudiante.
Resultado esperado:
- se guarda en data/estudiantes.json.

7. Guardar materia, periodo, matrícula, nota y asistencia.
Resultado esperado:
- se guardan en sus JSON correspondientes.

8. Revisar que el diseño visual cambió y no se parece al anterior.

------------------------------------------------------------
11. ACTUALIZAR EVIDENCIAS
------------------------------------------------------------

Actualiza el archivo de prompts del integrante con menos commits.

Agrega este prompt completo con este título:

### Prompt de mejora - Login, rutas protegidas y rediseño visual

También actualiza su archivo de evidencias indicando:

- qué integrante realizó la mejora
- qué archivos se crearon
- qué archivos se modificaron
- cómo se implementó el hash de contraseña
- cómo se protegieron las rutas
- cómo funciona el login
- cómo funciona el logout
- qué cambios visuales se hicieron
- qué pruebas manuales se realizaron

También actualiza:

evidencias/casos_prueba_generales.md

Agrega casos de prueba sobre:

- login correcto
- login incorrecto
- ruta protegida sin sesión
- cierre de sesión
- persistencia de datos en JSON
- cambio visual del sistema

------------------------------------------------------------
12. COMMIT
------------------------------------------------------------

Antes de hacer commit, revisa:

git status

Asegúrate de no agregar:

users-tokens.txt

Luego haz commit con este mensaje:

git add .
git reset users-tokens.txt
git commit -m "feat: agregar login rutas protegidas y rediseño visual"

No hagas push todavía.
Primero confirma qué archivos fueron modificados y que el repositorio quedó sin archivos sensibles agregados.
```
