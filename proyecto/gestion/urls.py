"""
URL configuration for proyecto project.

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('autores/', views.lista_autores, name='lista_autores'),
    path('autores/crear/', views.crear_autor, name='crear_autor'),
    path('autores/editar/<int:pk>/', views.editar_autor, name='editar_autor'),
    path('autores/eliminar/<int:pk>/', views.eliminar_autor, name='eliminar_autor'),
]