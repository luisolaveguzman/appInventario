from django.shortcuts import render


def tablero(request):
    return render(request, 'app/tablero.html')