from django.urls import path
from pre_entrega3 import views


urlpatterns = [
    path('',views.inicio, name='home' ),
    path('alta_alumnos',views.formulario_alumno, name='alumnos'),
    path('confirmacion',views.confirmacion),
    path('profesores', views.formulario_profesor),
    path('instituciones', views.formulario_institucion),
    path('ver_datos', views.ver_opciones),
    path('read_alumnos',views.mostrar_datos_alumnos, name='ver_alumnos'),
    path('read_profesores', views.mostrar_datos_profesores, name='ver_profesores'),
    path('read_instituciones', views.mostrar_datos_instituciones, name='ver_instituciones'),
    path('buscar_alumnos', views.buscar_alumnos, name='busqueda_alumnos'),
    path('buscar', views.buscar),
    path('opciones_busqueda', views.busqueda_opciones, name='opciones_busqueda'),
    path('buscar_profesores', views.buscar_profesores, name='busqueda_profesores'),
    path('buscar_instituciones', views.buscar_instituciones, name='busqueda_instituciones'),
    path('resultado_busqueda_alumno', views.resultado_busqueda_alumnos, name='resultado_alumnos')
    # path('confirmacion', 'confirmacion.html')
]