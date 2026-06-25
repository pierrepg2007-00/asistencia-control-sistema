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

### Prompt 2 - Organizar prompts y evidencias por estudiante

**Estudiante asociado:** Integrante 1  
**Módulo trabajado:** Estudiantes  
**Objetivo:** organizar los archivos de prompts y evidencias del equipo  

```text
Continúa con el proyecto control_academico_web.

Este trabajo corresponde al Integrante 1.
Módulo principal: Estudiantes.

Ahora organiza correctamente los archivos de prompts y evidencias por estudiante.

Dentro de prompts/ deben existir:

- estudiante_1_prompts.md
- estudiante_2_prompts.md
- estudiante_3_prompts.md
- estudiante_4_prompts.md
- estudiante_5_prompts.md

Cada archivo debe tener una estructura para guardar los prompts usados por ese estudiante.

Dentro de evidencias/ deben existir:

- estudiante_1_evidencias_resultado.md
- estudiante_2_evidencias_resultado.md
- estudiante_3_evidencias_resultado.md
- estudiante_4_evidencias_resultado.md
- estudiante_5_evidencias_resultado.md
- matriz_roles.md
- bitacora_equipo.md
- casos_prueba_generales.md
- declaracion_uso_ia.md

No borres contenido existente.
Si ya hay archivos anteriores como prompts/integrante_1/prompts_utilizados.md, conserva la información y pásala también a prompts/estudiante_1_prompts.md.

Al terminar, guarda este prompt completo en:
prompts/estudiante_1_prompts.md

Luego actualiza:
evidencias/estudiante_1_evidencias_resultado.md

Indicando:
- qué archivos de prompts se crearon
- qué archivos de evidencias se crearon
- cómo quedó organizada la evidencia del Integrante 1

Finalmente revisa los cambios y deja todo listo para commit.
```

### Prompt 6 - Generar código automático de estudiante

**Estudiante asociado:** Integrante 1  
**Módulo trabajado:** Estudiantes  
**Objetivo:** desarrollar la función que genera códigos únicos de estudiantes  

```text
Continúa con el módulo estudiantes.

Este trabajo corresponde al Integrante 1.
Módulo principal: Estudiantes.

Desarrolla la función generar_codigo_estudiante() en core/estudiantes.py.

El código debe tener este formato:

EST001
EST002
EST003

Reglas:

- debe leer los estudiantes guardados en data/estudiantes.json
- si no hay estudiantes, debe devolver EST001
- si ya hay estudiantes, debe generar el siguiente código disponible
- no debe repetir códigos
- debe funcionar aunque existan varios registros

Ejemplo:
Si existen EST001 y EST002, debe generar EST003.

Usa las funciones cargar_estudiantes() y guardar_estudiantes() si corresponde.
No uses código avanzado.

Al terminar, guarda este prompt completo en:
prompts/estudiante_1_prompts.md

Luego actualiza:
evidencias/estudiante_1_evidencias_resultado.md

Indicando:
- qué función se desarrolló
- qué problema resuelve
- qué archivo fue modificado

Finalmente revisa los cambios y deja todo listo para commit.
```
