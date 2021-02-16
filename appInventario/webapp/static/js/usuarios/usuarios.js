//Inicio funcion para listar usuarios
function listadoUsuarios() {
    $.ajax({
        url: "/usuarios",
        type: "get",
        dataType: "json",
        success: function (response) {
            console.log(response);
            if ($.fn.DataTable.isDataTable('#tabla_usuarios')) {
                $('#tabla_usuarios').DataTable().destroy();
            }
            $('#tabla_usuarios tbody').html(""); //vacia el contenido para rellenar
            for (let i = 0; i < response.length; i++) {
                let fila = '<tr>';
                fila += '<td>' + (i + 1) + '</td>';
                fila += '<td>' + response[i]['fields']['rut'] + '</td>';
                fila += '<td>' + response[i]['fields']['username'] + '</td>';
                fila += '<td>' + response[i]['fields']['nombres'] + '</td>';
                fila += '<td>' + response[i]['fields']['apellidos'] + '</td>';
                fila += '<td>' + response[i]['fields']['correo'] + '</td>';
                if (response[i]['fields']['estado']) {
                    fila += '<td>Activo</td>';
                } else
                    fila += '<td>Bloqueado</td>';
                console.log('Activo')

                if (response[i]['fields']['user_administrador']) {
                    fila += '<td>Administrador</td>';
                } else
                    fila += '<td>Usuario</td>';

                fila += '<td class="text-center btn-group-sm">'
                fila += '<button type="button" class="btn btn-warning" onclick="abrir_modal_editar(\'/editarUsuario/' + response[i]['pk'] + '\');">Editar</button>' + '<span>&nbsp;&nbsp;</span>'
                fila += '<button type="button" class="btn btn-danger">Eliminar</button>' + '<span>&nbsp;&nbsp;</span>'
                fila += '<button type="button" class="btn btn-info" onclick="abrir_modal_password(\'/cambiarClave/' + response[i]['pk'] + '\')">Password</button></td>';
                fila += '</tr>';
                $('#tabla_usuarios tbody').append(fila)
            }
            $('#tabla_usuarios').DataTable({
                language: {
                    decimal: "",
                    emptyTable: "No hay información",
                    info: "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
                    infoEmpty: "Mostrando 0 al 0 de 0 entradas",
                    infoFiltered: "(Filtrado de _MAX_ total entradas)",
                    infoPostFix: "",
                    thousands: ",",
                    lengthMenu: "Mostrar _MENU_ Entradas",
                    loadingRecords: "Cargando...",
                    processing: "Procesando...",
                    search: "Buscar:",
                    zeroRecords: "Sin resultados encontrados",
                    paginate: {
                        first: "Primero",
                        last: "Ultimo",
                        next: "Siguiente",
                        previous: "Anterior",
                    },
                },
            });
            console.log(response)
        },
        error: function (error) {
            console.log(error)
        }
    });
}

$(document).ready(function () {
    listadoUsuarios()
});

//Fin funcion listar usuarios

//Inicio modales
function abrir_modal_crearUsuario(url) {
    $('#ventanaModal').load(url, function () {
        $(this).modal('show');
    });
}

function abrir_modal_editar(url) {
    $('#ventanaModal').load(url, function () {
        $(this).modal('show');
    });
}

function abrir_modal_password(url){
        $('#ventanaModal').load(url, function (){
            $(this).modal('show');
        });
    }

function cerrar_modal() {
    $('#ventanaModal').modal('hide');
}

function registrar() {
    //activarBoton();
    $.ajax({
        data: $('#form_crear').serialize(),
        url: $('#form_crear').attr('action'),
        type: $('#form_crear').attr('method'),
        success: function (response) {
            activarBoton();
            notificacionCrear(response.mensaje);
            listadoUsuarios();
            cerrar_modal();
        },
        error: function (error) {
            notificacionError(error.responseJSON.mensaje);
            mostrarErrores(error);
            //activarBoton();
            console.log(error);
        }
    })
}

function editar() {
    $.ajax({
        data: $('#form_edicion').serialize(),
        url: $('#form_edicion').attr('action'),
        type: $('#form_edicion').attr('method'),
        success: function (response) {
            activarBoton();
            notificacionActualizar(response.mensaje);
            listadoUsuarios();
            cerrar_modal();
        },
        error: function (error) {
            console.log(error);
        }
    });
}

function cambiar_password() {
    $.ajax({
        data: $('#form_reset_password').serialize(),
        url: $('#form_reset_password').attr('action'),
        type: $('#form_reset_password').attr('method'),
        success: function (response) {
            activarBoton();
            notificacionActualizar(response.mensaje)
            listadoUsuarios();
            cerrar_modal();
        },
        error: function (error) {
            console.log(error);
        }
    });
}

function activarBoton() {
    if ($('#boton_creacion').prop('disabled')) {
        $('#boton_creacion').prop('disabled', false);
    } else {
        $('#boton_creacion').prop('disabled', true);
    }
}

//fin modales

/*Inicio errores en los modales
function mostrarErrores(errores) {
    $("div.help-block").remove();
    for (var error in errores.responseJSON.error) {
        $('#form_crear #' + error).addClass('is-invalid').append(errores.responseJSON.error[error]);
        console.log(error)
    }
}*/
/*
function mostrarErroresEdicion(errores) {
    $("div.help-block").remove();
    for (var error in errores.responseJSON.error) {
        $('#form_edicion #' + error).addClass('is-invalid');
        $('#form_edicion #' + error).append('<div class="help-block">' + errores.responseJSON.error[error] + '</div>');
    }
}*/

/*
$("#button").on("click", function() {
	if ($("#boton_creacion").next('p').length) $("input").nextAll('p').empty();
	for (var name in data) {
    for (var i in data[name]) {
      // object message error django
      var $input = $("input[name='"+ name +"']");
      $input.after("<p>" + data[name][i].message + "</p>");
    }
  }
});
*/
//Fin errores en los modales

//Inicio notificaciones sweet alert
function notificacionError(mensaje) {
    Swal.fire({
        title: 'Error',
        text: mensaje,
        icon: 'error'
    })
}

function notificacionCrear(mensaje) {
    Swal.fire({
        title: 'Registro Creado con exito',
        text: mensaje,
        icon: 'success'
    })
}

function notificacionActualizar(mensaje) {
    Swal.fire({
        title: 'Registro actualizado con exito',
        text: mensaje,
        icon: 'success'
    })
}

function notificacionActualizarClave(mensaje) {
    Swal.fire({
        title: 'Clave actualizada con exito',
        text: mensaje,
        icon: 'success'
    })
}


//Fin notificaciones Sweet alert