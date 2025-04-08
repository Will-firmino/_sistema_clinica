from django.shortcuts import render
from sistema.models import Paciente

def listarPacientes(request):
    pacientes = Paciente.objects.all() # Variável pacientes está guardando todos os objetos da tabela Paciente.

    context = { # Declaração de um dict que possui a chave pacientes e o valor pacientes(variável criada acima).
        'pacientes': pacientes,
    }

    return render(
        request,
        'paciente/listar.html',
        context,
    )