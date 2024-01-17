from django.urls import path

from .views import index, questoes_index, criar_questao, editar_questao, deletar_questao


urlpatterns = [
    path('', index, name='index'),
    
    path('questoes/', questoes_index, name='questoes'),
    path('questoes/criar', criar_questao, name='criar_questao'),
    path('questoes/editar/<int:id>', editar_questao, name='editar_questao'),
    path('questoes/deletar/<int:id>', deletar_questao, name='deletar_questao'),
]
