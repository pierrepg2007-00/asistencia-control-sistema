"""Funciones base para la gestión de notas."""

import json
import os


CARPETA_BASE = os.path.dirname(os.path.dirname(__file__))
ARCHIVO_NOTAS = os.path.join(CARPETA_BASE, "data", "notas.json")
ARCHIVO_MATRICULAS = os.path.join(CARPETA_BASE, "data", "matriculas.json")
ARCHIVO_ESTUDIANTES = os.path.join(CARPETA_BASE, "data", "estudiantes.json")


def cargar_lista_json(ruta_archivo):
    """Carga una lista desde un archivo JSON, devolviendo [] ante errores."""
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.read().strip()
    except (FileNotFoundError, OSError):
        return []

    if not contenido:
        return []

    try:
        datos = json.loads(contenido)
        if isinstance(datos, list):
            return datos
    except json.JSONDecodeError:
        pass

    return []


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
    """Verifica que exista una matrícula activa antes de registrar nota."""
    codigo_estudiante = (codigo_estudiante or "").strip().upper()
    codigo_materia = (codigo_materia or "").strip().upper()
    codigo_periodo = (codigo_periodo or "").strip().upper()
    matriculas = cargar_lista_json(ARCHIVO_MATRICULAS)

    for matricula in matriculas:
        misma_matricula = (
            matricula.get("codigo_estudiante") == codigo_estudiante
            and matricula.get("codigo_materia") == codigo_materia
            and matricula.get("codigo_periodo") == codigo_periodo
        )

        if misma_matricula:
            estado = matricula.get("estado", "activo").strip().lower()

            if estado == "activo":
                return {
                    "resultado": True,
                    "mensaje": "Matrícula activa encontrada.",
                    "datos": matricula,
                }

            return {
                "resultado": False,
                "mensaje": "La matrícula existe, pero no está activa.",
                "datos": matricula,
            }

    return {
        "resultado": False,
        "mensaje": "El estudiante no está matriculado en esa materia y periodo.",
        "datos": None,
    }


def nota_existe(codigo_estudiante, codigo_materia, codigo_periodo):
    """Devuelve True si ya existe nota para estudiante, materia y periodo."""
    codigo_estudiante = (codigo_estudiante or "").strip().upper()
    codigo_materia = (codigo_materia or "").strip().upper()
    codigo_periodo = (codigo_periodo or "").strip().upper()

    for nota in cargar_notas():
        if (
            nota.get("codigo_estudiante") == codigo_estudiante
            and nota.get("codigo_materia") == codigo_materia
            and nota.get("codigo_periodo") == codigo_periodo
        ):
            return True

    return False


def registrar_nota(codigo_estudiante, codigo_materia, codigo_periodo, nota1, nota2, nota3):
    """Registra notas de un estudiante matriculado."""
    codigo_estudiante = (codigo_estudiante or "").strip().upper()
    codigo_materia = (codigo_materia or "").strip().upper()
    codigo_periodo = (codigo_periodo or "").strip().upper()

    if not codigo_estudiante:
        return {"resultado": False, "mensaje": "El código de estudiante no puede estar vacío.", "datos": None}

    if not codigo_materia:
        return {"resultado": False, "mensaje": "El código de materia no puede estar vacío.", "datos": None}

    if not codigo_periodo:
        return {"resultado": False, "mensaje": "El código de periodo no puede estar vacío.", "datos": None}

    resultado_matricula = verificar_matricula_para_nota(
        codigo_estudiante,
        codigo_materia,
        codigo_periodo,
    )

    if not resultado_matricula["resultado"]:
        return {"resultado": False, "mensaje": resultado_matricula["mensaje"], "datos": None}

    if not validar_nota(nota1) or not validar_nota(nota2) or not validar_nota(nota3):
        return {"resultado": False, "mensaje": "Las notas deben ser números entre 0 y 20.", "datos": None}

    if nota_existe(codigo_estudiante, codigo_materia, codigo_periodo):
        return {"resultado": False, "mensaje": "Ya existe una nota registrada para esa matrícula.", "datos": None}

    promedio = calcular_promedio(nota1, nota2, nota3)
    estado_final = determinar_estado_final(promedio)
    notas = cargar_notas()

    registro = {
        "codigo_estudiante": codigo_estudiante,
        "codigo_materia": codigo_materia,
        "codigo_periodo": codigo_periodo,
        "nota1": float(nota1),
        "nota2": float(nota2),
        "nota3": float(nota3),
        "promedio": promedio,
        "estado_final": estado_final,
    }

    notas.append(registro)
    guardar_notas(notas)

    return {
        "resultado": True,
        "mensaje": "Nota registrada correctamente.",
        "datos": registro,
    }


