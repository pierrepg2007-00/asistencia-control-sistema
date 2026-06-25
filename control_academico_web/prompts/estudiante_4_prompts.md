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
