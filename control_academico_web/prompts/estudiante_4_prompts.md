# Estudiante 4 - Prompts utilizados

## Datos del estudiante

- Estudiante asociado: Integrante 4
- Módulo principal: Asistencia
- Responsabilidad adicional: apoyo al módulo Matrículas

## Prompts usados

Cada prompt debe registrarse con este formato:

### Prompt N - Título del prompt

**Estudiante asociado:** Integrante 4
**Módulo trabajado:** Asistencia
**Objetivo:** objetivo breve del prompt

```text
Aquí se pega el prompt completo utilizado.
```

### Prompt 1 - Preparar evidencias del integrante 4

**Estudiante asociado:** Integrante 4
**Módulo trabajado:** Asistencia
**Objetivo:** preparar la estructura de prompts y evidencias del Integrante 4

```text
Trabaja como agente de desarrollo dentro del proyecto control_academico_web.

Este trabajo corresponde al Integrante 4.
Módulo principal: Asistencia.
Responsabilidad adicional: apoyo al módulo Matrículas.

Antes de modificar archivos, revisa:
- AGENTS.md
- README.md
- estructura actual del proyecto
- prompts/estudiante_4_prompts.md
- evidencias/estudiante_4_evidencias_resultado.md

No borres archivos existentes.
No modifiques el módulo de estudiantes.
No modifiques el módulo de materias y periodos.
No modifiques el módulo de notas.
No desarrolles reportes.

Primero asegúrate de que existan estos archivos:

- prompts/estudiante_4_prompts.md
- evidencias/estudiante_4_evidencias_resultado.md

Si no existen, créalos.

El archivo prompts/estudiante_4_prompts.md debe tener esta estructura:

# Estudiante 4 - Prompts utilizados

## Datos del estudiante
- Estudiante asociado: Integrante 4
- Módulo principal: Asistencia
- Responsabilidad adicional: apoyo al módulo Matrículas

## Prompts usados

Cada prompt debe registrarse con este formato:

### Prompt N - Título del prompt
**Estudiante asociado:** Integrante 4
**Módulo trabajado:** Asistencia
**Objetivo:** objetivo breve del prompt

Aquí se pega el prompt completo utilizado.

El archivo evidencias/estudiante_4_evidencias_resultado.md debe tener esta estructura:

# Estudiante 4 - Evidencias de resultado

## Datos del estudiante
- Estudiante asociado: Integrante 4
- Módulo principal: Asistencia
- Responsabilidad adicional: apoyo al módulo Matrículas

## Resultados obtenidos

| N° | Actividad realizada | Resultado entregado por la IA | Cambios realizados manualmente | Archivo creado o modificado | Observación final |
|---|---|---|---|---|---|

## Conversación o resumen de interacción con IA

Al terminar, guarda este prompt completo en:
prompts/estudiante_4_prompts.md

Luego actualiza:
evidencias/estudiante_4_evidencias_resultado.md

Indicando:
- qué archivos de prompts y evidencias se revisaron o crearon
- qué estructura quedó preparada para el Integrante 4
- qué se desarrollará después

Finalmente revisa los cambios y deja todo listo para commit.
```

### Prompt 2 - Crear base del modulo asistencia

**Estudiante asociado:** Integrante 4
**Módulo trabajado:** Asistencia
**Objetivo:** crear los archivos iniciales del modulo Asistencia

```text
Continúa con el proyecto control_academico_web.

Este trabajo corresponde al Integrante 4.
Módulo principal: Asistencia.
Responsabilidad adicional: apoyo al módulo Matrículas.

Crea únicamente los archivos necesarios para empezar el módulo asistencia:

- data/asistencias.json
- core/asistencia.py
- web/asistencia.html
- static/asistencia.js

El archivo data/asistencias.json debe iniciar con una lista vacía [].

En core/asistencia.py deja preparada la estructura base con estas funciones:

- cargar_asistencias()
- guardar_asistencias(asistencias)
- validar_estado_asistencia(estado)
- validar_fecha(fecha)
- verificar_matricula_para_asistencia(codigo_estudiante, codigo_materia, codigo_periodo)
- asistencia_duplicada(codigo_estudiante, codigo_materia, codigo_periodo, fecha)
- registrar_asistencia(codigo_estudiante, codigo_materia, codigo_periodo, fecha, estado_asistencia)
- listar_asistencias()
- listar_asistencia_por_estudiante(codigo_estudiante)
- listar_asistencia_por_materia(codigo_materia, codigo_periodo, fecha=None)
- calcular_porcentaje_asistencia(codigo_estudiante, codigo_materia, codigo_periodo)
- listar_matriculados_para_asistencia(codigo_materia, codigo_periodo)

Por ahora algunas funciones pueden quedar como borrador, pero deben estar ordenadas y con comentarios simples.

No modifiques estudiantes.py.
No modifiques materias.py ni periodos.py.
No modifiques notas.py.
No desarrolles reportes.
No desarrolles el módulo completo de matrículas.

Al terminar, guarda este prompt completo en:
prompts/estudiante_4_prompts.md

Luego actualiza:
evidencias/estudiante_4_evidencias_resultado.md

Indicando:
- qué archivos se crearon
- qué funciones quedaron preparadas
- qué falta desarrollar

Finalmente revisa los cambios y deja todo listo para commit.
```

