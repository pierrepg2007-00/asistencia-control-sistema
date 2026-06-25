"""Funciones base para la generacion de reportes academicos."""

import json
import os


CARPETA_BASE = os.path.dirname(os.path.dirname(__file__))
ARCHIVO_MATRICULAS = os.path.join(CARPETA_BASE, "data", "matriculas.json")
ARCHIVO_ESTUDIANTES = os.path.join(CARPETA_BASE, "data", "estudiantes.json")
ARCHIVO_MATERIAS = os.path.join(CARPETA_BASE, "data", "materias.json")
ARCHIVO_PERIODOS = os.path.join(CARPETA_BASE, "data", "periodos.json")
ARCHIVO_NOTAS = os.path.join(CARPETA_BASE, "data", "notas.json")
ARCHIVO_ASISTENCIAS = os.path.join(CARPETA_BASE, "data", "asistencias.json")
CARPETA_REPORTES = os.path.join(CARPETA_BASE, "reportes_generados")


def reporte_estudiantes_por_materia(codigo_materia, codigo_periodo):
    """Devuelve la lista de estudiantes matriculados en una materia y periodo."""
    codigo_materia = (codigo_materia or "").strip().upper()
    codigo_periodo = (codigo_periodo or "").strip().upper()
    resultado = []

    # Cargar matriculas
    matriculas = []
    try:
        with open(ARCHIVO_MATRICULAS, "r", encoding="utf-8") as archivo:
            contenido = archivo.read().strip()
        if contenido:
            matriculas = json.loads(contenido)
    except (FileNotFoundError, OSError, json.JSONDecodeError):
        pass

    # Cargar estudiantes
    datos_estudiantes = {}
    try:
        with open(ARCHIVO_ESTUDIANTES, "r", encoding="utf-8") as archivo:
            contenido = archivo.read().strip()
        if contenido:
            estudiantes = json.loads(contenido)
            for estudiante in estudiantes:
                datos_estudiantes[estudiante.get("codigo")] = estudiante
    except (FileNotFoundError, OSError, json.JSONDecodeError):
        pass

    # Cargar materias
    nombre_materia = ""
    try:
        with open(ARCHIVO_MATERIAS, "r", encoding="utf-8") as archivo:
            contenido = archivo.read().strip()
        if contenido:
            materias = json.loads(contenido)
            for materia in materias:
                if materia.get("codigo_materia") == codigo_materia:
                    nombre_materia = materia.get("nombre_materia", "")
                    break
    except (FileNotFoundError, OSError, json.JSONDecodeError):
        pass

    for matricula in matriculas:
        if (matricula.get("codigo_materia") == codigo_materia
                and matricula.get("codigo_periodo") == codigo_periodo):
            estado_mat = matricula.get("estado", "")
            if estado_mat and estado_mat != "activa":
                continue

            cod_est = matricula.get("codigo_estudiante", "")
            info = datos_estudiantes.get(cod_est, {})

            entrada = {
                "codigo_materia": codigo_materia,
                "nombre_materia": nombre_materia,
                "codigo_periodo": codigo_periodo,
                "codigo_estudiante": cod_est,
                "nombres": info.get("nombres", ""),
                "apellidos": info.get("apellidos", ""),
                "dni": info.get("dni", ""),
                "estado_matricula": estado_mat,
            }
            resultado.append(entrada)

    if not resultado:
        return []

    return resultado


