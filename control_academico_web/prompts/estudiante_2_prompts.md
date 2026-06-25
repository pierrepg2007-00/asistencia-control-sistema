# Estudiante 2 - Prompts utilizados

## Datos del estudiante

- Estudiante asociado: Integrante 2
- Módulo principal: Materias y periodos
- Responsabilidad adicional: apoyo al módulo Matrículas

## Prompts usados

Cada prompt debe registrarse con este formato:

### Prompt N - Título del prompt

**Estudiante asociado:** Integrante 2  
**Módulo trabajado:** Materias y periodos  
**Objetivo:** objetivo breve del prompt  

```text
Aquí se pega el prompt completo utilizado.
```

### Prompt 1 - Preparar evidencias del integrante 2

**Estudiante asociado:** Integrante 2  
**Módulo trabajado:** Materias y periodos  
**Objetivo:** preparar la estructura de prompts y evidencias del Integrante 2  

```text
Trabaja como agente de desarrollo dentro del proyecto control_academico_web.

Este trabajo corresponde al Integrante 2.
Módulo principal: Materias y periodos.
Responsabilidad adicional: apoyo al módulo Matrículas.

Antes de modificar archivos, revisa:
- AGENTS.md
- README.md
- estructura actual del proyecto
- prompts/estudiante_2_prompts.md
- evidencias/estudiante_2_evidencias_resultado.md

No borres archivos existentes.
No modifiques el módulo de estudiantes.
No desarrolles todavía notas, asistencia ni reportes.

Primero asegúrate de que existan estos archivos:

- prompts/estudiante_2_prompts.md
- evidencias/estudiante_2_evidencias_resultado.md

Si no existen, créalos.

El archivo prompts/estudiante_2_prompts.md debe tener esta estructura:

# Estudiante 2 - Prompts utilizados

## Datos del estudiante
- Estudiante asociado: Integrante 2
- Módulo principal: Materias y periodos
- Responsabilidad adicional: apoyo al módulo Matrículas

## Prompts usados

Cada prompt debe registrarse con este formato:

### Prompt N - Título del prompt
**Estudiante asociado:** Integrante 2
**Módulo trabajado:** Materias y periodos
**Objetivo:** objetivo breve del prompt

```text
Aquí se pega el prompt completo utilizado.
```

El archivo evidencias/estudiante_2_evidencias_resultado.md debe tener esta estructura:

# Estudiante 2 - Evidencias de resultado

## Datos del estudiante

* Estudiante asociado: Integrante 2
* Módulo principal: Materias y periodos
* Responsabilidad adicional: apoyo al módulo Matrículas

## Resultados obtenidos

| N° | Actividad realizada | Resultado entregado por la IA | Cambios realizados manualmente | Archivo creado o modificado | Observación final |
| -- | ------------------- | ----------------------------- | ------------------------------ | --------------------------- | ----------------- |

## Conversación o resumen de interacción con IA

Al terminar, guarda este prompt completo en:
prompts/estudiante_2_prompts.md

Luego actualiza:
evidencias/estudiante_2_evidencias_resultado.md

Indicando:

* qué archivos de prompts y evidencias se revisaron o crearon
* qué estructura quedó preparada para el Integrante 2
* qué se desarrollará después

Finalmente revisa los cambios y deja todo listo para commit.
```

### Prompt 2 - Crear base del módulo materias y periodos

**Estudiante asociado:** Integrante 2  
**Módulo trabajado:** Materias y periodos  
**Objetivo:** crear los archivos iniciales del módulo Materias y periodos  

