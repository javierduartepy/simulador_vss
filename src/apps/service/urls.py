 # src/apps/service/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('disparar/', views.coordinar_disparo_vss, name='vss_disparar'),
    path('restaurar/', views.coordinar_restauracion_vss, name='vss_restaurar'),
]

