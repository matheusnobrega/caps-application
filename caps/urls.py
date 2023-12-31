from django.contrib import admin
from django.urls import path, include
from core.views import index
from core.views import vw_login, vw_register, vw_logout

urlpatterns = [
    path('', index, name="index"),
    path('admin/', admin.site.urls),
    path('pacientes/', include('paciente.urls')),
    path('unidade-acolhimento', include('unidade_acolhimento.urls')),
    path('login/', vw_login, name='vw_login'),
    path('register/', vw_register, name='vw_register'),
    path('logout/', vw_logout, name='vw_logout'),
]
