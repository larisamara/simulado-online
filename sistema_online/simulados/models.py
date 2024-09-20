from django.db import models

from questoes.models import Questao

class Simulado(models.Model):
    nome = models.CharField(max_length=255)
    tema = models.CharField(max_length=255)  # Adicionando tema
    questoes = models.ManyToManyField(Questao, through='QuestaoSimulado')

    def __str__(self):
        return self.nome

class QuestaoSimulado(models.Model):
    simulado = models.ForeignKey(Simulado, on_delete=models.CASCADE)
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)
    pontuacao = models.IntegerField()

    class Meta:
        unique_together = ('simulado', 'questao')

class Resposta(models.Model):
    simulado = models.ForeignKey(Simulado, on_delete=models.CASCADE)
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    resposta = models.CharField(max_length=1)  # A, B, C ou D

    class Meta:
        unique_together = ('simulado', 'questao', 'usuario')
        