from django.shortcuts import render

from sistema.models import Medico


def listarMedicos(request):
    medicos = Medico.objects.all()

    context = {
        'medicos': medicos,
    }
    
    return render(
        request,
        'medico/listar.html',
        context,
    )



