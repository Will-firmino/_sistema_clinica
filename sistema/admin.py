from django.contrib import admin

# Importação do módulo models.py
from sistema import models


# Aqui fica o registro do model do Paciente
@admin.register(models.Paciente)