### Prompt 3 - Agregar lectura y guardado de asistencias

**Estudiante asociado:** Integrante 4
**Módulo trabajado:** Asistencia
**Objetivo:** desarrollar funciones para cargar y guardar asistencias en JSON

```text
Continúa con el módulo asistencia.

Este trabajo corresponde al Integrante 4.
Módulo principal: Asistencia.

Desarrolla en core/asistencia.py las funciones para leer y guardar asistencias usando JSON:

- cargar_asistencias()
- guardar_asistencias(asistencias)

Reglas para cargar_asistencias():

- debe leer data/asistencias.json
- si el archivo no existe, debe crearlo con []
- si el archivo está vacío, debe devolver []
- si ocurre un error al leer, debe devolver []
- no debe romper el programa

Reglas para guardar_asistencias(asistencias):

- debe recibir una lista de asistencias
- debe guardar esa lista en data/asistencias.json
- el JSON debe quedar ordenado y legible

Usa Python básico.
Usa solo librerías estándar como json y os si hace falta.

No modifiques otros módulos.

Al terminar, guarda este prompt completo en:
prompts/estudiante_4_prompts.md

Luego actualiza:
evidencias/estudiante_4_evidencias_resultado.md

Indicando:
- qué funciones se desarrollaron
- qué validaciones de archivo se agregaron
- qué archivo fue modificado

Finalmente revisa los cambios y deja todo listo para commit.
```

### Prompt 4 - Agregar validaciones de asistencia

**Estudiante asociado:** Integrante 4
**Módulo trabajado:** Asistencia
**Objetivo:** validar estado de asistencia y formato de fecha

```text
Continúa con el módulo asistencia.

Este trabajo corresponde al Integrante 4.
Módulo principal: Asistencia.

Desarrolla en core/asistencia.py estas funciones:

- validar_estado_asistencia(estado)
- validar_fecha(fecha)

Reglas para validar_estado_asistencia(estado):

- debe aceptar solo estos estados:
  - presente
  - tarde
  - falta
  - justificado
- debe convertir el texto a minúsculas para evitar errores por mayúsculas
- debe devolver True si el estado es válido
- debe devolver False o un mensaje claro si no es válido

Reglas para validar_fecha(fecha):

- debe verificar que la fecha no esté vacía
- debe aceptar el formato YYYY-MM-DD
- si el formato es incorrecto, debe devolver un mensaje claro
- puedes usar datetime de Python si es necesario

Mantén el código simple y fácil de explicar.
No uses clases.
No modifiques otros módulos.

Al terminar, guarda este prompt completo en:
prompts/estudiante_4_prompts.md

Luego actualiza:
evidencias/estudiante_4_evidencias_resultado.md

Indicando:
- qué validaciones se implementaron
- qué reglas se aplicaron
- qué archivo fue modificado
- qué pruebas se deberían hacer después

Finalmente revisa los cambios y deja todo listo para commit.
```

### Prompt 5 - Validar matricula antes de registrar asistencia

**Estudiante asociado:** Integrante 4
**Módulo trabajado:** Asistencia
**Objetivo:** validar matricula activa antes de registrar asistencia

