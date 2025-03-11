from django.shortcuts import render

# Aqui fica a primeira view
def index(request):
    return render(
        request,
        'sistema/index.html',
    )

# REQUEST - RESPONSE - RENDER