from django.shortcuts import render

from bibliotecaApp.models import Prestec


def getter(request):
    queryset = request.GET.get("reserva")
    obj = Prestec.objects.filter(llibres__id=queryset)
    return render(request,'AceptarPrestamo.html',{"realitzar_view":obj})

def nombres(request):
    queryset = request.GET.get("cerca")
    obj = Prestec.objects.filter(llibres__id=queryset)
    return render(request,'AceptarPrestamo.html',{"realitzar_view":obj})