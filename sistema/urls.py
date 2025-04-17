# São as importações realizadas de forma a utilizar partes do django.
from django.urls import path
# Importação do diretório views, onde tem a view index e a view listarPacientes
from sistema import views

app_name = 'sistema'

# Lista responsável por organizar as urls do sistema.
urlpatterns = [
    path('', views.index, name='index'),
    path('pacientes/', views.listarPacientes, name='pacientes'),
    path('pacientes/novo/', views.criarPaciente, name='criar_paciente'),
    path('pacientes/perfil/<int:paciente_id>', views.perfilPaciente, name='perfil_paciente'),
    path('medicos/', views.listarMedicos, name='medicos'),
    path('medicos/novo/', views.criarMedico, name ='criar_medico')

]