def reporte_notas_por_materia(codigo_materia, codigo_periodo):
    """Devuelve el detalle de notas de cada estudiante en una materia y periodo."""
    codigo_materia = (codigo_materia or "").strip().upper()
    codigo_periodo = (codigo_periodo or "").strip().upper()
    detalle = []

    # Cargar notas
    notas = []
    try:
        with open(ARCHIVO_NOTAS, "r", encoding="utf-8") as archivo:
            contenido = archivo.read().strip()
        if contenido:
            notas = json.loads(contenido)
    except (FileNotFoundError, OSError, json.JSONDecodeError):
        pass

    # Cargar estudiantes
    datos_estudiantes = {}
    try:
        with open(ARCHIVO_ESTUDIANTES, "r", encoding="utf-8") as archivo:
            contenido = archivo.read().strip()
        if contenido:
            estudiantes = json.loads(contenido)
            for estudiante in estudiantes:
                datos_estudiantes[estudiante.get("codigo")] = estudiante
    except (FileNotFoundError, OSError, json.JSONDecodeError):
        pass

    # Cargar materias
    nombre_materia = ""
    try:
        with open(ARCHIVO_MATERIAS, "r", encoding="utf-8") as archivo:
            contenido = archivo.read().strip()
        if contenido:
            materias = json.loads(contenido)
            for materia in materias:
                if materia.get("codigo_materia") == codigo_materia:
                    nombre_materia = materia.get("nombre_materia", "")
                    break
    except (FileNotFoundError, OSError, json.JSONDecodeError):
        pass

    for nota in notas:
        if (nota.get("codigo_materia") == codigo_materia
                and nota.get("codigo_periodo") == codigo_periodo):
            cod_est = nota.get("codigo_estudiante", "")
            info = datos_estudiantes.get(cod_est, {})

            entrada = {
                "codigo_estudiante": cod_est,
                "nombres": info.get("nombres", ""),
                "apellidos": info.get("apellidos", ""),
                "codigo_materia": codigo_materia,
                "nombre_materia": nombre_materia,
                "codigo_periodo": codigo_periodo,
                "nota1": nota.get("nota1"),
                "nota2": nota.get("nota2"),
                "nota3": nota.get("nota3"),
                "promedio": nota.get("promedio"),
                "estado_final": nota.get("estado_final"),
            }
            detalle.append(entrada)

    total_estudiantes = len(detalle)
    aprobados = sum(1 for d in detalle if d.get("estado_final") == "aprobado")
    desaprobados = sum(1 for d in detalle if d.get("estado_final") == "desaprobado")

    promedio_general = 0
    promedios = [d.get("promedio") for d in detalle if d.get("promedio") is not None]
    if promedios:
        promedio_general = round(sum(promedios) / len(promedios), 2)

    return {
        "detalle": detalle,
        "total_estudiantes": total_estudiantes,
        "aprobados": aprobados,
        "desaprobados": desaprobados,
        "promedio_general": promedio_general,
    }


def reporte_asistencia_por_materia(codigo_materia, codigo_periodo):
    """Devuelve el resumen de asistencia de cada estudiante en una materia y periodo."""
    codigo_materia = (codigo_materia or "").strip().upper()
    codigo_periodo = (codigo_periodo or "").strip().upper()
    resultado = []

    # Cargar asistencias
    asistencias = []
    try:
        with open(ARCHIVO_ASISTENCIAS, "r", encoding="utf-8") as archivo:
            contenido = archivo.read().strip()
        if contenido:
            asistencias = json.loads(contenido)
    except (FileNotFoundError, OSError, json.JSONDecodeError):
        pass

    # Cargar estudiantes
    datos_estudiantes = {}
    try:
        with open(ARCHIVO_ESTUDIANTES, "r", encoding="utf-8") as archivo:
            contenido = archivo.read().strip()
        if contenido:
            estudiantes = json.loads(contenido)
            for estudiante in estudiantes:
                datos_estudiantes[estudiante.get("codigo")] = estudiante
    except (FileNotFoundError, OSError, json.JSONDecodeError):
        pass

    # Filtrar asistencias por materia y periodo
    asistencias_filtradas = []
    for asistencia in asistencias:
        if (asistencia.get("codigo_materia") == codigo_materia
                and asistencia.get("codigo_periodo") == codigo_periodo):
            asistencias_filtradas.append(asistencia)

    if not asistencias_filtradas:
        return []

    # Agrupar por estudiante
    datos_por_estudiante = {}
    for asistencia in asistencias_filtradas:
        cod_est = asistencia.get("codigo_estudiante", "")
        if cod_est not in datos_por_estudiante:
            datos_por_estudiante[cod_est] = []
        datos_por_estudiante[cod_est].append(asistencia)

    # Calcular resumen por estudiante
    for cod_est, registros in datos_por_estudiante.items():
        total_clases = len(registros)
        asistencias_count = 0
        faltas_count = 0

        for registro in registros:
            estado = registro.get("estado_asistencia", "").lower()
            if estado in ["presente", "tarde", "justificado"]:
                asistencias_count += 1
            elif estado == "falta":
                faltas_count += 1

        porcentaje = 0
        if total_clases > 0:
            porcentaje = round((asistencias_count / total_clases) * 100, 2)

        info = datos_estudiantes.get(cod_est, {})

        resultado.append({
            "codigo_estudiante": cod_est,
            "nombres": info.get("nombres", ""),
            "apellidos": info.get("apellidos", ""),
            "codigo_materia": codigo_materia,
            "codigo_periodo": codigo_periodo,
            "total_clases": total_clases,
            "asistencias": asistencias_count,
            "faltas": faltas_count,
            "porcentaje_asistencia": porcentaje,
        })

    return resultado


def reporte_estudiantes_en_riesgo():
    """Identifica estudiantes en riesgo por nota baja o baja asistencia."""
    return []


def exportar_reporte_txt(nombre_reporte, datos):
    """Genera un archivo de texto con el reporte en la carpeta reportes_generados."""
    return {"resultado": False, "mensaje": "Funcion pendiente de desarrollo."}
