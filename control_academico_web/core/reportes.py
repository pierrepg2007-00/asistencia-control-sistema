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
    return []


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
