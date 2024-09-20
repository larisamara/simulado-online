from django.db import models

class Questao(models.Model):
    enunciado = models.CharField(max_length=255)
    alternativa_a = models.CharField(max_length=255)
    alternativa_b = models.CharField(max_length=255)
    alternativa_c = models.CharField(max_length=255)
    alternativa_d = models.CharField(max_length=255)
    peso = models.IntegerField()
    resposta_correta = models.CharField(max_length=1, choices=[
        ('A', 'Alternativa A'),
        ('B', 'Alternativa B'),
        ('C', 'Alternativa C'),
        ('D', 'Alternativa D'),
    ])

    def __str__(self):
        return self.enunciado