```text
Continúa con el módulo asistencia.

Este trabajo corresponde al Integrante 4.
Módulo principal: Asistencia.
Responsabilidad adicional: apoyo al módulo Matrículas.

Desarrolla en core/asistencia.py la función:

- verificar_matricula_para_asistencia(codigo_estudiante, codigo_materia, codigo_periodo)

Esta función debe servir para validar que un estudiante esté matriculado antes de registrar asistencia.

Reglas:

- debe revisar el archivo data/matriculas.json
- si data/matriculas.json no existe, debe tratarlo como una lista vacía
- debe buscar una matrícula que coincida con:
  - codigo_estudiante
  - codigo_materia
  - codigo_periodo
- solo debe permitir registrar asistencia si la matrícula existe
- si el registro de matrícula tiene campo estado, debe aceptar solo matrículas activas
- si el estudiante no está matriculado, debe devolver un mensaje claro

No desarrolles el módulo completo de matrículas.
No crees funciones de registro de matrícula.
Solo crea esta validación de apoyo para asistencia.

Al terminar, guarda este prompt completo en:
prompts/estudiante_4_prompts.md

Luego actualiza:
evidencias/estudiante_4_evidencias_resultado.md

Indicando:
- qué función de apoyo a matrículas se creó
- qué valida
- qué archivo fue modificado
- cómo se usará antes de registrar asistencia

Finalmente revisa los cambios y deja todo listo para commit.
```

### Prompt 6 - Evitar asistencia duplicada

**Estudiante asociado:** Integrante 4
**Módulo trabajado:** Asistencia
**Objetivo:** evitar registrar dos veces la asistencia del mismo estudiante en el mismo dia

```text
Continúa con el módulo asistencia.

Este trabajo corresponde al Integrante 4.
Módulo principal: Asistencia.

Desarrolla en core/asistencia.py la función:

- asistencia_duplicada(codigo_estudiante, codigo_materia, codigo_periodo, fecha)

Reglas:

- debe leer data/asistencias.json
- debe verificar si ya existe una asistencia registrada para el mismo:
  - estudiante
  - materia
  - periodo
  - fecha
- debe devolver True si ya existe
- debe devolver False si no existe

Esta función servirá para evitar registrar dos veces asistencia del mismo estudiante en la misma clase.

No modifiques otros módulos.
Mantén el código simple y fácil de defender.

Al terminar, guarda este prompt completo en:
prompts/estudiante_4_prompts.md

Luego actualiza:
evidencias/estudiante_4_evidencias_resultado.md

Indicando:
- qué función se desarrolló
- qué problema evita
- qué archivo fue modificado

Finalmente revisa los cambios y deja todo listo para commit.
```

### Prompt 7 - Registrar asistencia con validaciones

**Estudiante asociado:** Integrante 4
**Módulo trabajado:** Asistencia
**Objetivo:** registrar asistencia validando matricula, duplicados y campos obligatorios

```text
Continúa con el módulo asistencia.

Este trabajo corresponde al Integrante 4.
Módulo principal: Asistencia.

Desarrolla la función registrar_asistencia(codigo_estudiante, codigo_materia, codigo_periodo, fecha, estado_asistencia) en core/asistencia.py.

La función debe:

- validar que codigo_estudiante no esté vacío
- validar que codigo_materia no esté vacío
- validar que codigo_periodo no esté vacío
- validar que fecha no esté vacía y tenga formato YYYY-MM-DD
- validar que estado_asistencia sea:
  - presente
  - tarde
  - falta
  - justificado
- verificar que el estudiante esté matriculado usando verificar_matricula_para_asistencia()
- evitar asistencia duplicada usando asistencia_duplicada()
- guardar el registro en data/asistencias.json
- devolver un diccionario con resultado, mensaje y datos de la asistencia registrada

La asistencia debe guardarse con esta estructura:

{
  "codigo_estudiante": "EST001",
  "codigo_materia": "MAT001",
  "codigo_periodo": "2026-I",
  "fecha": "2026-06-24",
  "estado_asistencia": "presente"
}

Si hay error, debe devolver un mensaje claro y no guardar datos.

No modifiques otros módulos.
No uses código avanzado.

Al terminar, guarda este prompt completo en:
prompts/estudiante_4_prompts.md

Luego actualiza:
evidencias/estudiante_4_evidencias_resultado.md

Indicando:
- qué función se desarrolló
- qué validaciones aplica
- cómo se guarda una asistencia
- qué archivo fue modificado

Finalmente revisa los cambios y deja todo listo para commit.
```

