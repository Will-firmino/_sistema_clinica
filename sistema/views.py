from django.shortcuts import render

# Aqui fica a primeira view
def index(request):

    return render(
        request,
        'global/base.html',
    )

# REQUEST - RESPONSE - RENDER