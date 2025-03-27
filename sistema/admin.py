from django.contrib import admin


""""""
# Importação do módulo models.py
from sistema import models 


# Aqui fica o registro do model do Paciente
@admin.register(models.Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'email', 'telefone', 'ativo',)
    list_editable = ('ativo',)
    search_fields = ('id', 'nome', 'email',)
    
   
# Aqui fica o registro do model da Especialidade
@admin.register(models.Especialidade)
class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome',)


# Aqui fica o registro do model do Médico
@admin.register(models.Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'email', 'crm', 'ativo',)
    list_editable = ('ativo',)

# Aqui fica o registro do model da Consulta
@admin.register(models.Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('id', 'paciente_id', 'medico_id', 'status')