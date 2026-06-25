"""Funciones base para la gestión de estudiantes."""

import json
import os


CARPETA_BASE = os.path.dirname(os.path.dirname(__file__))
ARCHIVO_ESTUDIANTES = os.path.join(CARPETA_BASE, "data", "estudiantes.json")


def cargar_estudiantes():
    """Carga y devuelve la lista de estudiantes guardada en JSON."""
    try:
        with open(ARCHIVO_ESTUDIANTES, "r", encoding="utf-8") as archivo:
            contenido = archivo.read().strip()
    except FileNotFoundError:
        try:
            guardar_estudiantes([])
        except OSError:
            pass
        return []
    except OSError:
        return []

    if not contenido:
        return []

    try:
        estudiantes = json.loads(contenido)
        if isinstance(estudiantes, list):
            return estudiantes
    except (json.JSONDecodeError, OSError):
        pass

    return []


def guardar_estudiantes(estudiantes):
    """Guarda la lista de estudiantes en el archivo JSON."""
    os.makedirs(os.path.dirname(ARCHIVO_ESTUDIANTES), exist_ok=True)

    with open(ARCHIVO_ESTUDIANTES, "w", encoding="utf-8") as archivo:
        json.dump(estudiantes, archivo, ensure_ascii=False, indent=4)


def generar_codigo_estudiante():
    """Genera el siguiente código consecutivo para un estudiante."""
    estudiantes = cargar_estudiantes()
    codigos_usados = []

    for estudiante in estudiantes:
        codigo = estudiante.get("codigo", "")

        if codigo.startswith("EST") and codigo[3:].isdigit():
            codigos_usados.append(int(codigo[3:]))

    numero = 1

    while numero in codigos_usados:
        numero += 1

    return f"EST{numero:03d}"


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
    """Valida que el correo tenga @ y un punto después de ella."""
    if not isinstance(correo, str) or "@" not in correo:
        return False

    dominio = correo.split("@", 1)[1]
    return "." in dominio


def dni_repetido(dni):
    """Devuelve True cuando el DNI ya está registrado."""
    estudiantes = cargar_estudiantes()

    for estudiante in estudiantes:
        if estudiante.get("dni") == dni:
            return True

    return False


def estudiante_existe(codigo):
    """Devuelve True cuando existe un estudiante con el código indicado."""
    estudiantes = cargar_estudiantes()

    for estudiante in estudiantes:
        if estudiante.get("codigo") == codigo:
            return True

    return False
