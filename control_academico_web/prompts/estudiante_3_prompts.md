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
