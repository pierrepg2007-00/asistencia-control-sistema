"""Funciones base para la gestion de matriculas."""

import json
import os


CARPETA_BASE = os.path.dirname(os.path.dirname(__file__))
ARCHIVO_MATRICULAS = os.path.join(CARPETA_BASE, "data", "matriculas.json")
ARCHIVO_ESTUDIANTES = os.path.join(CARPETA_BASE, "data", "estudiantes.json")
ARCHIVO_MATERIAS = os.path.join(CARPETA_BASE, "data", "materias.json")
ARCHIVO_PERIODOS = os.path.join(CARPETA_BASE, "data", "periodos.json")


def cargar_matriculas():
    """Carga y devuelve la lista de matriculas guardada en JSON."""
    try:
        with open(ARCHIVO_MATRICULAS, "r", encoding="utf-8") as archivo:
            contenido = archivo.read().strip()
    except FileNotFoundError:
        try:
            guardar_matriculas([])
        except OSError:
            pass
        return []
    except OSError:
        return []

    if not contenido:
        return []

    try:
        matriculas = json.loads(contenido)
        if isinstance(matriculas, list):
            return matriculas
    except (json.JSONDecodeError, OSError):
        pass

    return []


def guardar_matriculas(matriculas):
    """Guarda la lista de matriculas en el archivo JSON."""
    os.makedirs(os.path.dirname(ARCHIVO_MATRICULAS), exist_ok=True)

    with open(ARCHIVO_MATRICULAS, "w", encoding="utf-8") as archivo:
        json.dump(matriculas, archivo, ensure_ascii=False, indent=4)


def validar_estudiante_para_matricula(codigo_estudiante):
    """Verifica que el estudiante exista y este activo."""
    codigo_estudiante = (codigo_estudiante or "").strip().upper()

    if not codigo_estudiante:
        return {"resultado": False, "mensaje": "El codigo del estudiante no puede estar vacio."}

    try:
        with open(ARCHIVO_ESTUDIANTES, "r", encoding="utf-8") as archivo:
            contenido = archivo.read().strip()
    except (FileNotFoundError, OSError):
        return {"resultado": False, "mensaje": "No se pudo leer el archivo de estudiantes."}

    if not contenido:
        return {"resultado": False, "mensaje": "No hay estudiantes registrados."}

    try:
        estudiantes = json.loads(contenido)
    except (json.JSONDecodeError, OSError):
        return {"resultado": False, "mensaje": "Error al leer los datos de estudiantes."}

    for estudiante in estudiantes:
        if estudiante.get("codigo") == codigo_estudiante:
            if estudiante.get("estado") == "activo":
                return {"resultado": True, "mensaje": "Estudiante apto para matricula."}
            else:
                return {"resultado": False, "mensaje": "El estudiante no esta activo."}

    return {"resultado": False, "mensaje": "El estudiante no existe."}


def validar_materia_para_matricula(codigo_materia):
    """Verifica que la materia exista y este activa."""
    codigo_materia = (codigo_materia or "").strip().upper()

    if not codigo_materia:
        return {"resultado": False, "mensaje": "El codigo de la materia no puede estar vacio."}

    try:
        with open(ARCHIVO_MATERIAS, "r", encoding="utf-8") as archivo:
            contenido = archivo.read().strip()
    except (FileNotFoundError, OSError):
        return {"resultado": False, "mensaje": "No se pudo leer el archivo de materias."}

    if not contenido:
        return {"resultado": False, "mensaje": "No hay materias registradas."}

    try:
        materias = json.loads(contenido)
    except (json.JSONDecodeError, OSError):
        return {"resultado": False, "mensaje": "Error al leer los datos de materias."}

    for materia in materias:
        if materia.get("codigo_materia") == codigo_materia:
            if materia.get("estado") == "activo":
                return {"resultado": True, "mensaje": "Materia apta para matricula."}
            else:
                return {"resultado": False, "mensaje": "La materia no esta activa."}

    return {"resultado": False, "mensaje": "La materia no existe."}


def validar_periodo_para_matricula(codigo_periodo):
    """Verifica que el periodo exista y este activo."""
    codigo_periodo = (codigo_periodo or "").strip().upper()

    if not codigo_periodo:
        return {"resultado": False, "mensaje": "El codigo del periodo no puede estar vacio."}

    try:
        with open(ARCHIVO_PERIODOS, "r", encoding="utf-8") as archivo:
            contenido = archivo.read().strip()
    except (FileNotFoundError, OSError):
        return {"resultado": False, "mensaje": "No se pudo leer el archivo de periodos."}

    if not contenido:
        return {"resultado": False, "mensaje": "No hay periodos registrados."}

    try:
        periodos = json.loads(contenido)
    except (json.JSONDecodeError, OSError):
        return {"resultado": False, "mensaje": "Error al leer los datos de periodos."}

    for periodo in periodos:
        if periodo.get("codigo_periodo") == codigo_periodo:
            if periodo.get("estado") == "activo":
                return {"resultado": True, "mensaje": "Periodo apto para matricula."}
            else:
                return {"resultado": False, "mensaje": "El periodo no esta activo."}

    return {"resultado": False, "mensaje": "El periodo no existe."}


def matricula_existe(codigo_estudiante, codigo_materia, codigo_periodo):
    """Verifica si ya existe una matricula con esos datos."""
    matriculas = cargar_matriculas()

    for matricula in matriculas:
        if (matricula.get("codigo_estudiante") == codigo_estudiante
                and matricula.get("codigo_materia") == codigo_materia
                and matricula.get("codigo_periodo") == codigo_periodo):
            return True

    return False


def registrar_matricula(codigo_estudiante, codigo_materia, codigo_periodo):
    """Registra una nueva matricula con validaciones."""
    return {"resultado": False, "mensaje": "Funcion pendiente de desarrollo."}


def listar_matriculas():
    """Devuelve todas las matriculas registradas."""
    return []


def buscar_matricula(codigo_estudiante, codigo_materia, codigo_periodo):
    """Busca una matricula exacta por estudiante, materia y periodo."""
    return {"resultado": False, "mensaje": "Funcion pendiente de desarrollo."}


def listar_matriculas_por_estudiante(codigo_estudiante):
    """Devuelve todas las matriculas de un estudiante."""
    return []


def listar_matriculas_por_materia(codigo_materia, codigo_periodo):
    """Devuelve todos los estudiantes matriculados en una materia y periodo."""
    return []


def cambiar_estado_matricula(codigo_estudiante, codigo_materia, codigo_periodo, nuevo_estado):
    """Cambia el estado de una matricula existente."""
    return {"resultado": False, "mensaje": "Funcion pendiente de desarrollo."}
