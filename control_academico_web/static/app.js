async function verificarSesion() {
  try {
    const respuesta = await fetch("/api/session");
    const datos = await respuesta.json();

    if (!datos.resultado) {
      window.location.href = "/login";
      return;
    }

    const usuario = datos.datos || {};
    const nombreUsuario = document.getElementById("usuario-sesion");
    if (nombreUsuario) {
      nombreUsuario.textContent = usuario.nombre || usuario.usuario || "";
    }

    if (document.body.dataset.requiereAdmin === "true" && usuario.rol !== "administrador") {
      window.location.href = "/";
      return;
    }

    if (usuario.rol === "administrador") {
      document.querySelectorAll(".solo-admin").forEach((elemento) => {
        elemento.classList.add("visible-admin");
      });
    }
  } catch (error) {
    window.location.href = "/login";
  }
}

async function cerrarSesion() {
  await fetch("/api/logout", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({})
  });
  window.location.href = "/login";
}

document.addEventListener("DOMContentLoaded", () => {
  verificarSesion();

  const botonCerrarSesion = document.getElementById("btn-cerrar-sesion");
  if (botonCerrarSesion) {
    botonCerrarSesion.addEventListener("click", cerrarSesion);
  }
});