```text
Continúa con el proyecto control_academico_web.

Este trabajo corresponde al Integrante 2.
Módulo principal: Materias y periodos.
Responsabilidad adicional: apoyo al módulo Matrículas.

Crea únicamente los archivos necesarios para empezar el módulo de materias y periodos:

- data/materias.json
- data/periodos.json
- core/materias.py
- core/periodos.py
- web/materias.html
- static/materias.js

Los archivos JSON deben iniciar con una lista vacía [].

En core/materias.py deja preparada la estructura base con estas funciones:

- cargar_materias()
- guardar_materias(materias)
- generar_codigo_materia()
- registrar_materia(nombre_materia, docente, ciclo, estado)
- listar_materias()
- buscar_materia(codigo_materia)
- actualizar_materia(codigo_materia, nuevos_datos)
- validar_ciclo(ciclo)
- validar_estado_materia(estado)
- materia_existe(codigo_materia)

En core/periodos.py deja preparada la estructura base con estas funciones:

- cargar_periodos()
- guardar_periodos(periodos)
- registrar_periodo(codigo_periodo, anio, nombre, estado)
- listar_periodos()
- buscar_periodo(codigo_periodo)
- obtener_periodo_activo()
- cambiar_periodo_activo(codigo_periodo)
- validar_estado_periodo(estado)
- periodo_existe(codigo_periodo)

Por ahora algunas funciones pueden quedar como borrador, pero deben estar ordenadas y con comentarios simples.

No modifiques el módulo estudiantes.
No crees archivos de notas, asistencia ni reportes.
No desarrolles el módulo completo de matrículas todavía.

Al terminar, guarda este prompt completo en:
prompts/estudiante_2_prompts.md

Luego actualiza:
evidencias/estudiante_2_evidencias_resultado.md

Indicando:
- qué archivos se crearon
- qué funciones quedaron preparadas
- qué falta desarrollar

Finalmente revisa los cambios y deja todo listo para commit.
```

### Prompt 3 - Agregar lectura y guardado de materias y periodos

**Estudiante asociado:** Integrante 2  
**Módulo trabajado:** Materias y periodos  
**Objetivo:** desarrollar funciones para cargar y guardar datos JSON  

```text
Continúa con el módulo materias y periodos.

Este trabajo corresponde al Integrante 2.
Módulo principal: Materias y periodos.

Desarrolla en core/materias.py las funciones para leer y guardar materias usando JSON:

- cargar_materias()
- guardar_materias(materias)

Reglas para cargar_materias():

- debe leer data/materias.json
- si el archivo no existe, debe crearlo con []
- si el archivo está vacío, debe devolver []
- si ocurre un error al leer, debe devolver []
- no debe romper el programa

Reglas para guardar_materias(materias):

- debe recibir una lista de materias
- debe guardar esa lista en data/materias.json
- el JSON debe quedar ordenado y legible

Ahora desarrolla en core/periodos.py las funciones:

- cargar_periodos()
- guardar_periodos(periodos)

Reglas para cargar_periodos():

- debe leer data/periodos.json
- si el archivo no existe, debe crearlo con []
- si el archivo está vacío, debe devolver []
- si ocurre un error al leer, debe devolver []

Reglas para guardar_periodos(periodos):

- debe recibir una lista de periodos
- debe guardar esa lista en data/periodos.json
- el JSON debe quedar ordenado y legible

Usa Python básico.
Usa solo librerías estándar como json y os si hace falta.

No modifiques otros módulos.

Al terminar, guarda este prompt completo en:
prompts/estudiante_2_prompts.md

Luego actualiza:
evidencias/estudiante_2_evidencias_resultado.md

Indicando:
- qué funciones se desarrollaron
- qué validaciones de archivo se agregaron
- qué archivos fueron modificados

Finalmente revisa los cambios y deja todo listo para commit.
```

### Prompt 4 - Agregar validaciones de materias

**Estudiante asociado:** Integrante 2  
**Módulo trabajado:** Materias y periodos  
**Objetivo:** implementar validaciones básicas del módulo materias  

