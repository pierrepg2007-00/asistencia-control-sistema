async function llamarApi(ruta, datos) {
  const respuesta = await fetch(ruta, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(datos || {})
  });
  return await respuesta.json();
}

function mostrarMensajeAsistencia(mensaje, tipo) {
  const seccion = document.getElementById("mensajes-asistencia");
  seccion.textContent = mensaje || "";
  seccion.className = "mensaje " + (tipo || "");
}

function obtenerDatosFormularioAsistencia() {
  return {
    codigo_estudiante: document.getElementById("codigo-estudiante").value.trim().toUpperCase(),
    codigo_materia: document.getElementById("codigo-materia").value.trim().toUpperCase(),
    codigo_periodo: document.getElementById("codigo-periodo").value.trim().toUpperCase(),
    fecha: document.getElementById("fecha").value.trim(),
    estado_asistencia: document.getElementById("estado-asistencia").value
  };
}

function renderizarTablaAsistencia(asistencias) {
  const tbody = document.getElementById("tbody-asistencias");
  tbody.innerHTML = "";
  if (!asistencias || asistencias.length === 0) {
    tbody.innerHTML = '<tr><td colspan="5">No hay asistencias para mostrar.</td></tr>';
    return;
  }

  asistencias.forEach((asistencia) => {
    const fila = document.createElement("tr");
    fila.innerHTML = `
      <td>${asistencia.codigo_estudiante || ""}</td>
      <td>${asistencia.codigo_materia || ""}</td>
      <td>${asistencia.codigo_periodo || ""}</td>
      <td>${asistencia.fecha || ""}</td>
      <td>${asistencia.estado_asistencia || ""}</td>
    `;
    tbody.appendChild(fila);
  });
}

async function guardarAsistencia() {
  const respuesta = await llamarApi("/api/asistencia/guardar", obtenerDatosFormularioAsistencia());
  mostrarMensajeAsistencia(respuesta.mensaje, respuesta.resultado ? "exito" : "error");
  if (respuesta.resultado) {
    document.getElementById("form-asistencia").reset();
    listarAsistencias();
  }
}

async function listarAsistencias() {
  const respuesta = await llamarApi("/api/asistencia/listar");
  renderizarTablaAsistencia(respuesta.datos || []);
}

async function listarAsistenciaPorEstudiante() {
  const codigo = document.getElementById("filtro-codigo-estudiante").value.trim().toUpperCase();
  const respuesta = await llamarApi("/api/asistencia/por-estudiante", { codigo_estudiante: codigo });
  mostrarMensajeAsistencia(respuesta.mensaje, respuesta.resultado ? "exito" : "error");
  renderizarTablaAsistencia(respuesta.datos || []);
}

async function listarAsistenciaPorMateria() {
  const datos = {
    codigo_materia: document.getElementById("filtro-codigo-materia").value.trim().toUpperCase(),
    codigo_periodo: document.getElementById("filtro-codigo-periodo").value.trim().toUpperCase(),
    fecha: document.getElementById("filtro-fecha").value.trim()
  };
  const respuesta = await llamarApi("/api/asistencia/por-materia", datos);
  mostrarMensajeAsistencia(respuesta.mensaje, respuesta.resultado ? "exito" : "error");
  renderizarTablaAsistencia(respuesta.datos || []);
}

async function calcularPorcentajeAsistencia() {
  const datos = {
    codigo_estudiante: document.getElementById("calc-codigo-estudiante").value.trim().toUpperCase(),
    codigo_materia: document.getElementById("calc-codigo-materia").value.trim().toUpperCase(),
    codigo_periodo: document.getElementById("calc-codigo-periodo").value.trim().toUpperCase()
  };
  const respuesta = await llamarApi("/api/asistencia/porcentaje", datos);
  const resultado = respuesta.datos || {};
  document.getElementById("resultado-porcentaje").textContent =
    "Asistencia: " + (resultado.porcentaje_asistencia || 0) + "% (" +
    (resultado.asistencias || 0) + " asistencias de " + (resultado.total_clases || 0) + " clases).";
  mostrarMensajeAsistencia(respuesta.mensaje, respuesta.resultado ? "exito" : "error");
}

document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("btn-guardar-asistencia").addEventListener("click", guardarAsistencia);
  document.getElementById("btn-listar-asistencias").addEventListener("click", listarAsistencias);
  document.getElementById("btn-listar-por-estudiante").addEventListener("click", listarAsistenciaPorEstudiante);
  document.getElementById("btn-listar-por-materia").addEventListener("click", listarAsistenciaPorMateria);
  document.getElementById("btn-calcular-porcentaje").addEventListener("click", calcularPorcentajeAsistencia);
  listarAsistencias();
});