### Prompt 8 - Listar asistencia por estudiante y materia

**Estudiante asociado:** Integrante 4
**Módulo trabajado:** Asistencia
**Objetivo:** crear funciones de consulta de asistencia

```text
Continúa con el módulo asistencia.

Este trabajo corresponde al Integrante 4.
Módulo principal: Asistencia.

Desarrolla en core/asistencia.py estas funciones:

- listar_asistencias()
- listar_asistencia_por_estudiante(codigo_estudiante)
- listar_asistencia_por_materia(codigo_materia, codigo_periodo, fecha=None)

listar_asistencias():
- debe leer data/asistencias.json
- debe devolver todas las asistencias registradas
- si no hay asistencias, debe devolver una lista vacía

listar_asistencia_por_estudiante(codigo_estudiante):
- debe devolver todas las asistencias de un estudiante
- si existe data/materias.json, puede usarlo para mostrar el nombre de la materia
- si no encuentra registros, debe devolver lista vacía o mensaje claro

listar_asistencia_por_materia(codigo_materia, codigo_periodo, fecha=None):
- debe devolver asistencias de una materia y periodo
- si se envía fecha, debe filtrar por fecha
- si no se envía fecha, debe listar todos los registros de esa materia y periodo
- debe incluir código de estudiante, materia, periodo, fecha y estado

No modifiques otros módulos.
Mantén el código sencillo y entendible.

Al terminar, guarda este prompt completo en:
prompts/estudiante_4_prompts.md

Luego actualiza:
evidencias/estudiante_4_evidencias_resultado.md

Indicando:
- qué funciones se desarrollaron
- qué casos cubren
- qué archivo fue modificado

Finalmente revisa los cambios y deja todo listo para commit.
```

### Prompt 9 - Calcular porcentaje de asistencia

**Estudiante asociado:** Integrante 4
**Módulo trabajado:** Asistencia
**Objetivo:** calcular el porcentaje de asistencia de un estudiante

```text
Continúa con el módulo asistencia.

Este trabajo corresponde al Integrante 4.
Módulo principal: Asistencia.

Desarrolla en core/asistencia.py la función:

- calcular_porcentaje_asistencia(codigo_estudiante, codigo_materia, codigo_periodo)

La función debe calcular el porcentaje de asistencia del estudiante en una materia y periodo.

Reglas:

- debe leer data/asistencias.json
- debe filtrar registros por:
  - codigo_estudiante
  - codigo_materia
  - codigo_periodo
- debe contar el total de clases registradas
- debe considerar como asistencia:
  - presente
  - tarde
  - justificado
- debe considerar como falta:
  - falta
- debe calcular el porcentaje con esta formula:

porcentaje = (asistencias / total_clases) * 100

Debe devolver un diccionario con:
- codigo_estudiante
- codigo_materia
- codigo_periodo
- total_clases
- asistencias
- faltas
- porcentaje_asistencia

Si no hay registros, debe devolver un mensaje claro o porcentaje 0.

No modifiques otros módulos.
Mantén el código simple y fácil de explicar.

Al terminar, guarda este prompt completo en:
prompts/estudiante_4_prompts.md

Luego actualiza:
evidencias/estudiante_4_evidencias_resultado.md

Indicando:
- qué función se desarrolló
- qué fórmula se usa
- qué estados cuentan como asistencia
- qué archivo fue modificado

Finalmente revisa los cambios y deja todo listo para commit.
```

### Prompt 10 - Listar matriculados para asistencia

**Estudiante asociado:** Integrante 4
**Módulo trabajado:** Asistencia
**Objetivo:** obtener estudiantes matriculados antes de tomar asistencia