```text
Continúa con el módulo materias y periodos.

Este trabajo corresponde al Integrante 2.
Módulo principal: Materias y periodos.

Desarrolla en core/materias.py las funciones de validación:

- validar_ciclo(ciclo)
- validar_estado_materia(estado)
- materia_existe(codigo_materia)

Reglas:

validar_ciclo(ciclo):
- debe verificar que el ciclo no esté vacío
- debe verificar que sea un número entero
- debe verificar que sea mayor que cero

validar_estado_materia(estado):
- debe aceptar solo activo o inactivo
- debe convertir el texto a minúsculas para evitar errores por mayúsculas

materia_existe(codigo_materia):
- debe leer data/materias.json
- debe devolver True si el código de materia existe
- debe devolver False si no existe

Mantén el código simple y fácil de explicar.
No uses clases.
No modifiques otros módulos.

Al terminar, guarda este prompt completo en:
prompts/estudiante_2_prompts.md

Luego actualiza:
evidencias/estudiante_2_evidencias_resultado.md

Indicando:
- qué validaciones se implementaron
- qué archivo fue modificado
- qué pruebas se deberían hacer después

Finalmente revisa los cambios y deja todo listo para commit.
```

### Prompt 5 - Generar código automático de materia

**Estudiante asociado:** Integrante 2  
**Módulo trabajado:** Materias y periodos  
**Objetivo:** desarrollar el código automático de materias  

```text
Continúa con el módulo materias y periodos.

Este trabajo corresponde al Integrante 2.
Módulo principal: Materias y periodos.

Desarrolla la función generar_codigo_materia() en core/materias.py.

El código debe tener este formato:

MAT001
MAT002
MAT003

Reglas:

- debe leer las materias guardadas en data/materias.json
- si no hay materias, debe devolver MAT001
- si ya hay materias, debe generar el siguiente código disponible
- no debe repetir códigos
- debe funcionar aunque existan varios registros

Ejemplo:
Si existen MAT001 y MAT002, debe generar MAT003.

Usa las funciones cargar_materias() y guardar_materias() si corresponde.
No uses código avanzado.

No modifiques otros módulos.

Al terminar, guarda este prompt completo en:
prompts/estudiante_2_prompts.md

Luego actualiza:
evidencias/estudiante_2_evidencias_resultado.md

Indicando:
- qué función se desarrolló
- qué problema resuelve
- qué archivo fue modificado

Finalmente revisa los cambios y deja todo listo para commit.
```

### Prompt 6 - Registrar y listar materias

**Estudiante asociado:** Integrante 2  
**Módulo trabajado:** Materias y periodos  
**Objetivo:** desarrollar el registro y listado de materias  

```text
Continúa con el módulo materias y periodos.

Este trabajo corresponde al Integrante 2.
Módulo principal: Materias y periodos.

Desarrolla la función registrar_materia(nombre_materia, docente, ciclo, estado) en core/materias.py.

La función debe:

- generar automáticamente el código de materia
- validar que nombre_materia no esté vacío
- validar que docente no esté vacío
- validar que ciclo sea un número entero mayor que cero
- validar que estado solo sea activo o inactivo
- guardar la materia en data/materias.json
- devolver un diccionario con resultado, mensaje y datos de la materia registrada

La materia debe guardarse con esta estructura:

{
  "codigo_materia": "MAT001",
  "nombre_materia": "Matemática",
  "docente": "Juan Pérez",
  "ciclo": 1,
  "estado": "activo"
}

Si hay error, la función debe devolver un mensaje claro y no guardar datos.

También desarrolla listar_materias().

listar_materias():
- debe leer data/materias.json
- debe devolver todas las materias registradas
- si no hay materias, debe devolver una lista vacía

No uses clases.
No modifiques otros módulos.

Al terminar, guarda este prompt completo en:
prompts/estudiante_2_prompts.md

Luego actualiza:
evidencias/estudiante_2_evidencias_resultado.md

Indicando:
- qué funciones se desarrollaron
- qué validaciones se aplicaron
- qué archivo fue modificado

Finalmente revisa los cambios y deja todo listo para commit.
```

