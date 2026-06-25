let materiasActuales = [];
let periodosActuales = [];

async function llamarApi(ruta, datos) {
  const respuesta = await fetch(ruta, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(datos || {})
  });
  return await respuesta.json();
}

function mostrarMensajeMaterias(mensaje, tipo) {
  const zonaMensaje = document.getElementById("mensaje-materias");
  zonaMensaje.textContent = mensaje || "";
  zonaMensaje.className = "mensaje " + (tipo || "");
}

function datosMateria() {
  return {
    codigo_materia: document.getElementById("codigo-materia-editar").value.trim(),
    nombre_materia: document.getElementById("nombre-materia").value.trim(),
    docente: document.getElementById("docente").value.trim(),
    ciclo: document.getElementById("ciclo").value.trim(),
    estado: document.getElementById("estado-materia").value
  };
}

function datosPeriodo() {
  return {
    codigo_periodo: document.getElementById("codigo-periodo").value.trim().toUpperCase(),
    anio: document.getElementById("anio-periodo").value.trim(),
    nombre: document.getElementById("nombre-periodo").value.trim(),
    estado: document.getElementById("estado-periodo").value
  };
}

function renderizarTablaMaterias(materias) {
  const cuerpo = document.getElementById("tabla-materias");
  cuerpo.innerHTML = "";
  if (!materias || materias.length === 0) {
    cuerpo.innerHTML = '<tr><td colspan="6">No hay materias para mostrar.</td></tr>';
    return;
  }

  materias.forEach((materia) => {
    const fila = document.createElement("tr");
    fila.innerHTML = `
      <td>${materia.codigo_materia || ""}</td>
      <td>${materia.nombre_materia || ""}</td>
      <td>${materia.docente || ""}</td>
      <td>${materia.ciclo || ""}</td>
      <td>${materia.estado || ""}</td>
      <td><button type="button" class="secundario btn-editar-materia" data-codigo="${materia.codigo_materia || ""}">Editar</button></td>
    `;
    cuerpo.appendChild(fila);
  });
}

function renderizarTablaPeriodos(periodos) {
  const cuerpo = document.getElementById("tabla-periodos");
  cuerpo.innerHTML = "";
  if (!periodos || periodos.length === 0) {
    cuerpo.innerHTML = '<tr><td colspan="5">No hay periodos para mostrar.</td></tr>';
    return;
  }

  periodos.forEach((periodo) => {
    const fila = document.createElement("tr");
    fila.innerHTML = `
      <td>${periodo.codigo_periodo || ""}</td>
      <td>${periodo.anio || ""}</td>
      <td>${periodo.nombre || ""}</td>
      <td>${periodo.estado || ""}</td>
      <td><button type="button" class="secundario btn-usar-periodo" data-codigo="${periodo.codigo_periodo || ""}">Usar</button></td>
    `;
    cuerpo.appendChild(fila);
  });
}

async function guardarMateria() {
  const respuesta = await llamarApi("/api/materias/guardar", datosMateria());
  mostrarMensajeMaterias(respuesta.mensaje, respuesta.resultado ? "exito" : "error");
  if (respuesta.resultado) {
    document.getElementById("formulario-materia").reset();
    document.getElementById("codigo-materia-editar").value = "";
    listarMaterias();
  }
}

async function listarMaterias() {
  const respuesta = await llamarApi("/api/materias/listar");
  materiasActuales = respuesta.datos || [];
  renderizarTablaMaterias(materiasActuales);
}

async function buscarMateria() {
  const codigo = document.getElementById("buscar-materia").value.trim().toUpperCase();
  const respuesta = await llamarApi("/api/materias/buscar", { codigo_materia: codigo });
  mostrarMensajeMaterias(respuesta.mensaje, respuesta.resultado ? "exito" : "error");
  renderizarTablaMaterias(respuesta.resultado ? [respuesta.datos] : materiasActuales);
}

