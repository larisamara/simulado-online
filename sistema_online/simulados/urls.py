from django.urls import path
from . import views

urlpatterns = [
    path('criar/', views.criar_simulado, name='criar_simulado'),
    path('listar/', views.listar_simulados, name='listar_simulados'),
    path('listar/por-tema/', views.listar_simulados_por_tema, name='listar_simulados_por_tema'),
    path('responder/<int:simulado_id>/', views.responder_simulado, name='responder_simulado'),
    path('resultado/<int:simulado_id>/', views.resultado_simulado, name='resultado_simulado'),
    path('pesquisar/', views.pesquisar_simulado, name='pesquisar_simulado'),  
]
