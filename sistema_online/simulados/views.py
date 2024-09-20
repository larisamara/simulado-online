from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Questao, Simulado, QuestaoSimulado, Resposta
from .forms import SimuladoForm, PesquisaSimuladoForm

@login_required(login_url='/usuarios/login')
def criar_simulado(request):
    if request.method == 'POST':
        form = SimuladoForm(request.POST)
        if form.is_valid():
            simulado = form.save()
            questoes_ids = request.POST.getlist('questoes')
            pontuacoes = request.POST.getlist('pontuacoes')

            for questao_id, pontuacao in zip(questoes_ids, pontuacoes):
                QuestaoSimulado.objects.create(simulado=simulado, questao_id=questao_id, pontuacao=pontuacao)

            return redirect('listar_simulados')
    else:
        form = SimuladoForm()

    questoes = Questao.objects.all()
    return render(request, 'criar_simulado.html', {'form': form, 'questoes': questoes})
  
def listar_simulados(request):
    simulados = Simulado.objects.all()
    return render(request, 'listar_simulados.html', {'simulados': simulados})

def listar_simulados_por_tema(request):
    simulados = Simulado.objects.all()
    temas = {}
    
    for simulado in simulados:
        if simulado.tema not in temas:
            temas[simulado.tema] = []
        temas[simulado.tema].append(simulado)

    return render(request, 'listar_simulados_por_tema.html', {'temas': temas})
  
def resultado_simulado(request, simulado_id):
    simulado = Simulado.objects.get(id=simulado_id)
    questoes = QuestaoSimulado.objects.filter(simulado=simulado)

    total_pontos = 0
    respostas_certas = 0
    respostas_erradas = 0
    respostas_usuario = Resposta.objects.filter(simulado=simulado, usuario=request.user)

    resultados = []

    for questao in questoes:
        resposta_usuario = respostas_usuario.filter(questao=questao.questao).first()
        pontos = questao.pontuacao

        if resposta_usuario:
            correta = questao.questao.resposta_correta
            if resposta_usuario.resposta == correta:
                respostas_certas += 1
                total_pontos += pontos
                resultados.append({
                    'enunciado': questao.questao.enunciado,
                    'resposta_usuario': resposta_usuario.resposta,
                    'resultado': 'Certa',
                    'pontos': pontos
                })
            else:
                respostas_erradas += 1
                resultados.append({
                    'enunciado': questao.questao.enunciado,
                    'resposta_usuario': resposta_usuario.resposta,
                    'resultado': 'Errada',
                    'pontos': 0
                })
        else:
            resultados.append({
                'enunciado': questao.questao.enunciado,
                'resposta_usuario': 'Não respondida',
                'resultado': 'Não respondida',
                'pontos': 0
            })

    return render(request, 'resultado_simulado.html', {
        'simulado': simulado,
        'resultados': resultados,
        'total_pontos': total_pontos,
        'respostas_certas': respostas_certas,
        'respostas_erradas': respostas_erradas,
    })

def responder_simulado(request, simulado_id):
    simulado = Simulado.objects.get(id=simulado_id)
    questoes = QuestaoSimulado.objects.filter(simulado=simulado)

    if request.method == 'POST':
        for questao in questoes:
            resposta = request.POST.get(str(questao.questao.id))
            Resposta.objects.update_or_create(
                simulado=simulado,
                questao=questao.questao,
                usuario=request.user,
                defaults={'resposta': resposta}
            )
        return redirect('resultado_simulado', simulado_id=simulado.id)

    return render(request, 'responder_simulado.html', {'simulado': simulado, 'questoes': questoes})

def pesquisar_simulado(request):
    resultados = []
    form = PesquisaSimuladoForm()

    if request.method == 'POST':
        form = PesquisaSimuladoForm(request.POST)
        if form.is_valid():
            termo = form.cleaned_data['termo']
            resultados = Simulado.objects.filter(nome__icontains=termo)

    return render(request, 'pesquisar_simulado.html', {
        'form': form,
        'resultados': resultados,
    })