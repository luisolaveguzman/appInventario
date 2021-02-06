from django.shortcuts import render
from django.views.generic import TemplateView

"""
    Como funciiona Wiew
    dispatch(): Valida la petición y elige que metodo http se utilizo para la solicitud por el template
    http_metho_not_allowed(): retorna error cuando se utiliza un metodo http no soportado o definido
    options(): responde a peticios options
    
    View se utiliza para trabajar logica
    TemplateView se utiliza para renderizar un template
"""

#vista basada en clases
class TableroView(TemplateView):
    template_name = 'app/tablero.html'

    """ Ejemplo en ves de escribir template_name
    def get(self, request, *args, **kwargs):
        return render(request, 'app/tablero.html')
    """

#vista basada en funciones
def tablero(request):
    return render(request, 'app/tablero.html')