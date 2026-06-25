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
    return []


def guardar_matriculas(matriculas):
    """Guarda la lista de matriculas en el archivo JSON."""
    pass


def validar_estudiante_para_matricula(codigo_estudiante):
    """Verifica que el estudiante exista y este activo."""
    return {"resultado": False, "mensaje": "Funcion pendiente de desarrollo."}


def validar_materia_para_matricula(codigo_materia):
    """Verifica que la materia exista y este activa."""
    return {"resultado": False, "mensaje": "Funcion pendiente de desarrollo."}


def validar_periodo_para_matricula(codigo_periodo):
    """Verifica que el periodo exista y este activo."""
    return {"resultado": False, "mensaje": "Funcion pendiente de desarrollo."}


def matricula_existe(codigo_estudiante, codigo_materia, codigo_periodo):
    """Verifica si ya existe una matricula con esos datos."""
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
