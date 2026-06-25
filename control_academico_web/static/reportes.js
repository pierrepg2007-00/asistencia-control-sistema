let datosReporteActual = null;
let tipoReporteActual = "";

async function llamarApi(ruta, datos) {
  const respuesta = await fetch(ruta, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(datos || {})
  });
  return await respuesta.json();
}

function mostrarMensajeReportes(mensaje, tipo) {
  const zona = document.getElementById("zona-mensajes-reportes");
  zona.textContent = mensaje || "";
  zona.className = "mensaje " + (tipo || "");
}

function parametrosMateriaPeriodo() {
  return {
    codigo_materia: document.getElementById("rep-materia").value.trim().toUpperCase(),
    codigo_periodo: document.getElementById("rep-periodo").value.trim().toUpperCase()
  };
}

function renderizarResultadosReporte(datos) {
  const zona = document.getElementById("zona-resultados-reporte");
  zona.innerHTML = "";

  if (!datos || (Array.isArray(datos) && datos.length === 0)) {
    zona.innerHTML = "<p>No se encontraron registros para este reporte.</p>";
    return;
  }

  if (!Array.isArray(datos) && datos.detalle) {
    const resumen = document.createElement("div");
    resumen.className = "resumen-reporte";
    resumen.innerHTML =
      "<p>Total de estudiantes: " + (datos.total_estudiantes || 0) + "</p>" +
      "<p>Aprobados: " + (datos.aprobados || 0) + "</p>" +
      "<p>Desaprobados: " + (datos.desaprobados || 0) + "</p>" +
      "<p>Promedio general: " + (datos.promedio_general || 0) + "</p>";
    zona.appendChild(resumen);
    datos = datos.detalle || [];
  }

  if (!Array.isArray(datos) || datos.length === 0) {
    zona.innerHTML += "<p>No se encontraron registros para este reporte.</p>";
    return;
  }

  const tabla = document.createElement("table");
  const encabezado = document.createElement("thead");
  const filaEncabezado = document.createElement("tr");
  const claves = Object.keys(datos[0]);

  claves.forEach((clave) => {
    const th = document.createElement("th");
    th.textContent = clave.replace(/_/g, " ");
    filaEncabezado.appendChild(th);
  });
  encabezado.appendChild(filaEncabezado);
  tabla.appendChild(encabezado);

  const cuerpo = document.createElement("tbody");
  datos.forEach((item) => {
    const fila = document.createElement("tr");
    claves.forEach((clave) => {
      const td = document.createElement("td");
      td.textContent = item[clave] === null || item[clave] === undefined ? "" : item[clave];
      fila.appendChild(td);
    });
    cuerpo.appendChild(fila);
  });
  tabla.appendChild(cuerpo);
  zona.appendChild(tabla);
}

async function reporteEstudiantesPorMateria() {
  const respuesta = await llamarApi("/api/reportes/estudiantes-materia", parametrosMateriaPeriodo());
  datosReporteActual = respuesta.datos;
  tipoReporteActual = "estudiantes_por_materia";
  renderizarResultadosReporte(datosReporteActual);
  mostrarMensajeReportes(respuesta.mensaje, respuesta.resultado ? "exito" : "error");
}

async function reporteNotasPorMateria() {
  const respuesta = await llamarApi("/api/reportes/notas-materia", parametrosMateriaPeriodo());
  datosReporteActual = respuesta.datos;
  tipoReporteActual = "notas_por_materia";
  renderizarResultadosReporte(datosReporteActual);
  mostrarMensajeReportes(respuesta.mensaje, respuesta.resultado ? "exito" : "error");
}

async function reporteAsistenciaPorMateria() {
  const respuesta = await llamarApi("/api/reportes/asistencia-materia", parametrosMateriaPeriodo());
  datosReporteActual = respuesta.datos;
  tipoReporteActual = "asistencia_por_materia";
  renderizarResultadosReporte(datosReporteActual);
  mostrarMensajeReportes(respuesta.mensaje, respuesta.resultado ? "exito" : "error");
}

async function reporteEstudiantesEnRiesgo() {
  const respuesta = await llamarApi("/api/reportes/riesgo");
  datosReporteActual = respuesta.datos;
  tipoReporteActual = "estudiantes_en_riesgo";
  renderizarResultadosReporte(datosReporteActual);
  mostrarMensajeReportes(respuesta.mensaje, respuesta.resultado ? "exito" : "error");
}

async function exportarReporteTxt() {
  const nombre = document.getElementById("nombre-reporte").value.trim() || tipoReporteActual || "reporte";
  if (!datosReporteActual) {
    mostrarMensajeReportes("Genere un reporte antes de exportar.", "error");
    return;
  }
  const respuesta = await llamarApi("/api/reportes/exportar", {
    nombre_reporte: nombre,
    datos: datosReporteActual
  });
  mostrarMensajeReportes(respuesta.mensaje + (respuesta.ruta ? " Ruta: " + respuesta.ruta : ""), respuesta.resultado ? "exito" : "error");
}

document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("btn-reporte-estudiantes").addEventListener("click", reporteEstudiantesPorMateria);
  document.getElementById("btn-reporte-notas").addEventListener("click", reporteNotasPorMateria);
  document.getElementById("btn-reporte-asistencia").addEventListener("click", reporteAsistenciaPorMateria);
  document.getElementById("btn-reporte-riesgo").addEventListener("click", reporteEstudiantesEnRiesgo);
  document.getElementById("btn-exportar").addEventListener("click", exportarReporteTxt);
});
