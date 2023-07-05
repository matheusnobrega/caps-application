from django.urls import path
from . import views

app_name = 'paciente'

urlpatterns = [
    path('', views.cadastrar_paciente, name='cadastrar_paciente'),
    path('listar/', views.listar_pacientes, name='listar_pacientes'),
    path('estatisticas/', views.apresenta_estatisticas, name="apresenta_estatisticas"),
    path('<int:pk>/', views.detalhe_paciente, name='detalhe_paciente'),
    path('<int:pk>/consumo', views.adiciona_droga, name='adiciona_droga'),
    path('<int:pk>/remove_consumo/<int:dp_pk>', views.remove_droga, name='remove_droga'),
    path('<int:pk>/evolucao', views.adiciona_evolucao, name='adiciona_evolucao'),
    path('<int:pk>/unidade_acolhimento', views.insere_unidade_acolhimento, name='insere_unidade_acolhimento'),
    path('<int:pk>/remove_unidade_acolhimento', views.remove_unidade_acolhimento, name='remove_unidade_acolhimento'),
]