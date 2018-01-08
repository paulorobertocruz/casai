from django.shortcuts import render

from .models import Fluxo

def relatorio(request):
    template_name = "relatorios/relatorio.html"
    context = {}
    
    ocupacao_atual = Fluxo.objects.filter(data_saida = None)
    
    context["ocupacao_paciente"] = ocupacao_atual.filter(tipo = "PACIENTE")
    context["ocupacao_acompanhate"] = ocupacao_atual.filter(tipo = "ACOMPANHANTE")
    context["ocupacao_transito"] = ocupacao_atual.filter(tipo = "TRANSITO")

    return render(request, template_name, context)