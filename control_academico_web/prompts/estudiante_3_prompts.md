# Estudiante 3 - Prompts utilizados

## Datos del estudiante

- Estudiante asociado: Integrante 3
- Módulo principal: Notas
- Responsabilidad adicional: apoyo al módulo Matrículas

## Prompts usados

Cada prompt debe registrarse con este formato:

### Prompt N - Título del prompt

**Estudiante asociado:** Integrante 3  
**Módulo trabajado:** Notas  
**Objetivo:** objetivo breve del prompt  

```text
Aquí se pega el prompt completo utilizado.
```

### Prompt 1 - Preparar evidencias del integrante 3

**Estudiante asociado:** Integrante 3  
**Módulo trabajado:** Notas  
**Objetivo:** preparar la estructura de prompts y evidencias del Integrante 3  

````text
Trabaja como agente de desarrollo dentro del proyecto control_academico_web.

Este trabajo corresponde al Integrante 3.
Módulo principal: Notas.
Responsabilidad adicional: apoyo al módulo Matrículas.

Antes de modificar archivos, revisa:
- AGENTS.md
- README.md
- estructura actual del proyecto
- prompts/estudiante_3_prompts.md
- evidencias/estudiante_3_evidencias_resultado.md

No borres archivos existentes.
No modifiques el módulo de estudiantes.
No modifiques el módulo de materias y periodos.
No desarrolles asistencia ni reportes.

Primero asegúrate de que existan estos archivos:

- prompts/estudiante_3_prompts.md
- evidencias/estudiante_3_evidencias_resultado.md

Si no existen, créalos.

El archivo prompts/estudiante_3_prompts.md debe tener esta estructura:

# Estudiante 3 - Prompts utilizados

## Datos del estudiante
- Estudiante asociado: Integrante 3
- Módulo principal: Notas
- Responsabilidad adicional: apoyo al módulo Matrículas

## Prompts usados

Cada prompt debe registrarse con este formato:

### Prompt N - Título del prompt
**Estudiante asociado:** Integrante 3
**Módulo trabajado:** Notas
**Objetivo:** objetivo breve del prompt

```text
Aquí se pega el prompt completo utilizado.
```

El archivo evidencias/estudiante_3_evidencias_resultado.md debe tener esta estructura:

# Estudiante 3 - Evidencias de resultado

## Datos del estudiante

* Estudiante asociado: Integrante 3
* Módulo principal: Notas
* Responsabilidad adicional: apoyo al módulo Matrículas

## Resultados obtenidos

| N° | Actividad realizada | Resultado entregado por la IA | Cambios realizados manualmente | Archivo creado o modificado | Observación final |
| -- | ------------------- | ----------------------------- | ------------------------------ | --------------------------- | ----------------- |

## Conversación o resumen de interacción con IA

Al terminar, guarda este prompt completo en:
prompts/estudiante_3_prompts.md

Luego actualiza:
evidencias/estudiante_3_evidencias_resultado.md

Indicando:

* qué archivos de prompts y evidencias se revisaron o crearon
* qué estructura quedó preparada para el Integrante 3
* qué se desarrollará después

Finalmente revisa los cambios y deja todo listo para commit.
````

### Prompt 2 - Crear base del módulo notas

**Estudiante asociado:** Integrante 3  
**Módulo trabajado:** Notas  
**Objetivo:** crear los archivos iniciales del módulo Notas  

```text
Continúa con el proyecto control_academico_web.

Este trabajo corresponde al Integrante 3.
Módulo principal: Notas.
Responsabilidad adicional: apoyo al módulo Matrículas.

Crea únicamente los archivos necesarios para empezar el módulo notas:

- data/notas.json
- core/notas.py
- web/notas.html
- static/notas.js

El archivo data/notas.json debe iniciar con una lista vacía [].

En core/notas.py deja preparada la estructura base con las funciones indicadas para cargar, guardar, validar, registrar, listar y actualizar notas.

Por ahora algunas funciones pueden quedar como borrador, pero deben estar ordenadas y con comentarios simples.

No modifiques estudiantes.py.
No modifiques materias.py ni periodos.py.
No desarrolles asistencia ni reportes.
No desarrolles el módulo completo de matrículas.

Al terminar, guarda este prompt completo en:
prompts/estudiante_3_prompts.md

Luego actualiza:
evidencias/estudiante_3_evidencias_resultado.md

Indicando:
- qué archivos se crearon
- qué funciones quedaron preparadas
- qué falta desarrollar

Finalmente revisa los cambios y deja todo listo para commit.
```

### Prompt 3 - Agregar lectura y guardado de notas

**Estudiante asociado:** Integrante 3  
**Módulo trabajado:** Notas  
**Objetivo:** desarrollar funciones para cargar y guardar notas en JSON  

