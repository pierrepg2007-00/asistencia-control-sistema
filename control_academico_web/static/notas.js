async function llamarApi(ruta, datos) {
  const respuesta = await fetch(ruta, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(datos || {})
  });
  return await respuesta.json();
}

function mostrarMensajeNotas(mensaje, tipo) {
  const zona = document.getElementById("mensaje-notas");
  zona.textContent = mensaje || "";
  zona.className = "mensaje " + (tipo || "");
}

function datosNota() {
  return {
    codigo_estudiante: document.getElementById("codigo-estudiante").value.trim().toUpperCase(),
    codigo_materia: document.getElementById("codigo-materia").value.trim().toUpperCase(),
    codigo_periodo: document.getElementById("codigo-periodo").value.trim().toUpperCase(),
    nota1: document.getElementById("nota1").value.trim(),
    nota2: document.getElementById("nota2").value.trim(),
    nota3: document.getElementById("nota3").value.trim()
  };
}

function renderizarTablaNotas(notas) {
  const cuerpo = document.getElementById("tabla-notas");
  cuerpo.innerHTML = "";
  if (!notas || notas.length === 0) {
    cuerpo.innerHTML = '<tr><td colspan="9">No hay notas para mostrar.</td></tr>';
    return;
  }

  notas.forEach((nota) => {
    const fila = document.createElement("tr");
    fila.innerHTML = `
      <td>${nota.codigo_estudiante || ""}</td>
      <td>${nota.codigo_materia || ""}</td>
      <td>${nota.codigo_periodo || ""}</td>
      <td>${nota.nota1 || ""}</td>
      <td>${nota.nota2 || ""}</td>
      <td>${nota.nota3 || ""}</td>
      <td>${nota.promedio || ""}</td>
      <td>${nota.estado_final || ""}</td>
      <td><button type="button" class="secundario btn-editar-nota" data-estudiante="${nota.codigo_estudiante || ""}" data-materia="${nota.codigo_materia || ""}" data-periodo="${nota.codigo_periodo || ""}">Editar</button></td>
    `;
    cuerpo.appendChild(fila);
  });
}

function cargarNotaFormulario(nota) {
  document.getElementById("codigo-estudiante").value = nota.codigo_estudiante || "";
  document.getElementById("codigo-materia").value = nota.codigo_materia || "";
  document.getElementById("codigo-periodo").value = nota.codigo_periodo || "";
  document.getElementById("nota1").value = nota.nota1 || "";
  document.getElementById("nota2").value = nota.nota2 || "";
  document.getElementById("nota3").value = nota.nota3 || "";
}

async function guardarNota() {
  const respuesta = await llamarApi("/api/notas/guardar", datosNota());
  mostrarMensajeNotas(respuesta.mensaje, respuesta.resultado ? "exito" : "error");
  if (respuesta.resultado) {
    document.getElementById("formulario-nota").reset();
    listarNotas();
  }
}

async function listarNotas() {
  const respuesta = await llamarApi("/api/notas/listar");
  renderizarTablaNotas(respuesta.datos || []);
}

async function listarNotasPorEstudiante() {
  const codigo = document.getElementById("buscar-estudiante-notas").value.trim().toUpperCase();
  const respuesta = await llamarApi("/api/notas/por-estudiante", { codigo_estudiante: codigo });
  mostrarMensajeNotas(respuesta.mensaje, respuesta.resultado ? "exito" : "error");
  renderizarTablaNotas(respuesta.datos || []);
}

async function listarNotasPorMateria() {
  const datos = {
    codigo_materia: document.getElementById("buscar-materia-notas").value.trim().toUpperCase(),
    codigo_periodo: document.getElementById("buscar-periodo-notas").value.trim().toUpperCase()
  };
  const respuesta = await llamarApi("/api/notas/por-materia", datos);
  mostrarMensajeNotas(respuesta.mensaje, respuesta.resultado ? "exito" : "error");
  renderizarTablaNotas(respuesta.datos || []);
}

async function actualizarNota() {
  const respuesta = await llamarApi("/api/notas/actualizar", datosNota());
  mostrarMensajeNotas(respuesta.mensaje, respuesta.resultado ? "exito" : "error");
  if (respuesta.resultado) {
    listarNotas();
  }
}

async function prepararActualizacionNota(codigoEstudiante, codigoMateria, codigoPeriodo) {
  const respuesta = await llamarApi("/api/notas/por-materia", {
    codigo_materia: codigoMateria,
    codigo_periodo: codigoPeriodo
  });
  const nota = (respuesta.datos || []).find((item) => item.codigo_estudiante === codigoEstudiante);
  if (nota) {
    cargarNotaFormulario(nota);
    mostrarMensajeNotas("Nota cargada para actualizar.", "info");
  }
}

document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("btn-guardar-nota").addEventListener("click", guardarNota);
  document.getElementById("btn-actualizar-nota").addEventListener("click", actualizarNota);
  document.getElementById("btn-listar-notas").addEventListener("click", listarNotas);
  document.getElementById("btn-listar-notas-estudiante").addEventListener("click", listarNotasPorEstudiante);
  document.getElementById("btn-listar-notas-materia").addEventListener("click", listarNotasPorMateria);
  document.getElementById("tabla-notas").addEventListener("click", (evento) => {
    if (evento.target.classList.contains("btn-editar-nota")) {
      prepararActualizacionNota(
        evento.target.dataset.estudiante,
        evento.target.dataset.materia,
        evento.target.dataset.periodo
      );
    }
  });
  listarNotas();
});
