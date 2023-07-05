from django.urls import path

from . import views
from cad_usuarios.views import gerenciarUsuarios

urlpatterns = [
    path('', views.itemsView, name = 'itemsView'),
    path('cadastroitem/', views.cadastroitem, name = 'cadastroitem'),
    path('comprarItem/', views.comprarItem, name = 'comprarItem'),
    path('atualizarItem/', views.atualizarItem, name = 'atualizarItem'),
    path('apagarItem/', views.apagarItem, name = 'apagarItem'),
    path('gerenciarUsuarios/', views.gerenciarUsuarios, name = 'gerenciarUsuarios')
]
