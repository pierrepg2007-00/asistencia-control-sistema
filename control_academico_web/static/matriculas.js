async function llamarApi(ruta, datos) {
  const respuesta = await fetch(ruta, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(datos || {})
  });
  return await respuesta.json();
}

function mostrarMensajeMatriculas(mensaje, tipo) {
  const zona = document.getElementById("zona-mensajes-matriculas");
  zona.textContent = mensaje || "";
  zona.className = "mensaje " + (tipo || "");
}

function datosRegistroMatricula() {
  return {
    codigo_estudiante: document.getElementById("codigo-estudiante").value.trim().toUpperCase(),
    codigo_materia: document.getElementById("codigo-materia").value.trim().toUpperCase(),
    codigo_periodo: document.getElementById("codigo-periodo").value.trim().toUpperCase()
  };
}

function datosBusquedaMatricula() {
  return {
    codigo_estudiante: document.getElementById("buscar-estudiante").value.trim().toUpperCase(),
    codigo_materia: document.getElementById("buscar-materia").value.trim().toUpperCase(),
    codigo_periodo: document.getElementById("buscar-periodo").value.trim().toUpperCase()
  };
}

function renderizarTablaMatriculas(matriculas) {
  const cuerpo = document.getElementById("cuerpo-tabla-matriculas");
  cuerpo.innerHTML = "";
  if (!matriculas || matriculas.length === 0) {
    cuerpo.innerHTML = '<tr><td colspan="5">No hay matriculas para mostrar.</td></tr>';
    return;
  }

  matriculas.forEach((matricula) => {
    const fila = document.createElement("tr");
    fila.innerHTML = `
      <td>${matricula.codigo_estudiante || ""}</td>
      <td>${matricula.codigo_materia || ""}</td>
      <td>${matricula.codigo_periodo || ""}</td>
      <td>${matricula.estado || ""}</td>
      <td><button type="button" class="secundario btn-preparar-estado" data-estudiante="${matricula.codigo_estudiante || ""}" data-materia="${matricula.codigo_materia || ""}" data-periodo="${matricula.codigo_periodo || ""}">Cambiar</button></td>
    `;
    cuerpo.appendChild(fila);
  });
}

async function registrarMatricula() {
  const respuesta = await llamarApi("/api/matriculas/guardar", datosRegistroMatricula());
  mostrarMensajeMatriculas(respuesta.mensaje, respuesta.resultado ? "exito" : "error");
  if (respuesta.resultado) {
    document.getElementById("formulario-matricula").reset();
    listarMatriculas();
  }
}

async function listarMatriculas() {
  const respuesta = await llamarApi("/api/matriculas/listar");
  renderizarTablaMatriculas(respuesta.datos || []);
}

async function buscarMatriculaExacta() {
  const respuesta = await llamarApi("/api/matriculas/buscar", datosBusquedaMatricula());
  mostrarMensajeMatriculas(respuesta.mensaje, respuesta.resultado ? "exito" : "error");
  renderizarTablaMatriculas(respuesta.resultado ? [respuesta.datos] : []);
}

async function listarMatriculasPorEstudiante() {
  const datos = datosBusquedaMatricula();
  const respuesta = await llamarApi("/api/matriculas/por-estudiante", datos);
  mostrarMensajeMatriculas(respuesta.mensaje, respuesta.resultado ? "exito" : "error");
  renderizarTablaMatriculas(respuesta.datos || []);
}

async function listarMatriculasPorMateria() {
  const datos = datosBusquedaMatricula();
  const respuesta = await llamarApi("/api/matriculas/por-materia", datos);
  mostrarMensajeMatriculas(respuesta.mensaje, respuesta.resultado ? "exito" : "error");
  renderizarTablaMatriculas(respuesta.datos || []);
}

function prepararCambioEstadoMatricula(codigoEstudiante, codigoMateria, codigoPeriodo) {
  document.getElementById("cambio-estudiante").value = codigoEstudiante || "";
  document.getElementById("cambio-materia").value = codigoMateria || "";
  document.getElementById("cambio-periodo").value = codigoPeriodo || "";
  mostrarMensajeMatriculas("Datos cargados para cambiar estado.", "info");
}

async function cambiarEstadoMatricula() {
  const datos = {
    codigo_estudiante: document.getElementById("cambio-estudiante").value.trim().toUpperCase(),
    codigo_materia: document.getElementById("cambio-materia").value.trim().toUpperCase(),
    codigo_periodo: document.getElementById("cambio-periodo").value.trim().toUpperCase(),
    estado: document.getElementById("nuevo-estado").value
  };
  const respuesta = await llamarApi("/api/matriculas/cambiar-estado", datos);
  mostrarMensajeMatriculas(respuesta.mensaje, respuesta.resultado ? "exito" : "error");
  if (respuesta.resultado) {
    listarMatriculas();
  }
}

document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("btn-registrar-matricula").addEventListener("click", registrarMatricula);
  document.getElementById("btn-listar-todas").addEventListener("click", listarMatriculas);
  document.getElementById("btn-buscar-exacta").addEventListener("click", buscarMatriculaExacta);
  document.getElementById("btn-listar-estudiante").addEventListener("click", listarMatriculasPorEstudiante);
  document.getElementById("btn-listar-materia").addEventListener("click", listarMatriculasPorMateria);
  document.getElementById("btn-cambiar-estado").addEventListener("click", cambiarEstadoMatricula);
  document.getElementById("cuerpo-tabla-matriculas").addEventListener("click", (evento) => {
    if (evento.target.classList.contains("btn-preparar-estado")) {
      prepararCambioEstadoMatricula(
        evento.target.dataset.estudiante,
        evento.target.dataset.materia,
        evento.target.dataset.periodo
      );
    }
  });
  listarMatriculas();
});
