"""Funciones base para la gestión de periodos académicos."""

import json
import os


CARPETA_BASE = os.path.dirname(os.path.dirname(__file__))
ARCHIVO_PERIODOS = os.path.join(CARPETA_BASE, "data", "periodos.json")


def cargar_periodos():
    """Carga y devuelve la lista de periodos guardada en JSON."""
    try:
        with open(ARCHIVO_PERIODOS, "r", encoding="utf-8") as archivo:
            contenido = archivo.read().strip()
    except FileNotFoundError:
        try:
            guardar_periodos([])
        except OSError:
            pass
        return []
    except OSError:
        return []

    if not contenido:
        return []

    try:
        periodos = json.loads(contenido)
        if isinstance(periodos, list):
            return periodos
    except json.JSONDecodeError:
        pass

    return []


def guardar_periodos(periodos):
    """Guarda la lista de periodos en el archivo JSON."""
    os.makedirs(os.path.dirname(ARCHIVO_PERIODOS), exist_ok=True)

    with open(ARCHIVO_PERIODOS, "w", encoding="utf-8") as archivo:
        json.dump(periodos, archivo, ensure_ascii=False, indent=4)


def registrar_periodo(codigo_periodo, anio, nombre, estado):
    """Registra un periodo académico con validaciones básicas."""
    codigo_periodo = (codigo_periodo or "").strip().upper()
    nombre = (nombre or "").strip()
    estado = (estado or "").strip().lower()

    if not codigo_periodo:
        return {
            "resultado": False,
            "mensaje": "El código del periodo no puede estar vacío.",
            "datos": None,
        }

    if periodo_existe(codigo_periodo):
        return {
            "resultado": False,
            "mensaje": "El código del periodo ya está registrado.",
            "datos": None,
        }

    try:
        anio_entero = int(anio)
    except (ValueError, TypeError):
        return {
            "resultado": False,
            "mensaje": "El año debe ser numérico.",
            "datos": None,
        }

    if not nombre:
        return {
            "resultado": False,
            "mensaje": "El nombre del periodo no puede estar vacío.",
            "datos": None,
        }

    if not validar_estado_periodo(estado):
        return {
            "resultado": False,
            "mensaje": "El estado debe ser activo o cerrado.",
            "datos": None,
        }

    periodos = cargar_periodos()

    if estado == "activo":
        for periodo in periodos:
            periodo["estado"] = "cerrado"

    periodo = {
        "codigo_periodo": codigo_periodo,
        "anio": anio_entero,
        "nombre": nombre,
        "estado": estado,
    }

    periodos.append(periodo)
    guardar_periodos(periodos)

    return {
        "resultado": True,
        "mensaje": "Periodo registrado correctamente.",
        "datos": periodo,
    }


def listar_periodos():
    """Devuelve todos los periodos registrados."""
    return cargar_periodos()


def buscar_periodo(codigo_periodo):
    """Busca un periodo por su código."""
    codigo_periodo = (codigo_periodo or "").strip().upper()

    for periodo in cargar_periodos():
        if periodo.get("codigo_periodo") == codigo_periodo:
            return {
                "resultado": True,
                "mensaje": "Periodo encontrado.",
                "datos": periodo,
            }

    return {
        "resultado": False,
        "mensaje": "No existe un periodo con ese código.",
        "datos": None,
    }


def obtener_periodo_activo():
    """Devuelve el periodo que se encuentra activo."""
    for periodo in cargar_periodos():
        if periodo.get("estado") == "activo":
            return {
                "resultado": True,
                "mensaje": "Periodo activo encontrado.",
                "datos": periodo,
            }

    return {
        "resultado": False,
        "mensaje": "No hay un periodo activo registrado.",
        "datos": None,
    }


def cambiar_periodo_activo(codigo_periodo):
    """Marca un periodo como activo y cierra los demás."""
    codigo_periodo = (codigo_periodo or "").strip().upper()
    periodos = cargar_periodos()
    periodo_encontrado = None

    for periodo in periodos:
        if periodo.get("codigo_periodo") == codigo_periodo:
            periodo_encontrado = periodo
            periodo["estado"] = "activo"
        else:
            periodo["estado"] = "cerrado"

    if not periodo_encontrado:
        return {
            "resultado": False,
            "mensaje": "No existe un periodo con ese código.",
            "datos": None,
        }

    guardar_periodos(periodos)

    return {
        "resultado": True,
        "mensaje": "Periodo activo actualizado correctamente.",
        "datos": periodo_encontrado,
    }


def validar_estado_periodo(estado):
    """Valida que el estado del periodo sea activo o cerrado."""
    estado = (estado or "").strip().lower()
    return estado in ["activo", "cerrado"]


def periodo_existe(codigo_periodo):
    """Devuelve True cuando existe un periodo con el código indicado."""
    codigo_periodo = (codigo_periodo or "").strip().upper()

    for periodo in cargar_periodos():
        if periodo.get("codigo_periodo") == codigo_periodo:
            return True

    return False


def validar_periodo_para_matricula(codigo_periodo):
    """Valida si un periodo puede usarse en una matrícula."""
    resultado_busqueda = buscar_periodo(codigo_periodo)

    if not resultado_busqueda["resultado"]:
        return {
            "resultado": False,
            "mensaje": "El periodo no existe.",
            "datos": None,
        }

    periodo = resultado_busqueda["datos"]

    if periodo.get("estado") != "activo":
        return {
            "resultado": False,
            "mensaje": "El periodo no está activo para matrícula.",
            "datos": periodo,
        }

    return {
        "resultado": True,
        "mensaje": "El periodo puede usarse en matrícula.",
        "datos": periodo,
    }
