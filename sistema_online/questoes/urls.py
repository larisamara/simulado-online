from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar_questao, name='cadastrar_questao'),
    path('listar/', views.listar_questoes, name='listar_questoes'),
    path('editar/<int:pk>/', views.editar_questao, name='editar_questao'),
]
