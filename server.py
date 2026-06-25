# Servidor web simple para el sistema de control academico.
# Ejecutar: python server.py
# Abrir en navegador: http://localhost:8000

import http.server
import os
import webbrowser

# Cambiar al directorio del proyecto para servir archivos correctamente
DIRECTORIO_PROYECTO = os.path.join(os.path.dirname(__file__), "control_academico_web")
os.chdir(DIRECTORIO_PROYECTO)

PUERTO = 8000

# Crear el servidor HTTP
servidor = http.server.HTTPServer

# Usar SimpleHTTPRequestHandler para servir archivos estaticos
manejador = http.server.SimpleHTTPRequestHandler

# Iniciar el servidor
direccion = ("", PUERTO)
httpd = servidor(direccion, manejador)

print("=" * 50)
print("  Servidor iniciado en http://localhost:{}".format(PUERTO))
print("  Presiona Ctrl+C para detener el servidor")
print("=" * 50)

# Intentar abrir el navegador automaticamente
try:
    webbrowser.open("http://localhost:{}/web/index.html".format(PUERTO))
except Exception:
    pass

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nServidor detenido.")
    httpd.server_close()
