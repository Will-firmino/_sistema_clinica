from django.shortcuts import render

# Aqui fica a primeira view
def index(request):

    return render(
        request,
        'global/base.html',
    )

# Testando
def teste(request):
    return render(
        request,
        'global/teste.html'
    )


# REQUEST - RESPONSE - RENDER