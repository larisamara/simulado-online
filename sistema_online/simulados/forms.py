from django import forms
from .models import Simulado, QuestaoSimulado

class SimuladoForm(forms.ModelForm):
    class Meta:
        model = Simulado
        fields = ['nome', 'tema']

class QuestaoSimuladoForm(forms.ModelForm):
    class Meta:
        model = QuestaoSimulado
        fields = ['questao', 'pontuacao']

class PesquisaSimuladoForm(forms.Form):
    termo = forms.CharField(label='Pesquisar Simulado', max_length=255)
