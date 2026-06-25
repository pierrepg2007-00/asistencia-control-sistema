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
