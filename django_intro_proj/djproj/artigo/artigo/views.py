from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .form import ArtigoForm


def artigo_cadastro(request):
    msg = None

    formulario = ArtigoForm()

    if request.POST:
        formulario = ArtigoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            formulario = ArtigoForm()
            msg = "Salvo com sucesso"
    
    return render(
        request,
        'artigo_form.html',
        context={
            'formulario': formulario,
            'erros': formulario.erros,
            'msg': msg
        }
    )