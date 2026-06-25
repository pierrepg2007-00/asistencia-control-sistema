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
    return {"detalle": [], "total_estudiantes": 0, "aprobados": 0, "desaprobados": 0, "promedio_general": 0}


def reporte_asistencia_por_materia(codigo_materia, codigo_periodo):
    """Devuelve el resumen de asistencia de cada estudiante en una materia y periodo."""
    return []


def reporte_estudiantes_en_riesgo():
    """Identifica estudiantes en riesgo por nota baja o baja asistencia."""
    return []


def exportar_reporte_txt(nombre_reporte, datos):
    """Genera un archivo de texto con el reporte en la carpeta reportes_generados."""
    return {"resultado": False, "mensaje": "Funcion pendiente de desarrollo."}
