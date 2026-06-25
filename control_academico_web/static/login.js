function obtenerDatosLogin() {
  return {
    usuario: document.getElementById("usuario").value.trim(),
    password: document.getElementById("password").value
  };
}

function validarLogin(datos) {
  if (!datos.usuario) {
    return "Ingrese su usuario.";
  }
  if (!datos.password) {
    return "Ingrese su contrasena.";
  }
  return "";
}

function mostrarMensajeLogin(mensaje, tipo) {
  const zona = document.getElementById("mensaje-login");
  zona.textContent = mensaje || "";
  zona.className = "mensaje-login " + (tipo || "");
}

async function iniciarSesion() {
  const datos = obtenerDatosLogin();
  const error = validarLogin(datos);

  if (error) {
    mostrarMensajeLogin(error, "error");
    return;
  }

  const respuesta = await fetch("/api/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(datos)
  });

  const resultado = await respuesta.json();
  mostrarMensajeLogin(resultado.mensaje, resultado.resultado ? "exito" : "error");

  if (resultado.resultado) {
    window.location.href = "/";
  }
}

document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("btn-login").addEventListener("click", iniciarSesion);
  document.getElementById("form-login").addEventListener("submit", (evento) => {
    evento.preventDefault();
    iniciarSesion();
  });
});
