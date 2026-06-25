"""Funciones simples de autenticacion para el sistema academico."""

import hashlib
import hmac
import json
import os
import secrets


CARPETA_BASE = os.path.dirname(os.path.dirname(__file__))
ARCHIVO_USUARIOS = os.path.join(CARPETA_BASE, "data", "usuarios.json")
ITERACIONES_HASH = 100000


def generar_salt():
    """Genera un salt aleatorio usando librerias estandar."""
    return secrets.token_hex(16)


def generar_hash_password(password, salt):
    """Genera hash PBKDF2-HMAC-SHA256 para una contrasena y salt."""
    password = (password or "").encode("utf-8")
    salt = (salt or "").encode("utf-8")
    return hashlib.pbkdf2_hmac("sha256", password, salt, ITERACIONES_HASH).hex()


def crear_admin_por_defecto():
    """Devuelve el usuario administrador inicial con password hasheado."""
    salt = generar_salt()
    return {
        "usuario": "admin",
        "nombre": "Administrador",
        "password_hash": generar_hash_password("admin123", salt),
        "salt": salt,
        "rol": "administrador",
        "estado": "activo",
    }


def cargar_usuarios():
    """Carga usuarios desde JSON; si no hay datos crea admin por defecto."""
    try:
        with open(ARCHIVO_USUARIOS, "r", encoding="utf-8") as archivo:
            contenido = archivo.read().strip()
    except FileNotFoundError:
        usuarios = [crear_admin_por_defecto()]
        guardar_usuarios(usuarios)
        return usuarios
    except OSError:
        return []

    if not contenido:
        usuarios = [crear_admin_por_defecto()]
        guardar_usuarios(usuarios)
        return usuarios

    try:
        usuarios = json.loads(contenido)
        if isinstance(usuarios, list) and usuarios:
            return usuarios
    except json.JSONDecodeError:
        pass

    usuarios = [crear_admin_por_defecto()]
    guardar_usuarios(usuarios)
    return usuarios


def guardar_usuarios(usuarios):
    """Guarda la lista de usuarios en data/usuarios.json."""
    os.makedirs(os.path.dirname(ARCHIVO_USUARIOS), exist_ok=True)
    with open(ARCHIVO_USUARIOS, "w", encoding="utf-8") as archivo:
        json.dump(usuarios, archivo, ensure_ascii=False, indent=4)


def verificar_password(password, salt, password_hash):
    """Compara una contrasena ingresada contra el hash guardado."""
    hash_ingresado = generar_hash_password(password, salt)
    return hmac.compare_digest(hash_ingresado, password_hash or "")


def buscar_usuario(usuario):
    """Busca un usuario por nombre de usuario."""
    usuario = (usuario or "").strip().lower()
    for item in cargar_usuarios():
        if item.get("usuario", "").strip().lower() == usuario:
            return item
    return None


def datos_publicos_usuario(usuario):
    """Devuelve datos seguros para responder al navegador."""
    if not usuario:
        return None
    return {
        "usuario": usuario.get("usuario"),
        "nombre": usuario.get("nombre"),
        "rol": usuario.get("rol"),
        "estado": usuario.get("estado"),
    }


def listar_usuarios_publicos():
    """Lista usuarios sin exponer hash ni salt."""
    usuarios_publicos = []
    for usuario in cargar_usuarios():
        usuarios_publicos.append(datos_publicos_usuario(usuario))
    return usuarios_publicos


def autenticar_usuario(usuario, password):
    """Valida usuario, estado y contrasena sin exponer hash ni salt."""
    usuario_encontrado = buscar_usuario(usuario)

    if not usuario_encontrado:
        return {"resultado": False, "mensaje": "Usuario o contrasena incorrectos.", "datos": None}

    if usuario_encontrado.get("estado") != "activo":
        return {"resultado": False, "mensaje": "El usuario no esta activo.", "datos": None}

    password_ok = verificar_password(
        password,
        usuario_encontrado.get("salt"),
        usuario_encontrado.get("password_hash"),
    )

    if not password_ok:
        return {"resultado": False, "mensaje": "Usuario o contrasena incorrectos.", "datos": None}

    return {
        "resultado": True,
        "mensaje": "Inicio de sesion correcto.",
        "datos": datos_publicos_usuario(usuario_encontrado),
    }


def crear_usuario(usuario, nombre, password, rol="usuario", estado="activo"):
    """Crea un usuario nuevo guardando solo hash y salt."""
    usuario = (usuario or "").strip().lower()
    nombre = (nombre or "").strip()
    rol = (rol or "usuario").strip().lower()
    estado = (estado or "activo").strip().lower()

    if not usuario:
        return {"resultado": False, "mensaje": "El usuario no puede estar vacio.", "datos": None}
    if not nombre:
        return {"resultado": False, "mensaje": "El nombre no puede estar vacio.", "datos": None}
    if not password:
        return {"resultado": False, "mensaje": "La contrasena no puede estar vacia.", "datos": None}
    if rol not in ["administrador", "usuario"]:
        return {"resultado": False, "mensaje": "El rol debe ser administrador o usuario.", "datos": None}
    if estado not in ["activo", "inactivo"]:
        return {"resultado": False, "mensaje": "El estado debe ser activo o inactivo.", "datos": None}
    if buscar_usuario(usuario):
        return {"resultado": False, "mensaje": "El usuario ya existe.", "datos": None}

    salt = generar_salt()
    nuevo_usuario = {
        "usuario": usuario,
        "nombre": nombre,
        "password_hash": generar_hash_password(password, salt),
        "salt": salt,
        "rol": rol,
        "estado": estado,
    }

    usuarios = cargar_usuarios()
    usuarios.append(nuevo_usuario)
    guardar_usuarios(usuarios)

    return {
        "resultado": True,
        "mensaje": "Usuario creado correctamente.",
        "datos": datos_publicos_usuario(nuevo_usuario),
    }