### Prompt 7 - Buscar y actualizar materias

**Estudiante asociado:** Integrante 2  
**Módulo trabajado:** Materias y periodos  
**Objetivo:** desarrollar búsqueda y actualización segura de materias  

```text
Continúa con el módulo materias y periodos.

Este trabajo corresponde al Integrante 2.
Módulo principal: Materias y periodos.

Desarrolla en core/materias.py estas funciones:

- buscar_materia(codigo_materia)
- actualizar_materia(codigo_materia, nuevos_datos)

buscar_materia(codigo_materia):
- debe buscar una materia por su código
- si la encuentra, debe devolver sus datos
- si no existe, debe devolver un mensaje claro

actualizar_materia(codigo_materia, nuevos_datos):
- debe buscar la materia por su código
- debe permitir actualizar solo:
  - nombre_materia
  - docente
  - ciclo
  - estado

No debe permitir modificar:
- codigo_materia

Validaciones:
- la materia debe existir
- nombre_materia no debe quedar vacío
- docente no debe quedar vacío
- ciclo debe ser un número entero mayor que cero
- estado solo puede ser activo o inactivo

Después de actualizar, debe guardar los cambios en data/materias.json.

La función debe devolver:
- resultado
- mensaje
- materia actualizada, si corresponde

No modifiques otros módulos.
Mantén el código simple y fácil de defender.

Al terminar, guarda este prompt completo en:
prompts/estudiante_2_prompts.md

Luego actualiza:
evidencias/estudiante_2_evidencias_resultado.md

Indicando:
- qué funciones se desarrollaron
- qué campos permite modificar
- qué campos protege
- qué archivo fue modificado

Finalmente revisa los cambios y deja todo listo para commit.
```

### Prompt 8 - Gestionar periodos académicos

**Estudiante asociado:** Integrante 2  
**Módulo trabajado:** Materias y periodos  
**Objetivo:** desarrollar las funciones principales de periodos académicos  

```text
Continúa con el módulo materias y periodos.

Este trabajo corresponde al Integrante 2.
Módulo principal: Materias y periodos.

Desarrolla en core/periodos.py estas funciones:

- validar_estado_periodo(estado)
- periodo_existe(codigo_periodo)
- registrar_periodo(codigo_periodo, anio, nombre, estado)
- listar_periodos()
- buscar_periodo(codigo_periodo)
- obtener_periodo_activo()
- cambiar_periodo_activo(codigo_periodo)

Reglas:

validar_estado_periodo(estado):
- debe aceptar solo activo o cerrado
- debe convertir el texto a minúsculas

periodo_existe(codigo_periodo):
- debe leer data/periodos.json
- debe devolver True si existe
- debe devolver False si no existe

registrar_periodo(codigo_periodo, anio, nombre, estado):
- codigo_periodo será por ejemplo 2026-I o 2026-II
- anio debe ser numérico
- nombre no debe estar vacío
- estado solo puede ser activo o cerrado
- si se registra un periodo como activo, los demás periodos deben quedar como cerrado
- no debe permitir códigos de periodo repetidos

listar_periodos():
- debe devolver todos los periodos registrados

buscar_periodo(codigo_periodo):
- debe devolver el periodo si existe o un mensaje si no existe

obtener_periodo_activo():
- debe devolver el periodo que tenga estado activo
- si no hay periodo activo, debe devolver un mensaje claro

cambiar_periodo_activo(codigo_periodo):
- debe marcar el periodo indicado como activo
- debe cerrar los demás periodos

No uses clases.
No modifiques otros módulos.
Mantén el código simple.

Al terminar, guarda este prompt completo en:
prompts/estudiante_2_prompts.md

Luego actualiza:
evidencias/estudiante_2_evidencias_resultado.md

Indicando:
- qué funciones se desarrollaron
- cómo se controla que solo exista un periodo activo
- qué archivo fue modificado

Finalmente revisa los cambios y deja todo listo para commit.
```