```text
Continúa con el proyecto control_academico_web.

Este trabajo corresponde al Integrante 4.
Módulo principal: Asistencia.
Responsabilidad adicional: apoyo al módulo Matrículas.

Desarrolla en core/asistencia.py la función:

- listar_matriculados_para_asistencia(codigo_materia, codigo_periodo)

Esta función debe servir para obtener los estudiantes matriculados antes de tomar asistencia.

Reglas:

- debe leer data/matriculas.json
- si existe data/estudiantes.json, debe usarlo para mostrar nombres y DNI del estudiante
- debe buscar estudiantes matriculados en la materia y periodo indicados
- si el registro de matrícula tiene campo estado, debe mostrar solo matrículas activas
- debe devolver una lista de estudiantes matriculados
- cada registro debe incluir:
  - codigo_estudiante
  - nombres y apellidos, si están disponibles
  - DNI, si está disponible
  - codigo_materia
  - codigo_periodo
  - estado de matrícula, si existe

No desarrolles el módulo completo de matrículas.
No modifiques otros módulos.
Esta función solo será apoyo para tomar asistencia.

Al terminar, guarda este prompt completo en:
prompts/estudiante_4_prompts.md

Luego actualiza:
evidencias/estudiante_4_evidencias_resultado.md

Indicando:
- qué función de apoyo se creó
- qué archivos consulta
- qué problema ayuda a resolver
- qué falta integrar después

Finalmente revisa los cambios y deja todo listo para commit.
```

### Prompt 11 - Crear interfaz web de asistencia

**Estudiante asociado:** Integrante 4
**Módulo trabajado:** Asistencia
**Objetivo:** desarrollar la pagina HTML para la gestion de asistencia

```text
Continúa con el módulo asistencia.

Este trabajo corresponde al Integrante 4.
Módulo principal: Asistencia.

Desarrolla la página web/asistencia.html.

La página debe tener estas secciones:

1. Título:
Gestión de asistencia

2. Formulario de registro de asistencia con estos campos:
- código de estudiante
- código de materia
- código de periodo
- fecha
- estado de asistencia

3. Estados permitidos:
- presente
- tarde
- falta
- justificado

4. Botón:
Guardar asistencia

5. Sección para buscar o listar asistencia:
- campo para código de estudiante
- botón Listar asistencia por estudiante
- campo para código de materia
- campo para código de periodo
- campo opcional para fecha
- botón Listar asistencia por materia

6. Sección para porcentaje de asistencia:
- código de estudiante
- código de materia
- código de periodo
- botón Calcular porcentaje

7. Tabla de asistencia con columnas:
- código de estudiante
- código de materia
- periodo
- fecha
- estado de asistencia
- acciones

8. Zona para mostrar mensajes:
- errores
- confirmaciones

Usa HTML simple.
No hagas diseño complejo.
Usa ids claros para conectar con JavaScript.

El archivo debe quedar listo para trabajar con static/asistencia.js.

No conectes todavía con otros módulos.
No modifiques las páginas de estudiantes, materias ni notas.

Al terminar, guarda este prompt completo en:
prompts/estudiante_4_prompts.md

Luego actualiza:
evidencias/estudiante_4_evidencias_resultado.md

Indicando:
- qué página se creó
- qué elementos contiene
- qué falta conectar después

Finalmente revisa los cambios y deja todo listo para commit.
```

### Prompt 12 - Agregar logica visual de asistencia

**Estudiante asociado:** Integrante 4
**Módulo trabajado:** Asistencia
**Objetivo:** desarrollar el JavaScript para la pagina de asistencia

```text
Continúa con el módulo asistencia.

Este trabajo corresponde al Integrante 4.
Módulo principal: Asistencia.

Desarrolla static/asistencia.js para manejar la página web/asistencia.html.

El JavaScript debe tener funciones para:

- capturar los datos del formulario de asistencia
- validar campos vacíos antes de enviar
- validar visualmente el estado de asistencia
- validar visualmente que la fecha no esté vacía
- mostrar mensajes en pantalla
- limpiar el formulario
- llenar la tabla de asistencia
- buscar o filtrar asistencia por estudiante
- buscar o filtrar asistencia por materia y periodo
- preparar el cálculo del porcentaje de asistencia

Usa estos nombres de funciones:

- obtenerDatosFormularioAsistencia()
- validarFormularioAsistencia(datos)
- mostrarMensajeAsistencia(mensaje, tipo)
- limpiarFormularioAsistencia()
- renderizarTablaAsistencia(asistencias)
- filtrarAsistenciaPorEstudiante(codigo_estudiante)
- filtrarAsistenciaPorMateria(codigo_materia, codigo_periodo, fecha)
- prepararCalculoPorcentaje(codigo_estudiante, codigo_materia, codigo_periodo)

Como la integración completa con Python se hará después, deja funciones separadas y claras para conectarlas con el servidor.

No mezcles este archivo con otros módulos.
No desarrolles código de estudiantes, materias, notas, matrículas ni reportes.

Al terminar, guarda este prompt completo en:
prompts/estudiante_4_prompts.md

Luego actualiza:
evidencias/estudiante_4_evidencias_resultado.md

Indicando:
- qué funciones JavaScript se crearon
- qué parte de la pantalla controlan
- qué falta integrar después

Finalmente revisa los cambios y deja todo listo para commit.
```

