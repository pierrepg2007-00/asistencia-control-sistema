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
    """Genera el siguiente código consecutivo para una materia."""
    materias = cargar_materias()
    codigos_usados = []

    for materia in materias:
        codigo = materia.get("codigo_materia", "")

        if codigo.startswith("MAT") and codigo[3:].isdigit():
            codigos_usados.append(int(codigo[3:]))

    numero = 1

    while numero in codigos_usados:
        numero += 1

    return f"MAT{numero:03d}"


def registrar_materia(nombre_materia, docente, ciclo, estado):
    """Registra una materia nueva con validaciones básicas."""
    nombre_materia = (nombre_materia or "").strip()
    docente = (docente or "").strip()
    estado = (estado or "").strip().lower()

    if not nombre_materia:
        return {
            "resultado": False,
            "mensaje": "El nombre de la materia no puede estar vacío.",
            "datos": None,
        }

    if not docente:
        return {
            "resultado": False,
            "mensaje": "El docente no puede estar vacío.",
            "datos": None,
        }

    if not validar_ciclo(ciclo):
        return {
            "resultado": False,
            "mensaje": "El ciclo debe ser un número entero mayor que cero.",
            "datos": None,
        }

    if not validar_estado_materia(estado):
        return {
            "resultado": False,
            "mensaje": "El estado debe ser activo o inactivo.",
            "datos": None,
        }

    materias = cargar_materias()

    materia = {
        "codigo_materia": generar_codigo_materia(),
        "nombre_materia": nombre_materia,
        "docente": docente,
        "ciclo": int(ciclo),
        "estado": estado,
    }

    materias.append(materia)
    guardar_materias(materias)

    return {
        "resultado": True,
        "mensaje": "Materia registrada correctamente.",
        "datos": materia,
    }


def listar_materias():
    """Devuelve todas las materias registradas."""
    return cargar_materias()


def buscar_materia(codigo_materia):
    """Busca una materia por código. Pendiente de completar."""
    pass


def actualizar_materia(codigo_materia, nuevos_datos):
    """Actualiza una materia. Pendiente de completar."""
    pass


def validar_ciclo(ciclo):
    """Valida que el ciclo sea un entero mayor que cero."""
    if ciclo is None or ciclo == "":
        return False

    try:
        ciclo_entero = int(ciclo)
    except ValueError:
        return False

    return ciclo_entero > 0


def validar_estado_materia(estado):
    """Valida que el estado de la materia sea activo o inactivo."""
    estado = (estado or "").strip().lower()
    return estado in ["activo", "inactivo"]


def materia_existe(codigo_materia):
    """Devuelve True cuando existe una materia con el código indicado."""
    codigo_materia = (codigo_materia or "").strip().upper()

    for materia in cargar_materias():
        if materia.get("codigo_materia") == codigo_materia:
            return True

    return False
