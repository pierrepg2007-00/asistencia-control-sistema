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
