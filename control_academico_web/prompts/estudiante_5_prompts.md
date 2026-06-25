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
