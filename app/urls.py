from django.urls import path

from .views import index, index_questao, criar_questao, editar_questao, deletar_questao, index_prova


urlpatterns = [
    path('', index, name='index'),
    
    path('questoes/', index_questao, name='index_questao'),
    path('questoes/criar', criar_questao, name='criar_questao'),
    path('questoes/editar/<int:id>', editar_questao, name='editar_questao'),
    path('questoes/deletar/<int:id>', deletar_questao, name='deletar_questao'),

    path('prova/', index_prova, name='questoes'),
    path('prova/criar', criar_questao, name='criar_questao'),
    path('prova/editar/<int:id>', editar_questao, name='editar_prova'),
    path('prova/deletar/<int:id>', deletar_questao, name='deletar_prova'),
]
