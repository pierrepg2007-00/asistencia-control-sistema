"""Funciones base para la gestión de estudiantes."""

import json
from pathlib import Path


ARCHIVO_ESTUDIANTES = Path(__file__).resolve().parent.parent / "data" / "estudiantes.json"


def cargar_estudiantes():
    """Carga y devuelve la lista de estudiantes guardada en JSON."""
    if not ARCHIVO_ESTUDIANTES.exists():
        return []

    with ARCHIVO_ESTUDIANTES.open("r", encoding="utf-8") as archivo:
        return json.load(archivo)


def guardar_estudiantes(estudiantes):
    """Guarda la lista de estudiantes en el archivo JSON."""
    with ARCHIVO_ESTUDIANTES.open("w", encoding="utf-8") as archivo:
        json.dump(estudiantes, archivo, ensure_ascii=False, indent=2)


def generar_codigo_estudiante():
    """Genera el siguiente código consecutivo para un estudiante."""
    return f"EST-{len(cargar_estudiantes()) + 1:03d}"


def registrar_estudiante(nombres, apellidos, dni, correo, estado):
    """Registra un estudiante. La lógica detallada se completará después."""
    pass


def listar_estudiantes():
    """Devuelve todos los estudiantes registrados."""
    return cargar_estudiantes()


def buscar_estudiante(valor):
    """Busca por código, DNI, nombres o apellidos. Pendiente de completar."""
    pass


def actualizar_estudiante(codigo, nuevos_datos):
    """Actualiza los datos de un estudiante. Pendiente de completar."""
    pass


def validar_dni(dni):
    """Valida que el DNI tenga ocho dígitos."""
    return isinstance(dni, str) and dni.isdigit() and len(dni) == 8


def validar_correo(correo):
    """Valida de manera básica el formato de un correo electrónico."""
    return isinstance(correo, str) and "@" in correo and "." in correo.rsplit("@", 1)[-1]


def dni_repetido(dni):
    """Indica si un DNI ya está registrado."""
    return any(estudiante.get("dni") == dni for estudiante in cargar_estudiantes())


def estudiante_existe(codigo):
    """Indica si existe un estudiante con el código indicado."""
    return any(estudiante.get("codigo") == codigo for estudiante in cargar_estudiantes())
