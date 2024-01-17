from django.contrib import admin

from .models import Questao, Prova, Candidato, Resposta


class QuestoesAdmin(admin.ModelAdmin):
    list_display = ('materia', 'dificuldade')
    

admin.site.register(Questao)
admin.site.register(Prova)
admin.site.register(Candidato)
admin.site.register(Resposta)