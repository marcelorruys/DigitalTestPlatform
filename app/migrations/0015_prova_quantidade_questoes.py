# Generated by Django 5.0.1 on 2024-01-21 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_resposta_respostas'),
    ]

    operations = [
        migrations.AddField(
            model_name='prova',
            name='quantidade_questoes',
            field=models.IntegerField(null=True),
        ),
    ]