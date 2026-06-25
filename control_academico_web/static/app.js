async function verificarSesion() {
  try {
    const respuesta = await fetch("/api/session");
    const datos = await respuesta.json();

    if (!datos.resultado) {
      window.location.href = "/login";
      return;
    }

    const nombreUsuario = document.getElementById("usuario-sesion");
    if (nombreUsuario && datos.datos) {
      nombreUsuario.textContent = datos.datos.nombre || datos.datos.usuario || "";
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