def listar_notas():
    """Devuelve todas las notas registradas."""
    return cargar_notas()


def listar_notas_por_estudiante(codigo_estudiante):
    """Devuelve todas las notas de un estudiante."""
    codigo_estudiante = (codigo_estudiante or "").strip().upper()
    notas_estudiante = []

    for nota in cargar_notas():
        if nota.get("codigo_estudiante") == codigo_estudiante:
            notas_estudiante.append(nota)

    return notas_estudiante


def listar_notas_por_materia(codigo_materia, codigo_periodo):
    """Devuelve notas de una materia en un periodo."""
    codigo_materia = (codigo_materia or "").strip().upper()
    codigo_periodo = (codigo_periodo or "").strip().upper()
    notas_materia = []

    for nota in cargar_notas():
        if (
            nota.get("codigo_materia") == codigo_materia
            and nota.get("codigo_periodo") == codigo_periodo
        ):
            notas_materia.append(nota)

    return notas_materia


def actualizar_nota(codigo_estudiante, codigo_materia, codigo_periodo, nuevas_notas):
    """Actualiza nota1, nota2 y nota3 de un registro existente."""
    codigo_estudiante = (codigo_estudiante or "").strip().upper()
    codigo_materia = (codigo_materia or "").strip().upper()
    codigo_periodo = (codigo_periodo or "").strip().upper()
    nuevas_notas = nuevas_notas or {}
    notas = cargar_notas()

    for nota in notas:
        if (
            nota.get("codigo_estudiante") == codigo_estudiante
            and nota.get("codigo_materia") == codigo_materia
            and nota.get("codigo_periodo") == codigo_periodo
        ):
            nota1 = nuevas_notas.get("nota1", nota.get("nota1"))
            nota2 = nuevas_notas.get("nota2", nota.get("nota2"))
            nota3 = nuevas_notas.get("nota3", nota.get("nota3"))

            if not validar_nota(nota1) or not validar_nota(nota2) or not validar_nota(nota3):
                return {
                    "resultado": False,
                    "mensaje": "Las notas deben ser números entre 0 y 20.",
                    "datos": None,
                }

            promedio = calcular_promedio(nota1, nota2, nota3)
            nota["nota1"] = float(nota1)
            nota["nota2"] = float(nota2)
            nota["nota3"] = float(nota3)
            nota["promedio"] = promedio
            nota["estado_final"] = determinar_estado_final(promedio)

            guardar_notas(notas)

            return {
                "resultado": True,
                "mensaje": "Nota actualizada correctamente.",
                "datos": nota,
            }

    return {
        "resultado": False,
        "mensaje": "No existe una nota para ese estudiante, materia y periodo.",
        "datos": None,
    }


def listar_estudiantes_sin_nota(codigo_materia, codigo_periodo):
    """Lista estudiantes matriculados que aún no tienen nota registrada."""
    codigo_materia = (codigo_materia or "").strip().upper()
    codigo_periodo = (codigo_periodo or "").strip().upper()
    matriculas = cargar_lista_json(ARCHIVO_MATRICULAS)
    estudiantes = cargar_lista_json(ARCHIVO_ESTUDIANTES)
    pendientes = []

    for matricula in matriculas:
        misma_materia_periodo = (
            matricula.get("codigo_materia") == codigo_materia
            and matricula.get("codigo_periodo") == codigo_periodo
        )
        estado = matricula.get("estado", "activo").strip().lower()

        if misma_materia_periodo and estado == "activo":
            codigo_estudiante = matricula.get("codigo_estudiante")

            if not nota_existe(codigo_estudiante, codigo_materia, codigo_periodo):
                pendiente = {
                    "codigo_estudiante": codigo_estudiante,
                    "codigo_materia": codigo_materia,
                    "codigo_periodo": codigo_periodo,
                }

                for estudiante in estudiantes:
                    if estudiante.get("codigo") == codigo_estudiante:
                        pendiente["nombres"] = estudiante.get("nombres", "")
                        pendiente["apellidos"] = estudiante.get("apellidos", "")
                        break

                pendientes.append(pendiente)

    return pendientes
