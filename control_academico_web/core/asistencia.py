"""Funciones base para la gestion de asistencia."""

import json
import os
from datetime import datetime


CARPETA_BASE = os.path.dirname(os.path.dirname(__file__))
ARCHIVO_ASISTENCIAS = os.path.join(CARPETA_BASE, "data", "asistencias.json")
ARCHIVO_MATRICULAS = os.path.join(CARPETA_BASE, "data", "matriculas.json")
ARCHIVO_ESTUDIANTES = os.path.join(CARPETA_BASE, "data", "estudiantes.json")
ARCHIVO_MATERIAS = os.path.join(CARPETA_BASE, "data", "materias.json")


def cargar_lista_json(ruta_archivo):
    """Carga una lista desde un archivo JSON, devolviendo [] ante errores."""
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.read().strip()
    except (FileNotFoundError, OSError):
        return []

    if not contenido:
        return []

    try:
        datos = json.loads(contenido)
        if isinstance(datos, list):
            return datos
    except json.JSONDecodeError:
        pass

    return []


def cargar_asistencias():
    """Carga y devuelve la lista de asistencias guardada en JSON."""
    try:
        with open(ARCHIVO_ASISTENCIAS, "r", encoding="utf-8") as archivo:
            contenido = archivo.read().strip()
    except FileNotFoundError:
        try:
            guardar_asistencias([])
        except OSError:
            pass
        return []
    except OSError:
        return []

    if not contenido:
        return []

    try:
        asistencias = json.loads(contenido)
        if isinstance(asistencias, list):
            return asistencias
    except json.JSONDecodeError:
        pass

    return []


def guardar_asistencias(asistencias):
    """Guarda la lista de asistencias en el archivo JSON."""
    os.makedirs(os.path.dirname(ARCHIVO_ASISTENCIAS), exist_ok=True)

    with open(ARCHIVO_ASISTENCIAS, "w", encoding="utf-8") as archivo:
        json.dump(asistencias, archivo, ensure_ascii=False, indent=4)


def validar_estado_asistencia(estado):
    """Valida que el estado de asistencia sea uno de los permitidos."""
    if not estado:
        return False

    estado = estado.strip().lower()
    estados_validos = ["presente", "tarde", "falta", "justificado"]

    if estado in estados_validos:
        return True

    return False


def validar_fecha(fecha):
    """Valida que la fecha tenga el formato YYYY-MM-DD."""
    if not fecha:
        return False

    try:
        datetime.strptime(fecha, "%Y-%m-%d")
        return True
    except (ValueError, TypeError):
        return False


def verificar_matricula_para_asistencia(codigo_estudiante, codigo_materia, codigo_periodo):
    """Verifica que el estudiante este matriculado antes de registrar asistencia."""
    codigo_estudiante = (codigo_estudiante or "").strip().upper()
    codigo_materia = (codigo_materia or "").strip().upper()
    codigo_periodo = (codigo_periodo or "").strip().upper()
    matriculas = cargar_lista_json(ARCHIVO_MATRICULAS)

    for matricula in matriculas:
        misma_matricula = (
            matricula.get("codigo_estudiante") == codigo_estudiante
            and matricula.get("codigo_materia") == codigo_materia
            and matricula.get("codigo_periodo") == codigo_periodo
        )

        if misma_matricula:
            estado = matricula.get("estado", "activo").strip().lower()

            if estado == "activo":
                return {
                    "resultado": True,
                    "mensaje": "Matricula activa encontrada.",
                    "datos": matricula,
                }

            return {
                "resultado": False,
                "mensaje": "La matricula existe, pero no esta activa.",
                "datos": matricula,
            }

    return {
        "resultado": False,
        "mensaje": "El estudiante no esta matriculado en esa materia y periodo.",
        "datos": None,
    }


def asistencia_duplicada(codigo_estudiante, codigo_materia, codigo_periodo, fecha):
    """Verifica si ya existe asistencia para el mismo estudiante, materia, periodo y fecha."""
    pass


def registrar_asistencia(codigo_estudiante, codigo_materia, codigo_periodo, fecha, estado_asistencia):
    """Registra la asistencia de un estudiante con validaciones."""
    pass


def listar_asistencias():
    """Devuelve todas las asistencias registradas."""
    pass


def listar_asistencia_por_estudiante(codigo_estudiante):
    """Devuelve todas las asistencias de un estudiante."""
    pass


def listar_asistencia_por_materia(codigo_materia, codigo_periodo, fecha=None):
    """Devuelve las asistencias de una materia y periodo. Puede filtrar por fecha."""
    pass


def calcular_porcentaje_asistencia(codigo_estudiante, codigo_materia, codigo_periodo):
    """Calcula el porcentaje de asistencia de un estudiante en una materia y periodo."""
    pass


def listar_matriculados_para_asistencia(codigo_materia, codigo_periodo):
    """Devuelve los estudiantes matriculados en una materia y periodo para tomar asistencia."""
    pass
