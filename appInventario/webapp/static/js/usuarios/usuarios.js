function listadoUsuarios() {
    $.ajax({
        url: "/usuarios",
        type: "get",
        dataType: "json",
        success: function (response) {
            $('#tabla_usuarios').html();
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

                fila += '<td>' +
                    '<button class="btn btn-warning">Editar</button>' +
                    '<button class="btn btn-danger">Bloquear</button>' +
                    '<button class="btn btn-info">Password</button></td>';
                fila += '</tr>';
                $('#tabla_usuarios').append(fila)
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

function abrir_modal_cambiarEstado(url) {
    $('#ventanaModal').load(url, function () {
        $(this).modal('show');
    });
}

function abrir_modal_editar(url) {
    $('#ventanaModal').load(url, function () {
        $(this).modal('show');
    });
}

function abrir_modal_resetpass(url) {
    $('#ventanaModal').load(url, function () {
        $(this).modal('show');
    });
}

function abrir_modal_crearUsuario(url) {
    $('#ventanaModal').load(url, function () {
        $(this).modal('show');
    });
}
