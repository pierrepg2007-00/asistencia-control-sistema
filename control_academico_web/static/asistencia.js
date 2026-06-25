/* Funciones JavaScript para la gestion de asistencia */

function obtenerDatosFormularioAsistencia() {
    /* Captura los datos del formulario de asistencia */
    return {
        codigo_estudiante: document.getElementById("codigo-estudiante").value.trim(),
        codigo_materia: document.getElementById("codigo-materia").value.trim(),
        codigo_periodo: document.getElementById("codigo-periodo").value.trim(),
        fecha: document.getElementById("fecha").value.trim(),
        estado_asistencia: document.getElementById("estado-asistencia").value
    };
}

function validarFormularioAsistencia(datos) {
    /* Valida que los campos requeridos no esten vacios */
    var errores = [];

    if (!datos.codigo_estudiante) {
        errores.push("El codigo de estudiante no puede estar vacio.");
    }
    if (!datos.codigo_materia) {
        errores.push("El codigo de materia no puede estar vacio.");
    }
    if (!datos.codigo_periodo) {
        errores.push("El codigo de periodo no puede estar vacio.");
    }
    if (!datos.fecha) {
        errores.push("La fecha no puede estar vacia.");
    }
    if (!datos.estado_asistencia) {
        errores.push("Debe seleccionar un estado de asistencia.");
    }

    return errores;
}

function mostrarMensajeAsistencia(mensaje, tipo) {
    /* Muestra un mensaje en la seccion de mensajes */
    var seccion = document.getElementById("mensajes-asistencia");
    var clase = tipo === "error" ? "mensaje-error" : "mensaje-exito";
    seccion.innerHTML = '<div class="' + clase + '">' + mensaje + '</div>';
}

function limpiarFormularioAsistencia() {
    /* Limpia todos los campos del formulario */
    document.getElementById("codigo-estudiante").value = "";
    document.getElementById("codigo-materia").value = "";
    document.getElementById("codigo-periodo").value = "";
    document.getElementById("fecha").value = "";
    document.getElementById("estado-asistencia").value = "";
}

function renderizarTablaAsistencia(asistencias) {
    /* Llena la tabla con los registros de asistencia */
    var tbody = document.getElementById("tbody-asistencias");
    tbody.innerHTML = "";

    if (!asistencias || asistencias.length === 0) {
        tbody.innerHTML = '<tr><td colspan="6">No hay registros de asistencia.</td></tr>';
        return;
    }

    for (var i = 0; i < asistencias.length; i++) {
        var a = asistencias[i];
        var fila = '<tr>';
        fila += '<td>' + (a.codigo_estudiante || "") + '</td>';
        fila += '<td>' + (a.codigo_materia || "") + '</td>';
        fila += '<td>' + (a.codigo_periodo || "") + '</td>';
        fila += '<td>' + (a.fecha || "") + '</td>';
        fila += '<td>' + (a.estado_asistencia || "") + '</td>';
        fila += '<td>-</td>';
        fila += '</tr>';
        tbody.innerHTML += fila;
    }
}

function filtrarAsistenciaPorEstudiante(codigo_estudiante) {
    /* Prepara la busqueda de asistencia por estudiante */
    console.log("Filtrar asistencia por estudiante:", codigo_estudiante);
}

function filtrarAsistenciaPorMateria(codigo_materia, codigo_periodo, fecha) {
    /* Prepara la busqueda de asistencia por materia y periodo */
    console.log("Filtrar asistencia por materia:", codigo_materia, codigo_periodo, fecha);
}

function prepararCalculoPorcentaje(codigo_estudiante, codigo_materia, codigo_periodo) {
    /* Prepara el calculo del porcentaje de asistencia */
    console.log("Calcular porcentaje para:", codigo_estudiante, codigo_materia, codigo_periodo);
}

/* Conexion de eventos con los botones */

document.getElementById("btn-guardar-asistencia").addEventListener("click", function () {
    var datos = obtenerDatosFormularioAsistencia();
    var errores = validarFormularioAsistencia(datos);

    if (errores.length > 0) {
        mostrarMensajeAsistencia(errores.join(" "), "error");
        return;
    }

    mostrarMensajeAsistencia("Funcion de guardado pendiente de integracion con Python.", "exito");
    limpiarFormularioAsistencia();
});

document.getElementById("btn-listar-por-estudiante").addEventListener("click", function () {
    var codigo = document.getElementById("filtro-codigo-estudiante").value.trim();
    if (!codigo) {
        mostrarMensajeAsistencia("Ingrese un codigo de estudiante.", "error");
        return;
    }
    filtrarAsistenciaPorEstudiante(codigo);
    mostrarMensajeAsistencia("Busqueda pendiente de integracion.", "exito");
});

document.getElementById("btn-listar-por-materia").addEventListener("click", function () {
    var materia = document.getElementById("filtro-codigo-materia").value.trim();
    var periodo = document.getElementById("filtro-codigo-periodo").value.trim();
    var fecha = document.getElementById("filtro-fecha").value.trim();

    if (!materia || !periodo) {
        mostrarMensajeAsistencia("Ingrese codigo de materia y periodo.", "error");
        return;
    }

    filtrarAsistenciaPorMateria(materia, periodo, fecha || null);
    mostrarMensajeAsistencia("Busqueda pendiente de integracion.", "exito");
});

document.getElementById("btn-calcular-porcentaje").addEventListener("click", function () {
    var estudiante = document.getElementById("calc-codigo-estudiante").value.trim();
    var materia = document.getElementById("calc-codigo-materia").value.trim();
    var periodo = document.getElementById("calc-codigo-periodo").value.trim();

    if (!estudiante || !materia || !periodo) {
        mostrarMensajeAsistencia("Complete todos los campos para calcular el porcentaje.", "error");
        return;
    }

    prepararCalculoPorcentaje(estudiante, materia, periodo);
    mostrarMensajeAsistencia("Calculo pendiente de integracion.", "exito");
});
