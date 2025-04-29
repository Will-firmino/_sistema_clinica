from django.shortcuts import render, redirect
from sistema.forms import MedicoForm

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


def criarMedico(request):
    if request.method == 'POST':
        form = MedicoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/medicos')
    else:
        form = MedicoForm()
    return render(request, 'medico/cadastro.html', {'form': form})


