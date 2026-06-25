async function llamarApiUsuarios(ruta, datos) {
  const respuesta = await fetch(ruta, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(datos || {})
  });
  return await respuesta.json();
}

function obtenerDatosUsuario() {
  return {
    usuario: document.getElementById("usuario").value.trim(),
    nombre: document.getElementById("nombre").value.trim(),
    password: document.getElementById("password").value,
    rol: document.getElementById("rol").value,
    estado: document.getElementById("estado").value
  };
}

function validarUsuario(datos) {
  if (!datos.usuario) {
    return "Ingrese el usuario.";
  }
  if (!datos.nombre) {
    return "Ingrese el nombre.";
  }
  if (!datos.password || datos.password.length < 4) {
    return "Ingrese una contrasena de al menos 4 caracteres.";
  }
  return "";
}

function mostrarMensajeUsuarios(mensaje, tipo) {
  const zona = document.getElementById("mensaje-usuarios");
  zona.textContent = mensaje || "";
  zona.className = "mensaje " + (tipo || "");
}

function limpiarFormularioUsuario() {
  document.getElementById("formulario-usuario").reset();
}

function renderizarUsuarios(usuarios) {
  const cuerpo = document.getElementById("tabla-usuarios");
  cuerpo.innerHTML = "";

  if (!usuarios || usuarios.length === 0) {
    cuerpo.innerHTML = '<tr><td colspan="4">No hay usuarios para mostrar.</td></tr>';
    return;
  }

  usuarios.forEach((usuario) => {
    const fila = document.createElement("tr");
    fila.innerHTML = `
      <td>${usuario.usuario || ""}</td>
      <td>${usuario.nombre || ""}</td>
      <td>${usuario.rol || ""}</td>
      <td>${usuario.estado || ""}</td>
    `;
    cuerpo.appendChild(fila);
  });
}

async function listarUsuarios() {
  const respuesta = await llamarApiUsuarios("/api/usuarios/listar");
  renderizarUsuarios(respuesta.datos || []);
  if (!respuesta.resultado) {
    mostrarMensajeUsuarios(respuesta.mensaje, "error");
  }
}

async function crearUsuario() {
  const datos = obtenerDatosUsuario();
  const error = validarUsuario(datos);

  if (error) {
    mostrarMensajeUsuarios(error, "error");
    return;
  }

  const respuesta = await llamarApiUsuarios("/api/usuarios/crear", datos);
  mostrarMensajeUsuarios(respuesta.mensaje, respuesta.resultado ? "exito" : "error");

  if (respuesta.resultado) {
    limpiarFormularioUsuario();
    listarUsuarios();
  }
}

document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("btn-crear-usuario").addEventListener("click", crearUsuario);
  document.getElementById("btn-limpiar-usuario").addEventListener("click", limpiarFormularioUsuario);
  listarUsuarios();
});
