# Generated by Django 5.1.1 on 2024-09-20 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enunciado', models.CharField(max_length=255)),
                ('alternativa_a', models.CharField(max_length=255)),
                ('alternativa_b', models.CharField(max_length=255)),
                ('alternativa_c', models.CharField(max_length=255)),
                ('alternativa_d', models.CharField(max_length=255)),
                ('peso', models.IntegerField()),
                ('resposta_correta', models.CharField(choices=[('A', 'Alternativa A'), ('B', 'Alternativa B'), ('C', 'Alternativa C'), ('D', 'Alternativa D')], max_length=1)),
            ],
        ),
    ]
