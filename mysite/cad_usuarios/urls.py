from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from sorveteria.views import itemsView

urlpatterns = [
    path('', views.index, name = 'index'),
    path('cadastro/', views.cadastro, name = 'cadastro'),
    path('itemsView/', views.index, name='itemsView'),
    path('gerenciarUsuarios/', views.gerenciarUsuarios, name='gerenciarUsuarios'),
    path('apagarUsuario/', views.apagarUsuario, name='apagarUsuario')
]