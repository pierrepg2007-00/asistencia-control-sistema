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
    codigo_estudiante = (codigo_estudiante or "").strip().upper()
    codigo_materia = (codigo_materia or "").strip().upper()
    codigo_periodo = (codigo_periodo or "").strip().upper()

    for asistencia in cargar_asistencias():
        if (
            asistencia.get("codigo_estudiante") == codigo_estudiante
            and asistencia.get("codigo_materia") == codigo_materia
            and asistencia.get("codigo_periodo") == codigo_periodo
            and asistencia.get("fecha") == fecha
        ):
            return True

    return False


def registrar_asistencia(codigo_estudiante, codigo_materia, codigo_periodo, fecha, estado_asistencia):
    """Registra la asistencia de un estudiante con validaciones."""
    codigo_estudiante = (codigo_estudiante or "").strip().upper()
    codigo_materia = (codigo_materia or "").strip().upper()
    codigo_periodo = (codigo_periodo or "").strip().upper()
    fecha = (fecha or "").strip()
    estado_asistencia = (estado_asistencia or "").strip().lower()

    if not codigo_estudiante:
        return {"resultado": False, "mensaje": "El codigo de estudiante no puede estar vacio.", "datos": None}

    if not codigo_materia:
        return {"resultado": False, "mensaje": "El codigo de materia no puede estar vacio.", "datos": None}

    if not codigo_periodo:
        return {"resultado": False, "mensaje": "El codigo de periodo no puede estar vacio.", "datos": None}

    if not fecha:
        return {"resultado": False, "mensaje": "La fecha no puede estar vacia.", "datos": None}

    if not validar_fecha(fecha):
        return {"resultado": False, "mensaje": "La fecha debe tener el formato YYYY-MM-DD.", "datos": None}

    if not validar_estado_asistencia(estado_asistencia):
        return {"resultado": False, "mensaje": "El estado de asistencia debe ser: presente, tarde, falta o justificado.", "datos": None}

    resultado_matricula = verificar_matricula_para_asistencia(
        codigo_estudiante,
        codigo_materia,
        codigo_periodo,
    )

    if not resultado_matricula["resultado"]:
        return {"resultado": False, "mensaje": resultado_matricula["mensaje"], "datos": None}

    if asistencia_duplicada(codigo_estudiante, codigo_materia, codigo_periodo, fecha):
        return {"resultado": False, "mensaje": "Ya existe una asistencia registrada para ese estudiante en esa fecha.", "datos": None}

    asistencias = cargar_asistencias()

    registro = {
        "codigo_estudiante": codigo_estudiante,
        "codigo_materia": codigo_materia,
        "codigo_periodo": codigo_periodo,
        "fecha": fecha,
        "estado_asistencia": estado_asistencia,
    }

    asistencias.append(registro)
    guardar_asistencias(asistencias)

    return {
        "resultado": True,
        "mensaje": "Asistencia registrada correctamente.",
        "datos": registro,
    }


def listar_asistencias():
    """Devuelve todas las asistencias registradas."""
    return cargar_asistencias()


def listar_asistencia_por_estudiante(codigo_estudiante):
    """Devuelve todas las asistencias de un estudiante."""
    codigo_estudiante = (codigo_estudiante or "").strip().upper()
    asistencias_estudiante = []

    for asistencia in cargar_asistencias():
        if asistencia.get("codigo_estudiante") == codigo_estudiante:
            asistencias_estudiante.append(asistencia)

    return asistencias_estudiante


def listar_asistencia_por_materia(codigo_materia, codigo_periodo, fecha=None):
    """Devuelve las asistencias de una materia y periodo. Puede filtrar por fecha."""
    codigo_materia = (codigo_materia or "").strip().upper()
    codigo_periodo = (codigo_periodo or "").strip().upper()
    asistencias_materia = []

    for asistencia in cargar_asistencias():
        coincide_materia_periodo = (
            asistencia.get("codigo_materia") == codigo_materia
            and asistencia.get("codigo_periodo") == codigo_periodo
        )

        if coincide_materia_periodo:
            if fecha:
                if asistencia.get("fecha") == fecha:
                    asistencias_materia.append(asistencia)
            else:
                asistencias_materia.append(asistencia)

    return asistencias_materia


def calcular_porcentaje_asistencia(codigo_estudiante, codigo_materia, codigo_periodo):
    """Calcula el porcentaje de asistencia de un estudiante en una materia y periodo."""
    pass


def listar_matriculados_para_asistencia(codigo_materia, codigo_periodo):
    """Devuelve los estudiantes matriculados en una materia y periodo para tomar asistencia."""
    pass
