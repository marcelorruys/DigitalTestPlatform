# Generated by Django 5.0.1 on 2024-01-18 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_prova_titulo_alter_questao_peso_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prova',
            name='titulo',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questao',
            name='peso',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='questao',
            name='titulo',
            field=models.TextField(null=True),
        ),
    ]
