# Generated by Django 5.0.1 on 2024-01-17 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_questao_correta_alter_questao_dificuldade'),
    ]

    operations = [
        migrations.AddField(
            model_name='prova',
            name='titulo',
            field=models.TextField(blank=True),
        ),
    ]