async function actualizarMateria() {
  const datos = datosMateria();
  if (!datos.codigo_materia) {
    mostrarMensajeMaterias("Seleccione una materia con Editar antes de actualizar.", "error");
    return;
  }
  const respuesta = await llamarApi("/api/materias/actualizar", datos);
  mostrarMensajeMaterias(respuesta.mensaje, respuesta.resultado ? "exito" : "error");
  if (respuesta.resultado) {
    document.getElementById("formulario-materia").reset();
    document.getElementById("codigo-materia-editar").value = "";
    listarMaterias();
  }
}

function prepararActualizacionMateria(codigo) {
  const materia = materiasActuales.find((item) => item.codigo_materia === codigo);
  if (!materia) {
    mostrarMensajeMaterias("No se encontro la materia para editar.", "error");
    return;
  }
  document.getElementById("codigo-materia-editar").value = materia.codigo_materia || "";
  document.getElementById("nombre-materia").value = materia.nombre_materia || "";
  document.getElementById("docente").value = materia.docente || "";
  document.getElementById("ciclo").value = materia.ciclo || "";
  document.getElementById("estado-materia").value = materia.estado || "activo";
  mostrarMensajeMaterias("Datos de materia cargados para actualizar.", "info");
}

async function guardarPeriodo() {
  const respuesta = await llamarApi("/api/periodos/guardar", datosPeriodo());
  mostrarMensajeMaterias(respuesta.mensaje, respuesta.resultado ? "exito" : "error");
  if (respuesta.resultado) {
    document.getElementById("formulario-periodo").reset();
    listarPeriodos();
  }
}

async function listarPeriodos() {
  const respuesta = await llamarApi("/api/periodos/listar");
  periodosActuales = respuesta.datos || [];
  renderizarTablaPeriodos(periodosActuales);
}

async function buscarPeriodo() {
  const codigo = document.getElementById("buscar-periodo").value.trim().toUpperCase();
  const respuesta = await llamarApi("/api/periodos/buscar", { codigo_periodo: codigo });
  mostrarMensajeMaterias(respuesta.mensaje, respuesta.resultado ? "exito" : "error");
  renderizarTablaPeriodos(respuesta.resultado ? [respuesta.datos] : periodosActuales);
}

async function activarPeriodo() {
  const codigoFormulario = document.getElementById("codigo-periodo").value.trim().toUpperCase();
  const codigoBusqueda = document.getElementById("buscar-periodo").value.trim().toUpperCase();
  const codigo = codigoFormulario || codigoBusqueda;
  const respuesta = await llamarApi("/api/periodos/activar", { codigo_periodo: codigo });
  mostrarMensajeMaterias(respuesta.mensaje, respuesta.resultado ? "exito" : "error");
  if (respuesta.resultado) {
    listarPeriodos();
  }
}

function usarPeriodo(codigo) {
  document.getElementById("codigo-periodo").value = codigo;
  document.getElementById("buscar-periodo").value = codigo;
  mostrarMensajeMaterias("Periodo seleccionado.", "info");
}

document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("btn-guardar-materia").addEventListener("click", guardarMateria);
  document.getElementById("btn-actualizar-materia").addEventListener("click", actualizarMateria);
  document.getElementById("btn-listar-materias").addEventListener("click", listarMaterias);
  document.getElementById("btn-buscar-materia").addEventListener("click", buscarMateria);
  document.getElementById("btn-guardar-periodo").addEventListener("click", guardarPeriodo);
  document.getElementById("btn-listar-periodos").addEventListener("click", listarPeriodos);
  document.getElementById("btn-buscar-periodo").addEventListener("click", buscarPeriodo);
  document.getElementById("btn-activar-periodo").addEventListener("click", activarPeriodo);
  document.getElementById("tabla-materias").addEventListener("click", (evento) => {
    if (evento.target.classList.contains("btn-editar-materia")) {
      prepararActualizacionMateria(evento.target.dataset.codigo);
    }
  });
  document.getElementById("tabla-periodos").addEventListener("click", (evento) => {
    if (evento.target.classList.contains("btn-usar-periodo")) {
      usarPeriodo(evento.target.dataset.codigo);
    }
  });
  listarMaterias();
  listarPeriodos();
});
