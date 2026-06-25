"""Funciones base para la gestión de notas."""

import json
import os


CARPETA_BASE = os.path.dirname(os.path.dirname(__file__))
ARCHIVO_NOTAS = os.path.join(CARPETA_BASE, "data", "notas.json")
ARCHIVO_MATRICULAS = os.path.join(CARPETA_BASE, "data", "matriculas.json")
ARCHIVO_ESTUDIANTES = os.path.join(CARPETA_BASE, "data", "estudiantes.json")


def cargar_notas():
    """Carga y devuelve la lista de notas guardada en JSON."""
    try:
        with open(ARCHIVO_NOTAS, "r", encoding="utf-8") as archivo:
            contenido = archivo.read().strip()
    except FileNotFoundError:
        try:
            guardar_notas([])
        except OSError:
            pass
        return []
    except OSError:
        return []

    if not contenido:
        return []

    try:
        notas = json.loads(contenido)
        if isinstance(notas, list):
            return notas
    except json.JSONDecodeError:
        pass

    return []


def guardar_notas(notas):
    """Guarda la lista de notas en el archivo JSON."""
    os.makedirs(os.path.dirname(ARCHIVO_NOTAS), exist_ok=True)

    with open(ARCHIVO_NOTAS, "w", encoding="utf-8") as archivo:
        json.dump(notas, archivo, ensure_ascii=False, indent=4)


def validar_nota(nota):
    """Valida que una nota sea numérica y esté entre 0 y 20."""
    if nota is None or nota == "":
        return False

    try:
        nota_numero = float(nota)
    except (ValueError, TypeError):
        return False

    return 0 <= nota_numero <= 20


def calcular_promedio(nota1, nota2, nota3):
    """Calcula el promedio de tres notas válidas."""
    if not validar_nota(nota1) or not validar_nota(nota2) or not validar_nota(nota3):
        return None

    promedio = (float(nota1) + float(nota2) + float(nota3)) / 3
    return round(promedio, 2)


def determinar_estado_final(promedio):
    """Devuelve aprobado si el promedio es mayor o igual a 11."""
    if promedio is None:
        return "desaprobado"

    if float(promedio) >= 11:
        return "aprobado"

    return "desaprobado"


def verificar_matricula_para_nota(codigo_estudiante, codigo_materia, codigo_periodo):
    """Verifica si existe matrícula para registrar nota. Pendiente de completar."""
    pass


def nota_existe(codigo_estudiante, codigo_materia, codigo_periodo):
    """Verifica si ya existe una nota registrada. Pendiente de completar."""
    pass


def registrar_nota(codigo_estudiante, codigo_materia, codigo_periodo, nota1, nota2, nota3):
    """Registra una nota. Pendiente de completar."""
    pass


def listar_notas():
    """Lista todas las notas registradas. Pendiente de completar."""
    return cargar_notas()


def listar_notas_por_estudiante(codigo_estudiante):
    """Lista notas por estudiante. Pendiente de completar."""
    pass


def listar_notas_por_materia(codigo_materia, codigo_periodo):
    """Lista notas por materia y periodo. Pendiente de completar."""
    pass


def actualizar_nota(codigo_estudiante, codigo_materia, codigo_periodo, nuevas_notas):
    """Actualiza las notas de un registro. Pendiente de completar."""
    pass


def listar_estudiantes_sin_nota(codigo_materia, codigo_periodo):
    """Lista matriculados que aún no tienen nota. Pendiente de completar."""
    pass
