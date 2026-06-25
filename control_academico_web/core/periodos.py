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
    """Registra un periodo académico. Pendiente de completar."""
    pass


def listar_periodos():
    """Lista los periodos registrados. Pendiente de completar."""
    return cargar_periodos()


def buscar_periodo(codigo_periodo):
    """Busca un periodo por código. Pendiente de completar."""
    pass


def obtener_periodo_activo():
    """Obtiene el periodo activo. Pendiente de completar."""
    pass


def cambiar_periodo_activo(codigo_periodo):
    """Cambia el periodo activo. Pendiente de completar."""
    pass


def validar_estado_periodo(estado):
    """Valida el estado de un periodo. Pendiente de completar."""
    pass


def periodo_existe(codigo_periodo):
    """Verifica si un periodo existe. Pendiente de completar."""
    pass
