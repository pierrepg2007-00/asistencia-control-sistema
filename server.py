# Servidor web simple para el sistema de control academico.
# Ejecutar: python server.py
# Abrir en navegador: http://localhost:8000

import json
import mimetypes
import os
import uuid
from http import cookies
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

from control_academico_web.core import asistencia
from control_academico_web.core import auth
from control_academico_web.core import estudiantes
from control_academico_web.core import materias
from control_academico_web.core import matriculas
from control_academico_web.core import notas
from control_academico_web.core import periodos
from control_academico_web.core import reportes


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WEB_DIR = os.path.join(BASE_DIR, "control_academico_web", "web")
STATIC_DIR = os.path.join(BASE_DIR, "control_academico_web", "static")
PUERTO = 8000
SESIONES = {}
NOMBRE_COOKIE_SESION = "control_academico_session"

PAGINAS = {
    "/": "index.html",
    "/index": "index.html",
    "/estudiantes": "estudiantes.html",
    "/materias": "materias.html",
    "/matriculas": "matriculas.html",
    "/notas": "notas.html",
    "/asistencia": "asistencia.html",
    "/reportes": "reportes.html",
}

RUTAS_PUBLICAS_GET = ["/login"]
RUTAS_PUBLICAS_POST = ["/api/login", "/api/logout"]


def respuesta_ok(datos=None, mensaje="Operacion realizada correctamente."):
    return {"resultado": True, "mensaje": mensaje, "datos": datos}


