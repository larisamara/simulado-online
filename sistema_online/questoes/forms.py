from django import forms
from .models import Questao

class QuestaoForm(forms.ModelForm):
    class Meta:
        model = Questao
        fields = ['enunciado', 'alternativa_a', 'alternativa_b', 'alternativa_c', 'alternativa_d', 'peso', 'resposta_correta']
