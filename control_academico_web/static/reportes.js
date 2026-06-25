// Lógica visual inicial del módulo Reportes.
// La conexión con Python se realizará en una etapa posterior.

let datosReporteActual = [];
let tipoReporteActual = "";

function obtenerParametrosReporte() {
  return {
    tipo_reporte: tipoReporteActual,
    codigo_materia: document.getElementById("rep-est-materia") ? document.getElementById("rep-est-materia").value.trim().toUpperCase() : "",
    codigo_periodo: document.getElementById("rep-est-periodo") ? document.getElementById("rep-est-periodo").value.trim().toUpperCase() : "",
    nombre_reporte: document.getElementById("nombre-reporte") ? document.getElementById("nombre-reporte").value.trim() : ""
  };
}

function validarParametrosReporte(tipoReporte, parametros) {
  if (!tipoReporte) {
    return "Seleccione un tipo de reporte.";
  }

  if (tipoReporte !== "riesgo") {
    if (!parametros.codigo_materia) {
      return "Ingrese el código de materia.";
    }
    if (!parametros.codigo_periodo) {
      return "Ingrese el código de periodo.";
    }
  }

  return "";
}

function mostrarMensajeReportes(mensaje, tipo) {
  const zonaMensaje = document.getElementById("zona-mensajes-reportes");
  zonaMensaje.textContent = mensaje;
  zonaMensaje.className = tipo;
}

function limpiarResultadosReporte() {
  const zonaResultados = document.getElementById("zona-resultados-reporte");
  zonaResultados.innerHTML = "<p>Seleccione un tipo de reporte y presione Generar.</p>";
  datosReporteActual = [];
}

function renderizarResultadosReporte(datos) {
  const zonaResultados = document.getElementById("zona-resultados-reporte");
  zonaResultados.innerHTML = "";

  if (!datos || (Array.isArray(datos) && datos.length === 0)) {
    zonaResultados.innerHTML = "<p>No se encontraron registros para este reporte.</p>";
    return;
  }

  if (typeof datos === "object" && !Array.isArray(datos) && datos.detalle) {
    const resumen = document.createElement("div");
    resumen.innerHTML = "<p>Total de estudiantes: " + (datos.total_estudiantes || 0) + "</p>"
      + "<p>Aprobados: " + (datos.aprobados || 0) + "</p>"
      + "<p>Desaprobados: " + (datos.desaprobados || 0) + "</p>"
      + "<p>Promedio general: " + (datos.promedio_general || 0) + "</p>";
    zonaResultados.appendChild(resumen);
    datos = datos.detalle;
  }

  const tabla = document.createElement("table");
  tabla.id = "tabla-resultados";

  if (Array.isArray(datos) && datos.length > 0) {
    const encabezado = document.createElement("thead");
    const filaEncabezado = document.createElement("tr");

    const claves = Object.keys(datos[0]);
    for (const clave of claves) {
      const th = document.createElement("th");
      th.textContent = clave.replace(/_/g, " ");
      filaEncabezado.appendChild(th);
    }
    encabezado.appendChild(filaEncabezado);
    tabla.appendChild(encabezado);

    const cuerpo = document.createElement("tbody");
    for (const fila of datos) {
      const tr = document.createElement("tr");
      for (const clave of claves) {
        const td = document.createElement("td");
        td.textContent = fila[clave] !== null && fila[clave] !== undefined ? fila[clave] : "";
        tr.appendChild(td);
      }
      cuerpo.appendChild(tr);
    }
    tabla.appendChild(cuerpo);
  }

  zonaResultados.appendChild(tabla);
}

function prepararExportacionReporte(nombreReporte, datos) {
  if (!nombreReporte) {
    mostrarMensajeReportes("Ingrese un nombre para el reporte.", "error");
    return;
  }

  if (!datos || (Array.isArray(datos) && datos.length === 0)) {
    mostrarMensajeReportes("No hay datos para exportar.", "error");
    return;
  }

  mostrarMensajeReportes("Reporte preparado para exportar. La exportacion se conectara con Python.", "info");
}

console.log("reportes.js cargado.");