```text
Continúa con el módulo notas.

Este trabajo corresponde al Integrante 3.
Módulo principal: Notas.

Desarrolla en core/notas.py las funciones para leer y guardar notas usando JSON:

- cargar_notas()
- guardar_notas(notas)

Reglas para cargar_notas():

- debe leer data/notas.json
- si el archivo no existe, debe crearlo con []
- si el archivo está vacío, debe devolver []
- si ocurre un error al leer, debe devolver []
- no debe romper el programa

Reglas para guardar_notas(notas):

- debe recibir una lista de notas
- debe guardar esa lista en data/notas.json
- el JSON debe quedar ordenado y legible

Usa Python básico.
Usa solo librerías estándar como json y os si hace falta.

No modifiques otros módulos.

Al terminar, guarda este prompt completo en:
prompts/estudiante_3_prompts.md

Luego actualiza:
evidencias/estudiante_3_evidencias_resultado.md

Indicando:
- qué funciones se desarrollaron
- qué validaciones de archivo se agregaron
- qué archivo fue modificado

Finalmente revisa los cambios y deja todo listo para commit.
```

### Prompt 4 - Agregar validaciones y promedio de notas

**Estudiante asociado:** Integrante 3  
**Módulo trabajado:** Notas  
**Objetivo:** validar notas, calcular promedio y determinar estado final  

```text
Continúa con el módulo notas.

Este trabajo corresponde al Integrante 3.
Módulo principal: Notas.

Desarrolla en core/notas.py estas funciones:

- validar_nota(nota)
- calcular_promedio(nota1, nota2, nota3)
- determinar_estado_final(promedio)

Reglas:
- validar_nota debe aceptar valores numéricos entre 0 y 20.
- calcular_promedio debe validar primero las tres notas y redondear a dos decimales.
- determinar_estado_final debe devolver aprobado con promedio mayor o igual a 11 y desaprobado si es menor.

Mantén el código simple y fácil de explicar.
No uses clases.
No modifiques otros módulos.

Al terminar, guarda este prompt completo en:
prompts/estudiante_3_prompts.md

Luego actualiza:
evidencias/estudiante_3_evidencias_resultado.md

Indicando:
- qué funciones se desarrollaron
- qué reglas de nota se aplicaron
- qué archivo fue modificado
- qué pruebas se deberían hacer después

Finalmente revisa los cambios y deja todo listo para commit.
```

### Prompt 5 - Validar matrícula antes de registrar notas

**Estudiante asociado:** Integrante 3  
**Módulo trabajado:** Notas  
**Objetivo:** validar que el estudiante esté matriculado antes de registrar notas  

```text
Continúa con el módulo notas.

Este trabajo corresponde al Integrante 3.
Módulo principal: Notas.
Responsabilidad adicional: apoyo al módulo Matrículas.

Desarrolla en core/notas.py la función:

- verificar_matricula_para_nota(codigo_estudiante, codigo_materia, codigo_periodo)

Esta función debe revisar data/matriculas.json, buscar una matrícula que coincida con estudiante, materia y periodo, aceptar solo matrículas activas si existe campo estado y devolver un mensaje claro si no está matriculado.

No desarrolles el módulo completo de matrículas.
No crees funciones de registro de matrícula.
Solo crea esta validación de apoyo para notas.

Al terminar, guarda este prompt completo en:
prompts/estudiante_3_prompts.md

Luego actualiza:
evidencias/estudiante_3_evidencias_resultado.md

Indicando:
- qué función de apoyo a matrículas se creó
- qué valida
- qué archivo fue modificado
- cómo se usará antes de registrar notas

Finalmente revisa los cambios y deja todo listo para commit.
```

### Prompt 6 - Evitar notas duplicadas por matrícula

**Estudiante asociado:** Integrante 3  
**Módulo trabajado:** Notas  
**Objetivo:** evitar registros duplicados de notas  

```text
Continúa con el módulo notas.

Este trabajo corresponde al Integrante 3.
Módulo principal: Notas.

Desarrolla en core/notas.py la función:

- nota_existe(codigo_estudiante, codigo_materia, codigo_periodo)

La función debe leer data/notas.json y devolver True si ya existe una nota para el mismo estudiante, materia y periodo; si no existe, debe devolver False.

Esta función servirá para evitar registrar dos veces las notas del mismo estudiante en la misma materia y periodo.

No modifiques otros módulos.
Mantén el código simple y fácil de defender.

Al terminar, guarda este prompt completo en:
prompts/estudiante_3_prompts.md

Luego actualiza:
evidencias/estudiante_3_evidencias_resultado.md

Indicando:
- qué función se desarrolló
- qué problema evita
- qué archivo fue modificado

Finalmente revisa los cambios y deja todo listo para commit.
```

### Prompt 7 - Registrar notas con validaciones

