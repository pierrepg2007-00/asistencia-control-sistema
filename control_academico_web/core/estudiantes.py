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
    """Registra un estudiante nuevo con validaciones básicas."""
    nombres = (nombres or "").strip()
    apellidos = (apellidos or "").strip()
    dni = (dni or "").strip()
    correo = (correo or "").strip()
    estado = (estado or "").strip().lower()

    if not nombres:
        return {
            "resultado": False,
            "mensaje": "Los nombres no pueden estar vacíos.",
            "datos": None,
        }

    if not apellidos:
        return {
            "resultado": False,
            "mensaje": "Los apellidos no pueden estar vacíos.",
            "datos": None,
        }

    if not validar_dni(dni):
        return {
            "resultado": False,
            "mensaje": "El DNI debe tener exactamente 8 dígitos.",
            "datos": None,
        }

    if dni_repetido(dni):
        return {
            "resultado": False,
            "mensaje": "El DNI ya está registrado.",
            "datos": None,
        }

    if not validar_correo(correo):
        return {
            "resultado": False,
            "mensaje": "El correo no tiene un formato válido.",
            "datos": None,
        }

    if estado not in ["activo", "inactivo"]:
        return {
            "resultado": False,
            "mensaje": "El estado debe ser activo o inactivo.",
            "datos": None,
        }

    estudiantes = cargar_estudiantes()

    estudiante = {
        "codigo": generar_codigo_estudiante(),
        "nombres": nombres,
        "apellidos": apellidos,
        "dni": dni,
        "correo": correo,
        "estado": estado,
    }

    estudiantes.append(estudiante)
    guardar_estudiantes(estudiantes)

    return {
        "resultado": True,
        "mensaje": "Estudiante registrado correctamente.",
        "datos": estudiante,
    }


def listar_estudiantes():
    """Devuelve todos los estudiantes registrados."""
    return cargar_estudiantes()


def buscar_estudiante(valor):
    """Busca un estudiante por código o DNI."""
    valor = (valor or "").strip()
    estudiantes = cargar_estudiantes()

    if not valor:
        return {
            "resultado": False,
            "mensaje": "Debe ingresar un código o DNI para buscar.",
            "datos": None,
        }

    for estudiante in estudiantes:
        if valor.upper().startswith("EST"):
            if estudiante.get("codigo") == valor.upper():
                return {
                    "resultado": True,
                    "mensaje": "Estudiante encontrado.",
                    "datos": estudiante,
                }
        elif validar_dni(valor):
            if estudiante.get("dni") == valor:
                return {
                    "resultado": True,
                    "mensaje": "Estudiante encontrado.",
                    "datos": estudiante,
                }

    return {
        "resultado": False,
        "mensaje": "No se encontró ningún estudiante con ese código o DNI.",
        "datos": None,
    }


def actualizar_estudiante(codigo, nuevos_datos):
    """Actualiza datos permitidos de un estudiante."""
    codigo = (codigo or "").strip().upper()
    nuevos_datos = nuevos_datos or {}
    estudiantes = cargar_estudiantes()

    for estudiante in estudiantes:
        if estudiante.get("codigo") == codigo:
            nombres = nuevos_datos.get("nombres", estudiante.get("nombres", ""))
            apellidos = nuevos_datos.get("apellidos", estudiante.get("apellidos", ""))
            correo = nuevos_datos.get("correo", estudiante.get("correo", ""))
            estado = nuevos_datos.get("estado", estudiante.get("estado", ""))

            nombres = (nombres or "").strip()
            apellidos = (apellidos or "").strip()
            correo = (correo or "").strip()
            estado = (estado or "").strip().lower()

            if not nombres:
                return {
                    "resultado": False,
                    "mensaje": "Los nombres no pueden quedar vacíos.",
                    "datos": None,
                }

            if not apellidos:
                return {
                    "resultado": False,
                    "mensaje": "Los apellidos no pueden quedar vacíos.",
                    "datos": None,
                }

            if not validar_correo(correo):
                return {
                    "resultado": False,
                    "mensaje": "El correo no tiene un formato válido.",
                    "datos": None,
                }

            if estado not in ["activo", "inactivo"]:
                return {
                    "resultado": False,
                    "mensaje": "El estado debe ser activo o inactivo.",
                    "datos": None,
                }

            estudiante["nombres"] = nombres
            estudiante["apellidos"] = apellidos
            estudiante["correo"] = correo
            estudiante["estado"] = estado

            guardar_estudiantes(estudiantes)

            return {
                "resultado": True,
                "mensaje": "Estudiante actualizado correctamente.",
                "datos": estudiante,
            }

    return {
        "resultado": False,
        "mensaje": "No existe un estudiante con ese código.",
        "datos": None,
    }


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
