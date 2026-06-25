// Lógica visual inicial del módulo estudiantes.
// La conexión con Python se realizará en una etapa posterior.

let estudiantesTemporales = [];
let contadorTemporal = 1;

function obtenerDatosFormulario() {
  return {
    nombres: document.getElementById("nombres").value.trim(),
    apellidos: document.getElementById("apellidos").value.trim(),
    dni: document.getElementById("dni").value.trim(),
    correo: document.getElementById("correo").value.trim(),
    estado: document.getElementById("estado").value
  };
}

function validarFormularioEstudiante(datos) {
  if (!datos.nombres) {
    return "Ingrese los nombres del estudiante.";
  }

  if (!datos.apellidos) {
    return "Ingrese los apellidos del estudiante.";
  }

  if (!datos.dni) {
    return "Ingrese el DNI del estudiante.";
  }

  if (!datos.correo) {
    return "Ingrese el correo del estudiante.";
  }

  if (!datos.estado) {
    return "Seleccione el estado del estudiante.";
  }

  return "";
}

function mostrarMensajeEstudiantes(mensaje, tipo) {
  const zonaMensaje = document.getElementById("mensaje-estudiantes");
  zonaMensaje.textContent = mensaje;
  zonaMensaje.className = tipo;
}

function limpiarFormularioEstudiante() {
  document.getElementById("formulario-estudiante").reset();
}

function renderizarTablaEstudiantes(estudiantes) {
  const cuerpoTabla = document.getElementById("tabla-estudiantes");
  cuerpoTabla.innerHTML = "";

  estudiantes.forEach((estudiante) => {
    const fila = document.createElement("tr");

    fila.innerHTML = `
      <td>${estudiante.codigo}</td>
      <td>${estudiante.nombres}</td>
      <td>${estudiante.apellidos}</td>
      <td>${estudiante.dni}</td>
      <td>${estudiante.correo}</td>
      <td>${estudiante.estado}</td>
      <td>
        <button type="button" data-codigo="${estudiante.codigo}" class="btn-editar-estudiante">
          Editar
        </button>
      </td>
    `;

    cuerpoTabla.appendChild(fila);
  });
}

function buscarEstudianteEnTabla(valor) {
  const textoBusqueda = valor.trim().toUpperCase();

  return estudiantesTemporales.find((estudiante) => {
    return estudiante.codigo === textoBusqueda || estudiante.dni === valor.trim();
  });
}

function prepararActualizacionEstudiante(codigo) {
  const estudiante = buscarEstudianteEnTabla(codigo);

  if (!estudiante) {
    mostrarMensajeEstudiantes("No se encontró el estudiante para editar.", "error");
    return;
  }

  document.getElementById("nombres").value = estudiante.nombres;
  document.getElementById("apellidos").value = estudiante.apellidos;
  document.getElementById("dni").value = estudiante.dni;
  document.getElementById("correo").value = estudiante.correo;
  document.getElementById("estado").value = estudiante.estado;

  mostrarMensajeEstudiantes("Datos cargados para actualización visual.", "confirmacion");
}

document.addEventListener("DOMContentLoaded", () => {
  const formulario = document.getElementById("formulario-estudiante");
  const botonBuscar = document.getElementById("btn-buscar-estudiante");
  const tabla = document.getElementById("tabla-estudiantes");

  formulario.addEventListener("submit", (evento) => {
    evento.preventDefault();

    const datos = obtenerDatosFormulario();
    const error = validarFormularioEstudiante(datos);

    if (error) {
      mostrarMensajeEstudiantes(error, "error");
      return;
    }

    datos.codigo = `EST${String(contadorTemporal).padStart(3, "0")}`;
    contadorTemporal += 1;
    estudiantesTemporales.push(datos);

    renderizarTablaEstudiantes(estudiantesTemporales);
    limpiarFormularioEstudiante();
    mostrarMensajeEstudiantes("Estudiante agregado visualmente. Falta conectar con Python.", "confirmacion");
  });

  botonBuscar.addEventListener("click", () => {
    const valor = document.getElementById("buscar-estudiante").value;
    const estudiante = buscarEstudianteEnTabla(valor);

    if (estudiante) {
      renderizarTablaEstudiantes([estudiante]);
      mostrarMensajeEstudiantes("Estudiante encontrado en la tabla.", "confirmacion");
    } else {
      renderizarTablaEstudiantes(estudiantesTemporales);
      mostrarMensajeEstudiantes("No se encontró el estudiante en la tabla.", "error");
    }
  });

  tabla.addEventListener("click", (evento) => {
    if (evento.target.classList.contains("btn-editar-estudiante")) {
      prepararActualizacionEstudiante(evento.target.dataset.codigo);
    }
  });
});
