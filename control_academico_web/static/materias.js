// Lógica visual inicial del módulo Materias y periodos.
// La conexión con Python se realizará en una etapa posterior.

let materiasTemporales = [];
let periodosTemporales = [];
let contadorMateriaTemporal = 1;

function obtenerDatosFormularioMateria() {
  return {
    nombre_materia: document.getElementById("nombre-materia").value.trim(),
    docente: document.getElementById("docente").value.trim(),
    ciclo: document.getElementById("ciclo").value.trim(),
    estado: document.getElementById("estado-materia").value
  };
}

function validarFormularioMateria(datos) {
  if (!datos.nombre_materia) {
    return "Ingrese el nombre de la materia.";
  }

  if (!datos.docente) {
    return "Ingrese el docente de la materia.";
  }

  if (!datos.ciclo || Number(datos.ciclo) <= 0) {
    return "Ingrese un ciclo válido.";
  }

  if (!datos.estado) {
    return "Seleccione el estado de la materia.";
  }

  return "";
}

function mostrarMensajeMaterias(mensaje, tipo) {
  const zonaMensaje = document.getElementById("mensaje-materias");
  zonaMensaje.textContent = mensaje;
  zonaMensaje.className = tipo;
}

function limpiarFormularioMateria() {
  document.getElementById("formulario-materia").reset();
}

function renderizarTablaMaterias(materias) {
  const cuerpoTabla = document.getElementById("tabla-materias");
  cuerpoTabla.innerHTML = "";

  materias.forEach((materia) => {
    const fila = document.createElement("tr");

    fila.innerHTML = `
      <td>${materia.codigo_materia}</td>
      <td>${materia.nombre_materia}</td>
      <td>${materia.docente}</td>
      <td>${materia.ciclo}</td>
      <td>${materia.estado}</td>
      <td>
        <button type="button" data-codigo="${materia.codigo_materia}" class="btn-editar-materia">
          Editar
        </button>
      </td>
    `;

    cuerpoTabla.appendChild(fila);
  });
}

function buscarMateriaEnTabla(valor) {
  const codigo = valor.trim().toUpperCase();

  return materiasTemporales.find((materia) => {
    return materia.codigo_materia === codigo;
  });
}

function prepararActualizacionMateria(codigo_materia) {
  const materia = buscarMateriaEnTabla(codigo_materia);

  if (!materia) {
    mostrarMensajeMaterias("No se encontró la materia para editar.", "error");
    return;
  }

  document.getElementById("nombre-materia").value = materia.nombre_materia;
  document.getElementById("docente").value = materia.docente;
  document.getElementById("ciclo").value = materia.ciclo;
  document.getElementById("estado-materia").value = materia.estado;

  mostrarMensajeMaterias("Datos de materia cargados para actualización visual.", "confirmacion");
}

function obtenerDatosFormularioPeriodo() {
  return {
    codigo_periodo: document.getElementById("codigo-periodo").value.trim().toUpperCase(),
    anio: document.getElementById("anio-periodo").value.trim(),
    nombre: document.getElementById("nombre-periodo").value.trim(),
    estado: document.getElementById("estado-periodo").value
  };
}

function validarFormularioPeriodo(datos) {
  if (!datos.codigo_periodo) {
    return "Ingrese el código del periodo.";
  }

  if (!datos.anio || Number(datos.anio) <= 0) {
    return "Ingrese un año válido.";
  }

  if (!datos.nombre) {
    return "Ingrese el nombre del periodo.";
  }

  if (!datos.estado) {
    return "Seleccione el estado del periodo.";
  }

  return "";
}

function limpiarFormularioPeriodo() {
  document.getElementById("formulario-periodo").reset();
}

