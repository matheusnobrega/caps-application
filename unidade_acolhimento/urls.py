from django.urls import path
from . import views

app_name = 'unidade-acolhimento'

urlpatterns = [
    path('', views.detalhe_unidade, name='detalhe_unidade'),
]