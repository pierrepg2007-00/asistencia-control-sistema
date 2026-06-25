"""Funciones base para la gestión de materias."""

import json
import os


CARPETA_BASE = os.path.dirname(os.path.dirname(__file__))
ARCHIVO_MATERIAS = os.path.join(CARPETA_BASE, "data", "materias.json")


def cargar_materias():
    """Carga y devuelve la lista de materias guardada en JSON."""
    try:
        with open(ARCHIVO_MATERIAS, "r", encoding="utf-8") as archivo:
            contenido = archivo.read().strip()
    except FileNotFoundError:
        try:
            guardar_materias([])
        except OSError:
            pass
        return []
    except OSError:
        return []

    if not contenido:
        return []

    try:
        materias = json.loads(contenido)
        if isinstance(materias, list):
            return materias
    except json.JSONDecodeError:
        pass

    return []


def guardar_materias(materias):
    """Guarda la lista de materias en el archivo JSON."""
    os.makedirs(os.path.dirname(ARCHIVO_MATERIAS), exist_ok=True)

    with open(ARCHIVO_MATERIAS, "w", encoding="utf-8") as archivo:
        json.dump(materias, archivo, ensure_ascii=False, indent=4)


def generar_codigo_materia():
    """Genera el código automático de materia. Pendiente de completar."""
    pass


def registrar_materia(nombre_materia, docente, ciclo, estado):
    """Registra una materia. Pendiente de completar."""
    pass


def listar_materias():
    """Lista las materias registradas. Pendiente de completar."""
    return cargar_materias()


def buscar_materia(codigo_materia):
    """Busca una materia por código. Pendiente de completar."""
    pass


def actualizar_materia(codigo_materia, nuevos_datos):
    """Actualiza una materia. Pendiente de completar."""
    pass


def validar_ciclo(ciclo):
    """Valida el ciclo de una materia. Pendiente de completar."""
    pass


def validar_estado_materia(estado):
    """Valida el estado de una materia. Pendiente de completar."""
    pass


def materia_existe(codigo_materia):
    """Verifica si una materia existe. Pendiente de completar."""
    pass