class ManejadorControlAcademico(BaseHTTPRequestHandler):
    def do_GET(self):
        ruta = urlparse(self.path).path

        if ruta == "/login":
            if self.obtener_usuario_sesion():
                self.redirigir("/")
                return
            self.enviar_archivo(os.path.join(WEB_DIR, "login.html"))
            return

        if ruta == "/api/session":
            usuario_sesion = self.obtener_usuario_sesion()
            if usuario_sesion:
                self.enviar_json(respuesta_ok(usuario_sesion, "Sesion activa."))
            else:
                self.enviar_json({"resultado": False, "mensaje": "No hay sesion activa.", "datos": None}, 401)
            return

        if ruta in PAGINAS:
            if not self.obtener_usuario_sesion():
                self.redirigir("/login")
                return
            self.enviar_archivo(os.path.join(WEB_DIR, PAGINAS[ruta]))
            return

        if ruta.startswith("/static/"):
            nombre_archivo = ruta.replace("/static/", "", 1)
            self.enviar_archivo(os.path.join(STATIC_DIR, nombre_archivo))
            return

        self.enviar_json({"resultado": False, "mensaje": "Ruta no encontrada.", "datos": None}, 404)

    def do_POST(self):
        ruta = urlparse(self.path).path

        if not ruta.startswith("/api/"):
            self.enviar_json({"resultado": False, "mensaje": "Ruta API no encontrada.", "datos": None}, 404)
            return

        datos = self.leer_json()

        try:
            if ruta == "/api/login":
                respuesta = auth.autenticar_usuario(datos.get("usuario"), datos.get("password"))
                encabezados = {}

                if respuesta.get("resultado"):
                    session_id = str(uuid.uuid4())
                    SESIONES[session_id] = respuesta.get("datos")
                    encabezados["Set-Cookie"] = self.crear_cookie_sesion(session_id)

                self.enviar_json(respuesta, encabezados=encabezados)
                return

            if ruta == "/api/logout":
                session_id = self.obtener_session_id()
                if session_id in SESIONES:
                    del SESIONES[session_id]
                self.enviar_json(
                    respuesta_ok(None, "Sesion cerrada correctamente."),
                    encabezados={"Set-Cookie": self.crear_cookie_sesion("", expirar=True)},
                )
                return

            if ruta not in RUTAS_PUBLICAS_POST and not self.obtener_usuario_sesion():
                self.enviar_json({"resultado": False, "mensaje": "Sesion no iniciada.", "datos": None}, 401)
                return

            respuesta = self.procesar_api(ruta, datos)
            self.enviar_json(respuesta)
        except Exception as error:
            self.enviar_json(
                {"resultado": False, "mensaje": "Error interno: {}".format(error), "datos": None},
                500,
            )

    def leer_json(self):
        longitud = int(self.headers.get("Content-Length", 0))
        if longitud == 0:
            return {}

        contenido = self.rfile.read(longitud).decode("utf-8")
        try:
            datos = json.loads(contenido)
            if isinstance(datos, dict):
                return datos
        except json.JSONDecodeError:
            pass

        return {}

    def enviar_json(self, datos, estado=200, encabezados=None):
        contenido = json.dumps(datos, ensure_ascii=False).encode("utf-8")
        self.send_response(estado)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(contenido)))
        for nombre, valor in (encabezados or {}).items():
            self.send_header(nombre, valor)
        self.end_headers()
        self.wfile.write(contenido)

    def redirigir(self, ruta):
        self.send_response(302)
        self.send_header("Location", ruta)
        self.end_headers()

    def obtener_session_id(self):
        encabezado_cookie = self.headers.get("Cookie", "")
        if not encabezado_cookie:
            return ""

        cookie = cookies.SimpleCookie()
        try:
            cookie.load(encabezado_cookie)
        except cookies.CookieError:
            return ""

        if NOMBRE_COOKIE_SESION not in cookie:
            return ""

        return cookie[NOMBRE_COOKIE_SESION].value

    def obtener_usuario_sesion(self):
        session_id = self.obtener_session_id()
        if not session_id:
            return None
        return SESIONES.get(session_id)

    def crear_cookie_sesion(self, session_id, expirar=False):
        cookie = cookies.SimpleCookie()
        cookie[NOMBRE_COOKIE_SESION] = session_id
        cookie[NOMBRE_COOKIE_SESION]["path"] = "/"
        cookie[NOMBRE_COOKIE_SESION]["httponly"] = True
        cookie[NOMBRE_COOKIE_SESION]["samesite"] = "Lax"

        if expirar:
            cookie[NOMBRE_COOKIE_SESION]["max-age"] = 0

        return cookie.output(header="").strip()

    def enviar_archivo(self, ruta_archivo):
        if not os.path.isfile(ruta_archivo):
            self.enviar_json({"resultado": False, "mensaje": "Archivo no encontrado.", "datos": None}, 404)
            return

        tipo, _ = mimetypes.guess_type(ruta_archivo)
        if not tipo:
            tipo = "application/octet-stream"

        with open(ruta_archivo, "rb") as archivo:
            contenido = archivo.read()

        self.send_response(200)
        self.send_header("Content-Type", tipo)
        self.send_header("Content-Length", str(len(contenido)))
        self.end_headers()
        self.wfile.write(contenido)

    def procesar_api(self, ruta, datos):
        if ruta == "/api/estudiantes/guardar":
            return estudiantes.registrar_estudiante(
                datos.get("nombres"),
                datos.get("apellidos"),
                datos.get("dni"),
                datos.get("correo"),
                datos.get("estado"),
            )
        if ruta == "/api/estudiantes/listar":
            return respuesta_ok(estudiantes.listar_estudiantes(), "Estudiantes listados correctamente.")
        if ruta == "/api/estudiantes/buscar":
            return estudiantes.buscar_estudiante(datos.get("valor"))
        if ruta == "/api/estudiantes/actualizar":
            return estudiantes.actualizar_estudiante(datos.get("codigo"), datos)

        if ruta == "/api/materias/guardar":
            return materias.registrar_materia(
                datos.get("nombre_materia"),
                datos.get("docente"),
                datos.get("ciclo"),
                datos.get("estado"),
            )
        if ruta == "/api/materias/listar":
            return respuesta_ok(materias.listar_materias(), "Materias listadas correctamente.")
        if ruta == "/api/materias/buscar":
            return materias.buscar_materia(datos.get("codigo_materia"))
        if ruta == "/api/materias/actualizar":
            return materias.actualizar_materia(datos.get("codigo_materia"), datos)

        if ruta == "/api/periodos/guardar":
            return periodos.registrar_periodo(
                datos.get("codigo_periodo"),
                datos.get("anio"),
                datos.get("nombre"),
                datos.get("estado"),
            )
        if ruta == "/api/periodos/listar":
            return respuesta_ok(periodos.listar_periodos(), "Periodos listados correctamente.")
        if ruta == "/api/periodos/buscar":
            return periodos.buscar_periodo(datos.get("codigo_periodo"))
        if ruta == "/api/periodos/activar":
            return periodos.cambiar_periodo_activo(datos.get("codigo_periodo"))

        if ruta == "/api/matriculas/guardar":
            return matriculas.registrar_matricula(
                datos.get("codigo_estudiante"),
                datos.get("codigo_materia"),
                datos.get("codigo_periodo"),
            )
        if ruta == "/api/matriculas/listar":
            return respuesta_ok(matriculas.listar_matriculas(), "Matriculas listadas correctamente.")
        if ruta == "/api/matriculas/buscar":
            return matriculas.buscar_matricula(
                datos.get("codigo_estudiante"),
                datos.get("codigo_materia"),
                datos.get("codigo_periodo"),
            )
        if ruta == "/api/matriculas/por-estudiante":
            return respuesta_ok(
                matriculas.listar_matriculas_por_estudiante(datos.get("codigo_estudiante")),
                "Matriculas por estudiante listadas correctamente.",
            )
        if ruta == "/api/matriculas/por-materia":
            return respuesta_ok(
                matriculas.listar_matriculas_por_materia(datos.get("codigo_materia"), datos.get("codigo_periodo")),
                "Matriculas por materia listadas correctamente.",
            )
        if ruta == "/api/matriculas/cambiar-estado":
            return matriculas.cambiar_estado_matricula(
                datos.get("codigo_estudiante"),
                datos.get("codigo_materia"),
                datos.get("codigo_periodo"),
                datos.get("estado"),
            )

        if ruta == "/api/notas/guardar":
            return notas.registrar_nota(
                datos.get("codigo_estudiante"),
                datos.get("codigo_materia"),
                datos.get("codigo_periodo"),
                datos.get("nota1"),
                datos.get("nota2"),
                datos.get("nota3"),
            )
        if ruta == "/api/notas/listar":
            return respuesta_ok(notas.listar_notas(), "Notas listadas correctamente.")
        if ruta == "/api/notas/por-estudiante":
            return respuesta_ok(
                notas.listar_notas_por_estudiante(datos.get("codigo_estudiante")),
                "Notas por estudiante listadas correctamente.",
            )
        if ruta == "/api/notas/por-materia":
            return respuesta_ok(
                notas.listar_notas_por_materia(datos.get("codigo_materia"), datos.get("codigo_periodo")),
                "Notas por materia listadas correctamente.",
            )
        if ruta == "/api/notas/actualizar":
            return notas.actualizar_nota(
                datos.get("codigo_estudiante"),
                datos.get("codigo_materia"),
                datos.get("codigo_periodo"),
                datos,
            )

        if ruta == "/api/asistencia/guardar":
            return asistencia.registrar_asistencia(
                datos.get("codigo_estudiante"),
                datos.get("codigo_materia"),
                datos.get("codigo_periodo"),
                datos.get("fecha"),
                datos.get("estado_asistencia"),
            )
        if ruta == "/api/asistencia/listar":
            return respuesta_ok(asistencia.listar_asistencias(), "Asistencias listadas correctamente.")
        if ruta == "/api/asistencia/por-estudiante":
            return respuesta_ok(
                asistencia.listar_asistencia_por_estudiante(datos.get("codigo_estudiante")),
                "Asistencia por estudiante listada correctamente.",
            )
        if ruta == "/api/asistencia/por-materia":
            return respuesta_ok(
                asistencia.listar_asistencia_por_materia(
                    datos.get("codigo_materia"),
                    datos.get("codigo_periodo"),
                    datos.get("fecha"),
                ),
                "Asistencia por materia listada correctamente.",
            )
        if ruta == "/api/asistencia/porcentaje":
            return respuesta_ok(
                asistencia.calcular_porcentaje_asistencia(
                    datos.get("codigo_estudiante"),
                    datos.get("codigo_materia"),
                    datos.get("codigo_periodo"),
                ),
                "Porcentaje calculado correctamente.",
            )

        if ruta == "/api/reportes/estudiantes-materia":
            return respuesta_ok(
                reportes.reporte_estudiantes_por_materia(datos.get("codigo_materia"), datos.get("codigo_periodo")),
                "Reporte generado correctamente.",
            )
        if ruta == "/api/reportes/notas-materia":
            return respuesta_ok(
                reportes.reporte_notas_por_materia(datos.get("codigo_materia"), datos.get("codigo_periodo")),
                "Reporte generado correctamente.",
            )
        if ruta == "/api/reportes/asistencia-materia":
            return respuesta_ok(
                reportes.reporte_asistencia_por_materia(datos.get("codigo_materia"), datos.get("codigo_periodo")),
                "Reporte generado correctamente.",
            )
        if ruta == "/api/reportes/riesgo":
            return respuesta_ok(reportes.reporte_estudiantes_en_riesgo(), "Reporte generado correctamente.")
        if ruta == "/api/reportes/exportar":
            return reportes.exportar_reporte_txt(datos.get("nombre_reporte"), datos.get("datos"))

        return {"resultado": False, "mensaje": "Accion API no encontrada.", "datos": None}


if __name__ == "__main__":
    direccion = ("", PUERTO)
    httpd = HTTPServer(direccion, ManejadorControlAcademico)

    print("=" * 50)
    print("  Servidor iniciado en http://localhost:{}".format(PUERTO))
    print("  Presiona Ctrl+C para detener el servidor")
    print("=" * 50)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor detenido.")
        httpd.server_close()