### Prompt 13 - Documentar pruebas del modulo asistencia

**Estudiante asociado:** Integrante 4
**Módulo trabajado:** Asistencia
**Objetivo:** crear archivo de casos de prueba para el modulo asistencia

```text
Continúa con el módulo asistencia.

Este trabajo corresponde al Integrante 4.
Módulo principal: Asistencia.
Responsabilidad adicional: apoyo al módulo Matrículas.

Crea un archivo de pruebas dentro de evidencias llamado:

casos_prueba_asistencia.md

El archivo debe incluir una tabla con:

- número de caso
- acción realizada
- datos de entrada
- resultado esperado
- resultado obtenido
- observación

Incluye estos casos:

1. Registrar asistencia correctamente.
2. Registrar asistencia con estudiante vacío.
3. Registrar asistencia con materia vacía.
4. Registrar asistencia con periodo vacío.
5. Registrar asistencia con fecha vacía.
6. Registrar asistencia con fecha inválida.
7. Registrar asistencia con estado inválido.
8. Registrar asistencia de estudiante no matriculado.
9. Registrar asistencia duplicada para el mismo estudiante, materia, periodo y fecha.
10. Listar asistencias registradas.
11. Listar asistencia por estudiante.
12. Listar asistencia por materia y periodo.
13. Listar asistencia por materia, periodo y fecha.
14. Calcular porcentaje con asistencias y faltas.
15. Calcular porcentaje cuando solo tiene faltas.
16. Calcular porcentaje cuando no hay registros.
17. Listar matriculados para tomar asistencia.

Agrega al final una sección llamada:

Conclusión del módulo

En esa sección indica si el módulo asistencia quedó listo para integrarse con matrículas, estudiantes, materias y reportes.

Al terminar, guarda este prompt completo en:
prompts/estudiante_4_prompts.md

Luego actualiza:
evidencias/estudiante_4_evidencias_resultado.md

Indicando:
- que se creó la evidencia de pruebas
- qué casos cubre
- qué falta verificar en la integración

Finalmente revisa los cambios y deja todo listo para commit.
```

### Prompt 14 - Revisar entrega del integrante 4

**Estudiante asociado:** Integrante 4
**Módulo trabajado:** Asistencia
**Objetivo:** revision final del trabajo del Integrante 4

```text
Haz una revisión final del trabajo del Integrante 4 en el proyecto control_academico_web.

Este trabajo corresponde al Integrante 4.
Módulo principal: Asistencia.
Responsabilidad adicional: apoyo al módulo Matrículas.

Revisa que existan y estén ordenados estos elementos:

- data/asistencias.json
- core/asistencia.py
- web/asistencia.html
- static/asistencia.js
- prompts/estudiante_4_prompts.md
- evidencias/estudiante_4_evidencias_resultado.md
- evidencias/casos_prueba_asistencia.md

Verifica que:

- los prompts del Integrante 4 estén guardados en prompts/estudiante_4_prompts.md
- las evidencias del resultado estén registradas
- asistencia.py tenga funciones claras y separadas
- el módulo pueda validar matrícula antes de registrar asistencia
- el módulo evite asistencias duplicadas
- el módulo pueda listar asistencia por estudiante, materia y fecha
- el módulo pueda calcular porcentaje de asistencia
- no se haya modificado indebidamente estudiantes.py
- no se haya modificado indebidamente materias.py o periodos.py
- no se haya modificado indebidamente notas.py
- no se hayan desarrollado módulos que correspondan a otros integrantes
- no se hayan borrado archivos existentes
- el código sea entendible para estudiantes principiantes

Si encuentras detalles pequeños, corrígelos.
No hagas cambios grandes.
No agregues funcionalidades nuevas.

Al terminar, guarda este prompt completo en:
prompts/estudiante_4_prompts.md

Luego actualiza:
evidencias/estudiante_4_evidencias_resultado.md

Indicando:
- qué se revisó
- qué correcciones menores se hicieron
- si el trabajo del Integrante 4 quedó listo

Finalmente revisa los cambios y deja todo listo para commit.
```
