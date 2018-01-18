from django.shortcuts import render

from .models import Usuario, Etnia, Aldeia

def usuario(request):
    template_name = "identidade/usuario.html"
    context = {}
    
    numero_prontuario = request.GET.get("numero_prontuario", None)

    nome = request.GET.get("nome", None)
    nome_mae = request.GET.get("nome_mae", None)
    sexo = request.GET.get("sexo", None)
    
    context["etnias"] = Etnia.objects.all()
    context["aldeias"] = Aldeia.objects.all()
    
    if sexo != "F" and sexo != "M":
        sexo = None
    
    usuarios = Usuario.objects.all()
    
    filtered = False

    if numero_prontuario is not None and numero_prontuario is not "":
        usuarios = usuarios.filter(prontuario__numero = numero_prontuario)
        filtered = True

    if nome is not None and nome is not "":
        usuarios = usuarios.filter(nome__icontains = nome)
        filtered = True
    
    if nome_mae is not None and nome_mae is not "":
        usuarios = usuarios.filter(nome_mae__icontains = nome_mae)
        filtered = True

    if sexo is not None:
        usuarios = usuarios.filter(sexo = sexo)
        filtered = True

    if not filtered:
        usuarios = None

    context["usuarios"] = usuarios

    return render(request, template_name, context)