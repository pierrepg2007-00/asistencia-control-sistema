// Lógica visual inicial del módulo Matrículas.
// La conexión con Python se realizará en una etapa posterior.

let matriculasTemporales = [];

function obtenerDatosFormularioMatricula() {
  return {
    codigo_estudiante: document.getElementById("codigo-estudiante").value.trim().toUpperCase(),
    codigo_materia: document.getElementById("codigo-materia").value.trim().toUpperCase(),
    codigo_periodo: document.getElementById("codigo-periodo").value.trim().toUpperCase()
  };
}

function validarFormularioMatricula(datos) {
  if (!datos.codigo_estudiante) {
    return "Ingrese el código de estudiante.";
  }

  if (!datos.codigo_materia) {
    return "Ingrese el código de materia.";
  }

  if (!datos.codigo_periodo) {
    return "Ingrese el código de periodo.";
  }

  return "";
}

function mostrarMensajeMatriculas(mensaje, tipo) {
  const zonaMensaje = document.getElementById("zona-mensajes-matriculas");
  zonaMensaje.textContent = mensaje;
  zonaMensaje.className = tipo;
}

function limpiarFormularioMatricula() {
  document.getElementById("formulario-matricula").reset();
}

function renderizarTablaMatriculas(matriculas) {
  const cuerpo = document.getElementById("cuerpo-tabla-matriculas");
  cuerpo.innerHTML = "";

  if (!matriculas || matriculas.length === 0) {
    const fila = document.createElement("tr");
    const celda = document.createElement("td");
    celda.colSpan = 5;
    celda.textContent = "No hay matrículas registradas.";
    fila.appendChild(celda);
    cuerpo.appendChild(fila);
    return;
  }

  for (const matricula of matriculas) {
    const fila = document.createElement("tr");

    const tdEstudiante = document.createElement("td");
    tdEstudiante.textContent = matricula.codigo_estudiante || "";
    fila.appendChild(tdEstudiante);

    const tdMateria = document.createElement("td");
    tdMateria.textContent = matricula.codigo_materia || "";
    fila.appendChild(tdMateria);

    const tdPeriodo = document.createElement("td");
    tdPeriodo.textContent = matricula.codigo_periodo || "";
    fila.appendChild(tdPeriodo);

    const tdEstado = document.createElement("td");
    tdEstado.textContent = matricula.estado || "";
    fila.appendChild(tdEstado);

    const tdAcciones = document.createElement("td");
    const btnCambiar = document.createElement("button");
    btnCambiar.textContent = "Cambiar estado";
    btnCambiar.onclick = function() {
      prepararCambioEstadoMatricula(
        matricula.codigo_estudiante,
        matricula.codigo_materia,
        matricula.codigo_periodo
      );
    };
    tdAcciones.appendChild(btnCambiar);
    fila.appendChild(tdAcciones);

    cuerpo.appendChild(fila);
  }
}

function filtrarMatriculasPorEstudiante(codigo_estudiante) {
  if (!codigo_estudiante) {
    mostrarMensajeMatriculas("Ingrese el código de estudiante para buscar.", "error");
    return;
  }

  const filtradas = matriculasTemporales.filter(function(m) {
    return m.codigo_estudiante === codigo_estudiante;
  });

  if (filtradas.length === 0) {
    mostrarMensajeMatriculas("No se encontraron matrículas para ese estudiante.", "error");
  } else {
    mostrarMensajeMatriculas("Se encontraron " + filtradas.length + " matrícula(s).", "exito");
  }

  renderizarTablaMatriculas(filtradas);
}

function filtrarMatriculasPorMateria(codigo_materia, codigo_periodo) {
  if (!codigo_materia || !codigo_periodo) {
    mostrarMensajeMatriculas("Ingrese código de materia y periodo para buscar.", "error");
    return;
  }

  const filtradas = matriculasTemporales.filter(function(m) {
    return m.codigo_materia === codigo_materia && m.codigo_periodo === codigo_periodo;
  });

  if (filtradas.length === 0) {
    mostrarMensajeMatriculas("No se encontraron matrículas para esa materia y periodo.", "error");
  } else {
    mostrarMensajeMatriculas("Se encontraron " + filtradas.length + " matrícula(s).", "exito");
  }

  renderizarTablaMatriculas(filtradas);
}

function prepararCambioEstadoMatricula(codigo_estudiante, codigo_materia, codigo_periodo) {
  document.getElementById("cambio-estudiante").value = codigo_estudiante || "";
  document.getElementById("cambio-materia").value = codigo_materia || "";
  document.getElementById("cambio-periodo").value = codigo_periodo || "";
  document.getElementById("nuevo-estado").value = "";
  mostrarMensajeMatriculas("Seleccione el nuevo estado y presione Cambiar estado.", "info");
}

console.log("matriculas.js cargado.");
