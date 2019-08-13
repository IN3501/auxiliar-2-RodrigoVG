from django.contrib import admin
from django.urls import path
from . import views

urlpatterns= [
	path('',views.index, name='index'),
	path('pestaña/', views.pestaña, name='pestaña'),
	path('equipo_docente/', views.equipo_docente, name='equipo_docente')
]