**Estudiante asociado:** Integrante 3  
**Módulo trabajado:** Notas  
**Objetivo:** registrar notas validando matrícula, duplicados y promedio  

```text
Continúa con el módulo notas.

Este trabajo corresponde al Integrante 3.
Módulo principal: Notas.

Desarrolla la función registrar_nota(codigo_estudiante, codigo_materia, codigo_periodo, nota1, nota2, nota3) en core/notas.py.

La función debe validar códigos obligatorios, verificar matrícula, validar notas entre 0 y 20, evitar duplicados, calcular promedio, determinar estado final, guardar en data/notas.json y devolver resultado, mensaje y datos.

No modifiques otros módulos.
No uses código avanzado.

Al terminar, guarda este prompt completo en:
prompts/estudiante_3_prompts.md

Luego actualiza:
evidencias/estudiante_3_evidencias_resultado.md

Indicando:
- qué función se desarrolló
- qué validaciones aplica
- cómo calcula el promedio
- qué archivo fue modificado

Finalmente revisa los cambios y deja todo listo para commit.
```

### Prompt 8 - Listar notas por estudiante y materia

**Estudiante asociado:** Integrante 3  
**Módulo trabajado:** Notas  
**Objetivo:** crear funciones de consulta de notas  

```text
Continúa con el módulo notas.

Este trabajo corresponde al Integrante 3.
Módulo principal: Notas.

Desarrolla en core/notas.py estas funciones:

- listar_notas()
- listar_notas_por_estudiante(codigo_estudiante)
- listar_notas_por_materia(codigo_materia, codigo_periodo)

Las funciones deben leer data/notas.json y devolver las notas registradas, filtradas por estudiante o por materia y periodo según corresponda.

No modifiques otros módulos.
Mantén el código sencillo.

Al terminar, guarda este prompt completo en:
prompts/estudiante_3_prompts.md

Luego actualiza:
evidencias/estudiante_3_evidencias_resultado.md

Indicando:
- qué funciones se desarrollaron
- qué casos cubren
- qué archivo fue modificado

Finalmente revisa los cambios y deja todo listo para commit.
```

### Prompt 9 - Actualizar notas y recalcular promedio

**Estudiante asociado:** Integrante 3  
**Módulo trabajado:** Notas  
**Objetivo:** actualizar notas permitidas y recalcular promedio y estado final  

```text
Continúa con el módulo notas.

Este trabajo corresponde al Integrante 3.
Módulo principal: Notas.

Desarrolla la función actualizar_nota(codigo_estudiante, codigo_materia, codigo_periodo, nuevas_notas) en core/notas.py.

La función debe buscar el registro por estudiante, materia y periodo, permitir actualizar solo nota1, nota2 y nota3, validar notas entre 0 y 20, recalcular promedio y estado_final, guardar cambios y devolver resultado, mensaje y datos.

No modifiques otros módulos.
Mantén el código simple y fácil de defender.

Al terminar, guarda este prompt completo en:
prompts/estudiante_3_prompts.md

Luego actualiza:
evidencias/estudiante_3_evidencias_resultado.md

Indicando:
- qué función se desarrolló
- qué campos permite modificar
- qué campos protege
- qué archivo fue modificado

Finalmente revisa los cambios y deja todo listo para commit.
```

### Prompt 10 - Listar matriculados sin nota registrada

**Estudiante asociado:** Integrante 3  
**Módulo trabajado:** Notas  
**Objetivo:** identificar estudiantes matriculados que aún no tienen nota  

```text
Continúa con el proyecto control_academico_web.

Este trabajo corresponde al Integrante 3.
Módulo principal: Notas.
Responsabilidad adicional: apoyo al módulo Matrículas.

Desarrolla en core/notas.py la función:

- listar_estudiantes_sin_nota(codigo_materia, codigo_periodo)

La función debe leer data/matriculas.json y data/notas.json, comparar estudiantes matriculados en la materia y periodo indicados con las notas ya registradas, y devolver quienes aún no tienen nota. Si existe data/estudiantes.json puede usarlo para mostrar nombres.

No desarrolles el módulo completo de matrículas.
No modifiques otros módulos.
Esta función solo será apoyo para notas y reportes.

Al terminar, guarda este prompt completo en:
prompts/estudiante_3_prompts.md

Luego actualiza:
evidencias/estudiante_3_evidencias_resultado.md

Indicando:
- qué función de apoyo se creó
- qué archivos consulta
- qué problema ayuda a resolver
- qué falta integrar después

Finalmente revisa los cambios y deja todo listo para commit.
```

### Prompt 11 - Crear interfaz web de notas

**Estudiante asociado:** Integrante 3  
**Módulo trabajado:** Notas  
**Objetivo:** crear la página HTML del módulo Notas  