### Prompt 9 - Validar materias y periodos para matrículas

**Estudiante asociado:** Integrante 2  
**Módulo trabajado:** Materias y periodos  
**Objetivo:** crear funciones de apoyo para el módulo Matrículas  

```text
Continúa con el proyecto control_academico_web.

Este trabajo corresponde al Integrante 2.
Módulo principal: Materias y periodos.
Responsabilidad adicional: apoyo al módulo Matrículas.

Ahora agrega funciones de apoyo para que el módulo de matrículas pueda validar materias y periodos.

En core/materias.py desarrolla o ajusta esta función:

- validar_materia_para_matricula(codigo_materia)

Reglas:
- debe verificar que la materia exista en data/materias.json
- debe verificar que la materia esté activa
- si puede usarse en matrícula, debe devolver resultado positivo
- si no puede usarse, debe devolver un mensaje claro

En core/periodos.py desarrolla o ajusta esta función:

- validar_periodo_para_matricula(codigo_periodo)

Reglas:
- debe verificar que el periodo exista en data/periodos.json
- debe verificar que el periodo esté activo
- si puede usarse en matrícula, debe devolver resultado positivo
- si no puede usarse, debe devolver un mensaje claro

Estas funciones serán usadas después por el módulo de matrículas.
No desarrolles el módulo completo de matrículas.
No modifiques estudiantes, notas, asistencia ni reportes.

Al terminar, guarda este prompt completo en:
prompts/estudiante_2_prompts.md

Luego actualiza:
evidencias/estudiante_2_evidencias_resultado.md

Indicando:
- qué funciones de apoyo a matrículas se crearon
- qué validan
- qué archivos fueron modificados

Finalmente revisa los cambios y deja todo listo para commit.
```

### Prompt 10 - Crear interfaz web de materias y periodos

**Estudiante asociado:** Integrante 2  
**Módulo trabajado:** Materias y periodos  
**Objetivo:** crear la página HTML del módulo Materias y periodos  

```text
Continúa con el módulo materias y periodos.

Este trabajo corresponde al Integrante 2.
Módulo principal: Materias y periodos.

Desarrolla la página web/materias.html.

La página debe tener estas secciones:

1. Título:
Gestión de materias y periodos

2. Formulario de registro de materia con estos campos:
- nombre de materia
- docente
- ciclo
- estado

3. Botón:
Guardar materia

4. Sección de búsqueda de materia:
- campo para buscar por código de materia
- botón Buscar materia

5. Tabla de materias con columnas:
- código
- nombre de materia
- docente
- ciclo
- estado
- acciones

6. Formulario de registro de periodo con estos campos:
- código de periodo
- año
- nombre
- estado

7. Botón:
Guardar periodo

8. Tabla de periodos con columnas:
- código de periodo
- año
- nombre
- estado
- acciones

9. Zona para mostrar mensajes:
- errores
- confirmaciones

Usa HTML simple.
No hagas diseño complejo.
Usa ids claros para conectar con JavaScript.

El archivo debe quedar listo para trabajar con static/materias.js.

No conectes todavía con otros módulos.
No modifiques la página de estudiantes.

Al terminar, guarda este prompt completo en:
prompts/estudiante_2_prompts.md

Luego actualiza:
evidencias/estudiante_2_evidencias_resultado.md

Indicando:
- qué página se creó
- qué elementos contiene
- qué falta conectar después

Finalmente revisa los cambios y deja todo listo para commit.
```

### Prompt 11 - Agregar lógica visual de materias y periodos

**Estudiante asociado:** Integrante 2  
**Módulo trabajado:** Materias y periodos  
**Objetivo:** crear funciones JavaScript para manejar la pantalla de materias y periodos  

