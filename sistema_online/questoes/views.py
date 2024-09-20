from django.shortcuts import render, redirect, get_object_or_404
from .models import Questao
from .forms import QuestaoForm

def cadastrar_questao(request):
    if request.method == 'POST':
        form = QuestaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_questoes')
    else:
        form = QuestaoForm()
    return render(request, 'cadastrar.html', {'form': form})

def listar_questoes(request):
    questoes = Questao.objects.all()
    return render(request, 'listar.html', {'questoes': questoes})

def editar_questao(request, pk):
    questao = get_object_or_404(Questao, pk=pk)
    if request.method == 'POST':
        form = QuestaoForm(request.POST, instance=questao)
        if form.is_valid():
            form.save()
            return redirect('listar_questoes')
    else:
        form = QuestaoForm(instance=questao)
    return render(request, 'editar.html', {'form': form, 'questao': questao})