```text
Continúa con el módulo notas.

Este trabajo corresponde al Integrante 3.
Módulo principal: Notas.

Desarrolla la página web/notas.html con título, formulario de registro, sección para listar por estudiante o materia, tabla de notas y zona de mensajes.

Usa HTML simple.
No hagas diseño complejo.
Usa ids claros para conectar con JavaScript.

El archivo debe quedar listo para trabajar con static/notas.js.

No conectes todavía con otros módulos.
No modifiques las páginas de estudiantes ni materias.

Al terminar, guarda este prompt completo en:
prompts/estudiante_3_prompts.md

Luego actualiza:
evidencias/estudiante_3_evidencias_resultado.md

Indicando:
- qué página se creó
- qué elementos contiene
- qué falta conectar después

Finalmente revisa los cambios y deja todo listo para commit.
```

### Prompt 12 - Agregar lógica visual de notas

**Estudiante asociado:** Integrante 3  
**Módulo trabajado:** Notas  
**Objetivo:** crear funciones JavaScript para manejar la pantalla de notas  

```text
Continúa con el módulo notas.

Este trabajo corresponde al Integrante 3.
Módulo principal: Notas.

Desarrolla static/notas.js para manejar la página web/notas.html.

El JavaScript debe capturar datos del formulario, validar campos vacíos, validar notas entre 0 y 20, mostrar mensajes, limpiar formulario, llenar tabla, filtrar por estudiante, filtrar por materia y periodo, y preparar la actualización.

Usa estos nombres de funciones:
- obtenerDatosFormularioNota()
- validarFormularioNota(datos)
- mostrarMensajeNotas(mensaje, tipo)
- limpiarFormularioNota()
- renderizarTablaNotas(notas)
- filtrarNotasPorEstudiante(codigo_estudiante)
- filtrarNotasPorMateria(codigo_materia, codigo_periodo)
- prepararActualizacionNota(codigo_estudiante, codigo_materia, codigo_periodo)

No mezcles este archivo con otros módulos.
No desarrolles código de estudiantes, materias, asistencia, matrículas ni reportes.

Al terminar, guarda este prompt completo en:
prompts/estudiante_3_prompts.md

Luego actualiza:
evidencias/estudiante_3_evidencias_resultado.md

Indicando:
- qué funciones JavaScript se crearon
- qué parte de la pantalla controlan
- qué falta integrar después

Finalmente revisa los cambios y deja todo listo para commit.
```

### Prompt 13 - Documentar pruebas del módulo notas

**Estudiante asociado:** Integrante 3  
**Módulo trabajado:** Notas  
**Objetivo:** documentar casos de prueba del módulo Notas  

```text
Continúa con el módulo notas del proyecto control_academico_web.

Este trabajo corresponde al Integrante 3.
Módulo principal: Notas.
Responsabilidad adicional: apoyo al módulo Matrículas.

Antes de trabajar, revisa:

git status
git log --oneline -5

Asegúrate de que el commit anterior ya exista:

feat: agregar logica visual de notas

Ahora crea un archivo de pruebas dentro de evidencias llamado:

control_academico_web/evidencias/casos_prueba_notas.md

El archivo debe incluir una tabla con estas columnas:

- número de caso
- acción realizada
- datos de entrada
- resultado esperado
- resultado obtenido
- observación

Incluye estos casos:

1. Registrar nota correctamente.
2. Registrar nota con estudiante vacío.
3. Registrar nota con materia vacía.
4. Registrar nota con periodo vacío.
5. Registrar nota menor a 0.
6. Registrar nota mayor a 20.
7. Registrar nota con texto en vez de número.
8. Registrar nota de estudiante no matriculado.
9. Registrar nota duplicada para el mismo estudiante, materia y periodo.
10. Calcular promedio aprobado.
11. Calcular promedio desaprobado.
12. Listar notas registradas.
13. Listar notas por estudiante.
14. Listar notas por materia y periodo.
15. Actualizar notas existentes.
16. Intentar actualizar nota inexistente.
17. Verificar estudiantes matriculados sin nota.

Agrega al final una sección llamada:

Conclusión del módulo

En esa sección indica si el módulo notas quedó listo para integrarse con matrículas, estudiantes, materias y reportes.

También actualiza:

control_academico_web/prompts/estudiante_3_prompts.md

Agrega este prompt completo como nuevo registro, sin borrar los prompts anteriores.

También actualiza:

control_academico_web/evidencias/estudiante_3_evidencias_resultado.md

Indicando:
- que se creó la evidencia de pruebas
- qué casos cubre
- qué falta verificar en la integración

Cuando termines, revisa los cambios con:

git status

Luego haz el commit:

git add control_academico_web/evidencias/casos_prueba_notas.md control_academico_web/evidencias/estudiante_3_evidencias_resultado.md control_academico_web/prompts/estudiante_3_prompts.md
git commit -m "test: documentar pruebas del modulo notas"

No hagas push todavía.
```