function renderizarTablaPeriodos(periodos) {
  const cuerpoTabla = document.getElementById("tabla-periodos");
  cuerpoTabla.innerHTML = "";

  periodos.forEach((periodo) => {
    const fila = document.createElement("tr");

    fila.innerHTML = `
      <td>${periodo.codigo_periodo}</td>
      <td>${periodo.anio}</td>
      <td>${periodo.nombre}</td>
      <td>${periodo.estado}</td>
      <td>
        <button type="button" data-codigo="${periodo.codigo_periodo}" class="btn-activar-periodo">
          Activar
        </button>
      </td>
    `;

    cuerpoTabla.appendChild(fila);
  });
}

function buscarPeriodoEnTabla(valor) {
  const codigo = valor.trim().toUpperCase();

  return periodosTemporales.find((periodo) => {
    return periodo.codigo_periodo === codigo;
  });
}

function prepararCambioPeriodoActivo(codigo_periodo) {
  const periodo = buscarPeriodoEnTabla(codigo_periodo);

  if (!periodo) {
    mostrarMensajeMaterias("No se encontró el periodo para activar.", "error");
    return;
  }

  periodosTemporales = periodosTemporales.map((item) => {
    return {
      ...item,
      estado: item.codigo_periodo === codigo_periodo ? "activo" : "cerrado"
    };
  });

  renderizarTablaPeriodos(periodosTemporales);
  mostrarMensajeMaterias("Periodo activado visualmente. Falta conectar con Python.", "confirmacion");
}

document.addEventListener("DOMContentLoaded", () => {
  const formularioMateria = document.getElementById("formulario-materia");
  const formularioPeriodo = document.getElementById("formulario-periodo");
  const botonBuscarMateria = document.getElementById("btn-buscar-materia");
  const tablaMaterias = document.getElementById("tabla-materias");
  const tablaPeriodos = document.getElementById("tabla-periodos");

  formularioMateria.addEventListener("submit", (evento) => {
    evento.preventDefault();

    const datos = obtenerDatosFormularioMateria();
    const error = validarFormularioMateria(datos);

    if (error) {
      mostrarMensajeMaterias(error, "error");
      return;
    }

    datos.codigo_materia = `MAT${String(contadorMateriaTemporal).padStart(3, "0")}`;
    contadorMateriaTemporal += 1;
    materiasTemporales.push(datos);

    renderizarTablaMaterias(materiasTemporales);
    limpiarFormularioMateria();
    mostrarMensajeMaterias("Materia agregada visualmente. Falta conectar con Python.", "confirmacion");
  });

  botonBuscarMateria.addEventListener("click", () => {
    const valor = document.getElementById("buscar-materia").value;
    const materia = buscarMateriaEnTabla(valor);

    if (materia) {
      renderizarTablaMaterias([materia]);
      mostrarMensajeMaterias("Materia encontrada en la tabla.", "confirmacion");
    } else {
      renderizarTablaMaterias(materiasTemporales);
      mostrarMensajeMaterias("No se encontró la materia en la tabla.", "error");
    }
  });

  tablaMaterias.addEventListener("click", (evento) => {
    if (evento.target.classList.contains("btn-editar-materia")) {
      prepararActualizacionMateria(evento.target.dataset.codigo);
    }
  });

  formularioPeriodo.addEventListener("submit", (evento) => {
    evento.preventDefault();

    const datos = obtenerDatosFormularioPeriodo();
    const error = validarFormularioPeriodo(datos);

    if (error) {
      mostrarMensajeMaterias(error, "error");
      return;
    }

    if (datos.estado === "activo") {
      periodosTemporales = periodosTemporales.map((periodo) => {
        return {
          ...periodo,
          estado: "cerrado"
        };
      });
    }

    periodosTemporales.push(datos);
    renderizarTablaPeriodos(periodosTemporales);
    limpiarFormularioPeriodo();
    mostrarMensajeMaterias("Periodo agregado visualmente. Falta conectar con Python.", "confirmacion");
  });

  tablaPeriodos.addEventListener("click", (evento) => {
    if (evento.target.classList.contains("btn-activar-periodo")) {
      prepararCambioPeriodoActivo(evento.target.dataset.codigo);
    }
  });
});
