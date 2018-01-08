from django.shortcuts import render

from .models import Usuario

def usuario(request):
    template_name = "identidade/usuario.html"
    context = {}
    
    nome = request.GET.get("nome", None)
    nome_mae = request.GET.get("nome_mae", None)
    sexo = request.GET.get("sexo", None)
    
    if sexo != "F" and sexo != "M":
        sexo = None
    
    usuarios = Usuario.objects.all()
    

    if nome is not None:
        usuarios = usuarios.filter(nome__icontains = nome)
        filtered = True
    
    if nome_mae is not None:
        usuarios = usuarios.filter(nome_mae__icontains = nome_mae)
        filtered = True

    if sexo is not None:
        usuarios = usuarios.filter(sexo = sexo)
        filtered = True
    
    context["usuarios"] = usuarios

    return render(request, template_name, context)