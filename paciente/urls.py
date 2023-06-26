from django.urls import path
from . import views

app_name = 'paciente'

urlpatterns = [
    path('', views.cadastrar_paciente, name='cadastrar_paciente'),
    path('listar/', views.listar_pacientes, name='listar_pacientes'),
    path('<int:pk>/', views.detalhe_paciente, name='detalhe_paciente'),
    path('<int:pk>/consumo', views.adiciona_droga, name='adiciona_droga'),
    path('<int:pk>/evolucao', views.adiciona_evolucao, name='adiciona_evolucao'),
    path('<int:pk>/unidade_acolhimento', views.insere_unidade_acolhimento, name='insere_unidade_acolhimento'),
]