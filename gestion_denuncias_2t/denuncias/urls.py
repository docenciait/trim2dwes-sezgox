from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='lista_denuncias'),
    path('crear/', views.create, name='crear_denuncia'),
    path('eliminar/<int:id>/', views.delete, name='eliminar_denuncia.'),
    path('editar/<int:id>/', views.edit, name='editar_denuncia.'),
]
