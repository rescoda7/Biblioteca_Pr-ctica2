"""Biblioteca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.utils import timezone
from django.views.generic import ListView
from django.contrib import admin
from django.urls import path
from bibliotecaApp.models import Prestec
from django.conf.urls import url
from bibliotecaApp.views import getter, nombres

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ListView.as_view(queryset=Prestec.objects.all(),
        context_object_name='list_prestec',
        template_name='Llibres_biblio.html'), name='list_prestec'),
    path('llibres', ListView.as_view(queryset=Prestec.objects.all(),
                              context_object_name='reserva_llibre',
                              template_name='Lloc_llibre.html'), name='reserva_llibre'),
    path('llibres/disponibles', ListView.as_view(queryset=Prestec.objects.all(),
                                      context_object_name='llibre_disp',
                                      template_name='Llibres_disponibles.html'), name='llibre_disp'),
    path('llibres/nodisponibles', ListView.as_view(queryset=Prestec.objects.all(),
                                      context_object_name='llibre_nodisp',
                                      template_name='Llibres_nodisponibles.html'), name='llibre_nodisp'),
    url('/prestec', getter, name='realitzar_prest'),
    path('llibres/cerca', ListView.as_view(queryset=Prestec.objects.all(),
                                   context_object_name='busqueda_llibre',
                                   template_name='CercaLlibre.html'), name='busqueda_llibre'),
    url('/llibres/2', nombres, name='reserva_llibre2'),


]
""" url('/llibres/cerca/', getter, name='busqueda_libre'),"""