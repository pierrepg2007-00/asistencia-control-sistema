# Estudiante 1 - Prompts utilizados

## Datos del estudiante

- Estudiante asociado: Integrante 1
- Módulo principal: Estudiantes
- Responsabilidad adicional: estructura inicial del proyecto

## Prompts usados

A partir de ahora, cada vez que se trabaje un prompt del Integrante 1, se debe agregar en este archivo con esta estructura:

### Prompt X - Título del prompt

**Estudiante asociado:** Integrante 1  
**Módulo trabajado:** Estudiantes / estructura inicial  
**Objetivo:** breve descripción del objetivo del prompt  

```text
Aquí se debe pegar el prompt completo utilizado.
```

### Prompt 1 - Estructura base y guías iniciales

**Estudiante asociado:** Integrante 1  
**Módulo trabajado:** Estudiantes / estructura inicial  
**Objetivo:** revisar la base general del proyecto y crear las guías iniciales  

```text
Trabaja como agente de desarrollo dentro del proyecto control_academico_web.

Este trabajo corresponde al Integrante 1.
Módulo principal: Estudiantes.
Responsabilidad adicional: estructura inicial del proyecto.

Primero revisa la estructura actual del proyecto y corrige lo necesario sin borrar archivos existentes.

Debes asegurar que existan estas carpetas:

- data/
- core/
- web/
- static/
- evidencias/
- reportes_generados/
- prompts/

También crea o corrige estos archivos generales:

- AGENTS.md
- README.md

El archivo AGENTS.md debe incluir:
- objetivo del proyecto
- tecnologías usadas
- estructura de carpetas
- reglas de desarrollo
- módulos del sistema
- cómo ejecutar el proyecto
- definición de terminado

El README.md debe incluir:
- nombre del proyecto
- objetivo
- módulos
- tecnologías usadas
- estructura general
- integrantes y módulos asignados

No desarrolles todavía lógica completa de estudiantes.
Este commit es solo para dejar lista la base general del proyecto.

Al terminar, guarda este prompt completo en:
prompts/estudiante_1_prompts.md

Luego actualiza:
evidencias/estudiante_1_evidencias_resultado.md

Indicando:
- qué carpetas se revisaron o crearon
- qué archivos se crearon o corrigieron
- qué falta desarrollar después

Finalmente revisa los cambios realizados y deja todo listo para commit.
```

## Instrucción final para los próximos prompts

Al final de cada prompt del Integrante 1 se agregará este bloque:

````text
Antes de terminar, guarda este prompt completo en:

prompts/estudiante_1_prompts.md

Debes agregarlo debajo de los prompts anteriores, sin borrar el contenido existente.

Usa este formato:

### Prompt X - Título del prompt
**Estudiante asociado:** Integrante 1
**Módulo trabajado:** Estudiantes
**Objetivo:** escribe brevemente qué se hizo con este prompt

```text
Pega aquí este prompt completo.
```
````

### Prompt 2 - Crear archivos base para estudiantes

**Estudiante asociado:** Integrante 1  
**Módulo trabajado:** Estudiantes  
**Objetivo:** crear los archivos iniciales del módulo estudiantes  

````text
Ya se creó la estructura inicial de carpetas del proyecto control_academico_web.

Ahora necesito que empieces con el módulo de estudiantes.

Este trabajo corresponde al Estudiante 1.
Módulo principal del Estudiante 1: Estudiantes.
Responsabilidad adicional del Estudiante 1: estructura inicial del proyecto.

Crea únicamente los archivos necesarios para este módulo:

- data/estudiantes.json
- core/estudiantes.py
- web/estudiantes.html
- static/estudiantes.js

El archivo data/estudiantes.json debe iniciar con una lista vacía [].

En core/estudiantes.py deja preparada la estructura base del módulo con estas funciones, aunque algunas todavía queden incompletas:

- cargar_estudiantes()
- guardar_estudiantes(estudiantes)
- generar_codigo_estudiante()
- registrar_estudiante(nombres, apellidos, dni, correo, estado)
- listar_estudiantes()
- buscar_estudiante(valor)
- actualizar_estudiante(codigo, nuevos_datos)
- validar_dni(dni)
- validar_correo(correo)
- dni_repetido(dni)
- estudiante_existe(codigo)

No desarrolles otros módulos.
No crees archivos para materias, notas, asistencia, matrículas ni reportes.

Antes de terminar, guarda este prompt completo en:

prompts/estudiante_1_prompts.md

Debes agregarlo debajo de los prompts anteriores, sin borrar el contenido existente.

Usa este formato:

### Prompt 2 - Crear archivos base para estudiantes
**Estudiante asociado:** Integrante 1
**Módulo trabajado:** Estudiantes
**Objetivo:** crear los archivos iniciales del módulo estudiantes

```text
Pega aquí este prompt completo.
```
````
