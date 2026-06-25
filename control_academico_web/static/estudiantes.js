let estudiantesActuales = [];

async function llamarApi(ruta, datos) {
  const respuesta = await fetch(ruta, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(datos || {})
  });
  return await respuesta.json();
}

function mostrarMensajeEstudiantes(mensaje, tipo) {
  const zonaMensaje = document.getElementById("mensaje-estudiantes");
  zonaMensaje.textContent = mensaje || "";
  zonaMensaje.className = "mensaje " + (tipo || "");
}

function obtenerDatosFormulario() {
  return {
    codigo: document.getElementById("codigo-estudiante-editar").value.trim(),
    nombres: document.getElementById("nombres").value.trim(),
    apellidos: document.getElementById("apellidos").value.trim(),
    dni: document.getElementById("dni").value.trim(),
    correo: document.getElementById("correo").value.trim(),
    estado: document.getElementById("estado").value
  };
}

function limpiarFormularioEstudiante() {
  document.getElementById("formulario-estudiante").reset();
  document.getElementById("codigo-estudiante-editar").value = "";
  document.getElementById("dni").disabled = false;
}

function renderizarTablaEstudiantes(estudiantes) {
  const cuerpoTabla = document.getElementById("tabla-estudiantes");
  cuerpoTabla.innerHTML = "";

  if (!estudiantes || estudiantes.length === 0) {
    cuerpoTabla.innerHTML = '<tr><td colspan="7">No hay estudiantes para mostrar.</td></tr>';
    return;
  }

  estudiantes.forEach((estudiante) => {
    const fila = document.createElement("tr");
    fila.innerHTML = `
      <td>${estudiante.codigo || ""}</td>
      <td>${estudiante.nombres || ""}</td>
      <td>${estudiante.apellidos || ""}</td>
      <td>${estudiante.dni || ""}</td>
      <td>${estudiante.correo || ""}</td>
      <td>${estudiante.estado || ""}</td>
      <td><button type="button" class="secundario btn-editar-estudiante" data-codigo="${estudiante.codigo || ""}">Editar</button></td>
    `;
    cuerpoTabla.appendChild(fila);
  });
}

function cargarEstudianteEnFormulario(estudiante) {
  document.getElementById("codigo-estudiante-editar").value = estudiante.codigo || "";
  document.getElementById("nombres").value = estudiante.nombres || "";
  document.getElementById("apellidos").value = estudiante.apellidos || "";
  document.getElementById("dni").value = estudiante.dni || "";
  document.getElementById("correo").value = estudiante.correo || "";
  document.getElementById("estado").value = estudiante.estado || "activo";
  document.getElementById("dni").disabled = true;
}

async function guardarEstudiante() {
  const datos = obtenerDatosFormulario();
  const respuesta = await llamarApi("/api/estudiantes/guardar", datos);
  mostrarMensajeEstudiantes(respuesta.mensaje, respuesta.resultado ? "exito" : "error");
  if (respuesta.resultado) {
    limpiarFormularioEstudiante();
    listarEstudiantes();
  }
}

async function listarEstudiantes() {
  const respuesta = await llamarApi("/api/estudiantes/listar");
  estudiantesActuales = respuesta.datos || [];
  renderizarTablaEstudiantes(estudiantesActuales);
}

async function buscarEstudiante() {
  const valor = document.getElementById("buscar-estudiante").value.trim();
  const respuesta = await llamarApi("/api/estudiantes/buscar", { valor: valor });
  mostrarMensajeEstudiantes(respuesta.mensaje, respuesta.resultado ? "exito" : "error");
  renderizarTablaEstudiantes(respuesta.resultado ? [respuesta.datos] : estudiantesActuales);
}

async function actualizarEstudiante() {
  const datos = obtenerDatosFormulario();
  if (!datos.codigo) {
    mostrarMensajeEstudiantes("Seleccione un estudiante con Editar antes de actualizar.", "error");
    return;
  }

  const respuesta = await llamarApi("/api/estudiantes/actualizar", datos);
  mostrarMensajeEstudiantes(respuesta.mensaje, respuesta.resultado ? "exito" : "error");
  if (respuesta.resultado) {
    limpiarFormularioEstudiante();
    listarEstudiantes();
  }
}

function prepararActualizacionEstudiante(codigo) {
  const estudiante = estudiantesActuales.find((item) => item.codigo === codigo);
  if (!estudiante) {
    mostrarMensajeEstudiantes("No se encontro el estudiante para editar.", "error");
    return;
  }
  cargarEstudianteEnFormulario(estudiante);
  mostrarMensajeEstudiantes("Datos cargados para actualizar.", "info");
}

document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("btn-guardar-estudiante").addEventListener("click", guardarEstudiante);
  document.getElementById("btn-actualizar-estudiante").addEventListener("click", actualizarEstudiante);
  document.getElementById("btn-limpiar-estudiante").addEventListener("click", limpiarFormularioEstudiante);
  document.getElementById("btn-buscar-estudiante").addEventListener("click", buscarEstudiante);
  document.getElementById("btn-listar-estudiantes").addEventListener("click", listarEstudiantes);
  document.getElementById("tabla-estudiantes").addEventListener("click", (evento) => {
    if (evento.target.classList.contains("btn-editar-estudiante")) {
      prepararActualizacionEstudiante(evento.target.dataset.codigo);
    }
  });
  listarEstudiantes();
});
