// Lógica visual inicial del módulo Notas.
// La conexión con Python se realizará en una etapa posterior.

let notasTemporales = [];

function obtenerDatosFormularioNota() {
  return {
    codigo_estudiante: document.getElementById("codigo-estudiante").value.trim().toUpperCase(),
    codigo_materia: document.getElementById("codigo-materia").value.trim().toUpperCase(),
    codigo_periodo: document.getElementById("codigo-periodo").value.trim().toUpperCase(),
    nota1: document.getElementById("nota1").value.trim(),
    nota2: document.getElementById("nota2").value.trim(),
    nota3: document.getElementById("nota3").value.trim()
  };
}

function validarFormularioNota(datos) {
  if (!datos.codigo_estudiante) {
    return "Ingrese el código de estudiante.";
  }

  if (!datos.codigo_materia) {
    return "Ingrese el código de materia.";
  }

  if (!datos.codigo_periodo) {
    return "Ingrese el código de periodo.";
  }

  const notas = [datos.nota1, datos.nota2, datos.nota3];

  for (const nota of notas) {
    const numero = Number(nota);

    if (nota === "" || Number.isNaN(numero) || numero < 0 || numero > 20) {
      return "Las notas deben ser números entre 0 y 20.";
    }
  }

  return "";
}

function mostrarMensajeNotas(mensaje, tipo) {
  const zonaMensaje = document.getElementById("mensaje-notas");
  zonaMensaje.textContent = mensaje;
  zonaMensaje.className = tipo;
}

function limpiarFormularioNota() {
  document.getElementById("formulario-nota").reset();
}

function calcularPromedioVisual(nota1, nota2, nota3) {
  const promedio = (Number(nota1) + Number(nota2) + Number(nota3)) / 3;
  return Math.round(promedio * 100) / 100;
}

function renderizarTablaNotas(notas) {
  const cuerpoTabla = document.getElementById("tabla-notas");
  cuerpoTabla.innerHTML = "";

  notas.forEach((nota) => {
    const fila = document.createElement("tr");

    fila.innerHTML = `
      <td>${nota.codigo_estudiante}</td>
      <td>${nota.codigo_materia}</td>
      <td>${nota.codigo_periodo}</td>
      <td>${nota.nota1}</td>
      <td>${nota.nota2}</td>
      <td>${nota.nota3}</td>
      <td>${nota.promedio}</td>
      <td>${nota.estado_final}</td>
      <td>
        <button
          type="button"
          class="btn-editar-nota"
          data-estudiante="${nota.codigo_estudiante}"
          data-materia="${nota.codigo_materia}"
          data-periodo="${nota.codigo_periodo}">
          Editar
        </button>
      </td>
    `;

    cuerpoTabla.appendChild(fila);
  });
}

function filtrarNotasPorEstudiante(codigo_estudiante) {
  const codigo = codigo_estudiante.trim().toUpperCase();

  return notasTemporales.filter((nota) => {
    return nota.codigo_estudiante === codigo;
  });
}

function filtrarNotasPorMateria(codigo_materia, codigo_periodo) {
  const materia = codigo_materia.trim().toUpperCase();
  const periodo = codigo_periodo.trim().toUpperCase();

  return notasTemporales.filter((nota) => {
    return nota.codigo_materia === materia && nota.codigo_periodo === periodo;
  });
}

function prepararActualizacionNota(codigo_estudiante, codigo_materia, codigo_periodo) {
  const notaEncontrada = notasTemporales.find((nota) => {
    return (
      nota.codigo_estudiante === codigo_estudiante
      && nota.codigo_materia === codigo_materia
      && nota.codigo_periodo === codigo_periodo
    );
  });

  if (!notaEncontrada) {
    mostrarMensajeNotas("No se encontró la nota para editar.", "error");
    return;
  }

  document.getElementById("codigo-estudiante").value = notaEncontrada.codigo_estudiante;
  document.getElementById("codigo-materia").value = notaEncontrada.codigo_materia;
  document.getElementById("codigo-periodo").value = notaEncontrada.codigo_periodo;
  document.getElementById("nota1").value = notaEncontrada.nota1;
  document.getElementById("nota2").value = notaEncontrada.nota2;
  document.getElementById("nota3").value = notaEncontrada.nota3;

  mostrarMensajeNotas("Nota cargada para actualización visual.", "confirmacion");
}

document.addEventListener("DOMContentLoaded", () => {
  const formulario = document.getElementById("formulario-nota");
  const botonListarEstudiante = document.getElementById("btn-listar-notas-estudiante");
  const botonListarMateria = document.getElementById("btn-listar-notas-materia");
  const tablaNotas = document.getElementById("tabla-notas");

  formulario.addEventListener("submit", (evento) => {
    evento.preventDefault();

    const datos = obtenerDatosFormularioNota();
    const error = validarFormularioNota(datos);

    if (error) {
      mostrarMensajeNotas(error, "error");
      return;
    }

    datos.nota1 = Number(datos.nota1);
    datos.nota2 = Number(datos.nota2);
    datos.nota3 = Number(datos.nota3);
    datos.promedio = calcularPromedioVisual(datos.nota1, datos.nota2, datos.nota3);
    datos.estado_final = datos.promedio >= 11 ? "aprobado" : "desaprobado";

    notasTemporales.push(datos);
    renderizarTablaNotas(notasTemporales);
    limpiarFormularioNota();
    mostrarMensajeNotas("Nota agregada visualmente. Falta conectar con Python.", "confirmacion");
  });

  botonListarEstudiante.addEventListener("click", () => {
    const codigo = document.getElementById("buscar-estudiante-notas").value;
    const notas = filtrarNotasPorEstudiante(codigo);
    renderizarTablaNotas(notas);
    mostrarMensajeNotas("Filtro por estudiante aplicado.", "confirmacion");
  });

  botonListarMateria.addEventListener("click", () => {
    const materia = document.getElementById("buscar-materia-notas").value;
    const periodo = document.getElementById("buscar-periodo-notas").value;
    const notas = filtrarNotasPorMateria(materia, periodo);
    renderizarTablaNotas(notas);
    mostrarMensajeNotas("Filtro por materia y periodo aplicado.", "confirmacion");
  });

  tablaNotas.addEventListener("click", (evento) => {
    if (evento.target.classList.contains("btn-editar-nota")) {
      prepararActualizacionNota(
        evento.target.dataset.estudiante,
        evento.target.dataset.materia,
        evento.target.dataset.periodo
      );
    }
  });
});