```text
Continúa con el módulo materias y periodos.

Este trabajo corresponde al Integrante 2.
Módulo principal: Materias y periodos.

Desarrolla static/materias.js para manejar la página web/materias.html.

El JavaScript debe tener funciones para materias:

- obtenerDatosFormularioMateria()
- validarFormularioMateria(datos)
- mostrarMensajeMaterias(mensaje, tipo)
- limpiarFormularioMateria()
- renderizarTablaMaterias(materias)
- buscarMateriaEnTabla(valor)
- prepararActualizacionMateria(codigo_materia)

También debe tener funciones para periodos:

- obtenerDatosFormularioPeriodo()
- validarFormularioPeriodo(datos)
- limpiarFormularioPeriodo()
- renderizarTablaPeriodos(periodos)
- buscarPeriodoEnTabla(valor)
- prepararCambioPeriodoActivo(codigo_periodo)

Reglas:
- validar que los campos obligatorios no estén vacíos
- validar que ciclo y año sean números válidos
- mostrar mensajes claros en pantalla
- separar la lógica de materias y periodos
- dejar funciones preparadas para conectarse después con Python

No mezcles este archivo con otros módulos.
No desarrolles código de estudiantes, notas, asistencia, matrículas ni reportes.

Al terminar, guarda este prompt completo en:
prompts/estudiante_2_prompts.md

Luego actualiza:
evidencias/estudiante_2_evidencias_resultado.md

Indicando:
- qué funciones JavaScript se crearon
- qué parte de la pantalla controlan
- qué falta integrar después

Finalmente revisa los cambios y deja todo listo para commit.
```

### Prompt 12 - Documentar pruebas de materias y periodos

**Estudiante asociado:** Integrante 2  
**Módulo trabajado:** Materias y periodos  
**Objetivo:** crear la evidencia de pruebas del módulo Materias y periodos  

```text
Continúa con el módulo materias y periodos.

Este trabajo corresponde al Integrante 2.
Módulo principal: Materias y periodos.
Responsabilidad adicional: apoyo al módulo Matrículas.

Crea un archivo de pruebas dentro de evidencias llamado:

casos_prueba_materias_periodos.md

El archivo debe incluir una tabla con:

- número de caso
- módulo
- acción realizada
- datos de entrada
- resultado esperado
- resultado obtenido
- observación

Incluye estos casos de materias:

1. Registrar materia correctamente.
2. Registrar materia con nombre vacío.
3. Registrar materia con docente vacío.
4. Registrar materia con ciclo inválido.
5. Registrar materia con estado inválido.
6. Listar materias registradas.
7. Buscar materia por código existente.
8. Buscar materia inexistente.
9. Actualizar materia existente.
10. Intentar actualizar materia inexistente.
11. Cambiar estado de materia de activo a inactivo.

Incluye estos casos de periodos:

12. Registrar periodo correctamente.
13. Registrar periodo con año inválido.
14. Registrar periodo con nombre vacío.
15. Registrar periodo con estado inválido.
16. Registrar periodo repetido.
17. Activar un periodo.
18. Verificar que solo exista un periodo activo.
19. Buscar periodo existente.
20. Buscar periodo inexistente.

Incluye estos casos de apoyo a matrículas:

21. Validar materia activa para matrícula.
22. Intentar validar materia inactiva para matrícula.
23. Validar periodo activo para matrícula.
24. Intentar validar periodo cerrado para matrícula.

Agrega al final una sección llamada:

Conclusión del módulo

En esa sección indica si el módulo materias y periodos quedó listo para integrarse con matrículas y los demás módulos.

Al terminar, guarda este prompt completo en:
prompts/estudiante_2_prompts.md

Luego actualiza:
evidencias/estudiante_2_evidencias_resultado.md

Indicando:
- que se creó la evidencia de pruebas
- qué casos cubre
- qué falta verificar en la integración

Finalmente revisa los cambios y deja todo listo para commit.
```
