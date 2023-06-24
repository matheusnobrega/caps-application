from django.contrib import admin
from .models import Paciente, Droga

admin.site.register([Paciente, Droga])
