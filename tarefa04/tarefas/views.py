from django.shortcuts import render

from .models import Tarefa
from datetime import date

def lista_tarefas(request):
    hoje = date.today()
    tarefas = Tarefa.objects.all()
    return render(request, 'tarefas/index.html', {
        'tarefas': tarefas,
        'hoje':hoje })
